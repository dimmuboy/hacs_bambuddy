"""BamBuddy number entities for offsets and adjustments."""
from __future__ import annotations

import logging

from homeassistant.components.number import NumberEntity, NumberEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .api import BamBuddyClient
from .const import DOMAIN
from .entity import BamBuddyPrinterEntityMixin

_LOGGER = logging.getLogger(__name__)


PRINTER_NUMBERS: list[NumberEntityDescription] = [
    NumberEntityDescription(
        key="nozzle_offset_x",
        name="Nozzle Offset X",
        icon="mdi:arrow-left-right",
        entity_category=EntityCategory.CONFIG,
        native_min_value=-5.0,
        native_max_value=5.0,
        native_step=0.1,
    ),
    NumberEntityDescription(
        key="nozzle_offset_y",
        name="Nozzle Offset Y",
        icon="mdi:arrow-up-down",
        entity_category=EntityCategory.CONFIG,
        native_min_value=-5.0,
        native_max_value=5.0,
        native_step=0.1,
    ),
    NumberEntityDescription(
        key="nozzle_offset_z",
        name="Nozzle Offset Z",
        icon="mdi:arrow-expand-vertical",
        entity_category=EntityCategory.CONFIG,
        native_min_value=-5.0,
        native_max_value=5.0,
        native_step=0.01,
    ),
    NumberEntityDescription(
        key="bed_offset_x",
        name="Bed Offset X",
        icon="mdi:arrow-left-right",
        entity_category=EntityCategory.CONFIG,
        native_min_value=-10.0,
        native_max_value=10.0,
        native_step=0.1,
    ),
    NumberEntityDescription(
        key="bed_offset_y",
        name="Bed Offset Y",
        icon="mdi:arrow-up-down",
        entity_category=EntityCategory.CONFIG,
        native_min_value=-10.0,
        native_max_value=10.0,
        native_step=0.1,
    ),
]


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up BamBuddy number entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    entities = []
    for printer_data in data["printers"].values():
        entities.extend(
            BamBuddyPrinterNumber(hass, entry, data["client"], printer_data, description)
            for description in PRINTER_NUMBERS
        )
    async_add_entities(entities)


class BamBuddyPrinterNumber(BamBuddyPrinterEntityMixin, CoordinatorEntity, NumberEntity):
    """BamBuddy printer number entity for offsets."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
        client: BamBuddyClient,
        printer_data: dict,
        description: NumberEntityDescription,
    ) -> None:
        super().__init__(printer_data["coordinator"])
        self.hass = hass
        self.entity_description = description
        self._entry = entry
        self._entry_id = entry.entry_id
        self._instance_url = f"http://{entry.data.get('host')}:{entry.data.get('port', 8000)}"
        self._client = client
        self._printer_data = printer_data
        self._attr_unique_id = f"{entry.entry_id}_p{printer_data['printer_id']}_{description.key}"

    @property
    def native_value(self) -> float | None:
        """Return current offset value."""
        data = self._coordinator_data()
        status = data.get("status", {})
        offsets = status.get("offsets", {})
        key = self.entity_description.key

        if key == "nozzle_offset_x":
            return offsets.get("nozzle_x")
        elif key == "nozzle_offset_y":
            return offsets.get("nozzle_y")
        elif key == "nozzle_offset_z":
            return offsets.get("nozzle_z")
        elif key == "bed_offset_x":
            return offsets.get("bed_x")
        elif key == "bed_offset_y":
            return offsets.get("bed_y")
        return None

    async def async_set_native_value(self, value: float) -> None:
        """Set the offset value."""
        printer_id = self._printer_data["printer_id"]
        key = self.entity_description.key

        try:
            if key == "nozzle_offset_x":
                await self._client.set_nozzle_offset(printer_id, x=value)
            elif key == "nozzle_offset_y":
                await self._client.set_nozzle_offset(printer_id, y=value)
            elif key == "nozzle_offset_z":
                await self._client.set_nozzle_offset(printer_id, z=value)
            elif key == "bed_offset_x":
                await self._client.set_bed_offset(printer_id, x=value)
            elif key == "bed_offset_y":
                await self._client.set_bed_offset(printer_id, y=value)

            await self.coordinator.async_request_refresh()
        except Exception as err:
            _LOGGER.error("Error setting offset %s: %s", key, err)
