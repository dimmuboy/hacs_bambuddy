<p align="center">
  <img src="https://raw.githubusercontent.com/Spegeli/hacs_bambuddy/main/logo.png" alt="BamBuddy Logo" width="300">
</p>

# 🚀 BamBuddy – Home Assistant Integration

<p align="center">
  <a href="https://github.com/hacs/integration"><img src="https://img.shields.io/badge/HACS-Custom-orange.svg"></a>
  <a href="https://github.com/NMC214F/hacs_bambuddy/releases"><img src="https://img.shields.io/github/v/release/NMC214F/hacs_bambuddy?label=release&color=blue"></a>
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
</p>

<p align="center">
  A custom <a href="https://www.home-assistant.io/">Home Assistant</a> integration for <a href="https://github.com/maziggy/bambuddy">BamBuddy</a> — a self-hosted command center for Bambu Lab.<br>
  <strong>Your printers. No cloud. Your rules.</strong>
</p>

> [!WARNING]
> **This integration is currently under active development and is not intended for production use.**
> Expect breaking changes, incomplete features, and potential instability. Use at your own risk.

---

## ✨ Features

- **Multiple printers** — manage any number of printers from one BamBuddy instance
- **Live status** — print progress, layer count, remaining time, current job name
- **Temperature sensors** — nozzle, bed (and chamber where available), including target temperatures
- **Fan speeds** — cooling, auxiliary, chamber, and heatbreak fans
- **Camera** — live MJPEG stream and snapshot from the printer camera
- **Cover image** — current print job cover image, auto-refreshing on new jobs
- **Print controls** — pause, resume, and stop the current print job
- **Print speed** — select between Silent, Standard, Sport, and Ludicrous modes
- **Lighting controls** — toggle chamber light, work light, and LED light
- **Calibration & Leveling** — start nozzle calibration and auto bed leveling
- **Offset adjustments** — fine-tune nozzle and bed offsets with number sliders
- **Diagnostic entities** — firmware version, IP address, Wi-Fi signal, wired network, developer mode, HMS error status

---

## 📋 Requirements

- Home Assistant **2025.1** or newer
- A running [BamBuddy](https://github.com/maziggy/bambuddy) instance reachable from your HA server
- A BamBuddy API key

---

## 📦 Installation

### Via HACS (recommended)

Click the button below to automatically add the repository to HACS:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect?repository_url=https://github.com/NMC214F/hacs_bambuddy)

Or add it manually:

1. Open HACS in Home Assistant
2. Go to **Integrations** → click the three-dot menu → **Custom repositories**
3. Add `https://github.com/NMC214F/hacs_bambuddy` with category **Integration**
4. Search for **BamBuddy** and install it
5. Restart Home Assistant

### Manual

1. Copy the `custom_components/bambuddy` folder into your HA `custom_components` directory
2. Restart Home Assistant

---

## ⚙️ Configuration

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for **BamBuddy**
3. Enter your BamBuddy host, port (default: `8000`), and API key
4. After setup, click the **Configure** button (wrench icon) on the integration card to add your printers

### Adding & removing printers

Open the integration options (wrench icon) and select **Add Printer**. BamBuddy will list all available printers — select one to create a device in Home Assistant.

Printers can be removed either via the options menu or by deleting the device directly from the device page.

---

## 📊 Entities

### Per printer

#### Status & Monitoring
| Entity | Type | Description |
|---|---|---|
| Status | Sensor | Current printer state |
| Progress | Sensor | Print progress in % |
| Remaining Time | Sensor | Estimated time remaining |
| Current Layer / Total Layers | Sensor | Layer progress |
| Current Print | Sensor | Active print job name |
| Online | Binary Sensor | Printer connectivity |

#### Temperature Sensors
| Entity | Type | Description |
|---|---|---|
| Nozzle Temperature | Sensor | Current nozzle temp |
| Nozzle Target Temperature | Sensor | Target nozzle temp |
| Bed Temperature | Sensor | Current bed temp |
| Bed Target Temperature | Sensor | Target bed temp |
| Chamber Temperature | Sensor | Chamber temp (where available) |

#### Fan Control
| Entity | Type | Description |
|---|---|---|
| Cooling / Aux / Chamber / Heatbreak Fan | Sensor | Fan speeds in % |

#### Print Control
| Entity | Type | Description |
|---|---|---|
| Pause / Resume / Stop Print | Button | Print job controls |
| Print Speed | Select | Silent / Standard / Sport / Ludicrous |

#### Lighting Control
| Entity | Type | Description |
|---|---|---|
| Chamber Light | Switch | Toggle chamber light on/off |
| Work Light | Switch | Toggle work light on/off |
| LED Light | Switch | Toggle LED light on/off |

#### Calibration & Leveling
| Entity | Type | Description |
|---|---|---|
| Start Nozzle Calibration | Button | Start nozzle calibration procedure |
| Start Auto Bed Leveling | Button | Start automatic bed leveling |

#### Offset Adjustments
| Entity | Type | Description |
|---|---|---|
| Nozzle Offset X | Number | Nozzle X offset (-5.0 to 5.0 mm) |
| Nozzle Offset Y | Number | Nozzle Y offset (-5.0 to 5.0 mm) |
| Nozzle Offset Z | Number | Nozzle Z offset (-5.0 to 5.0 mm) |
| Bed Offset X | Number | Bed X offset (-10.0 to 10.0 mm) |
| Bed Offset Y | Number | Bed Y offset (-10.0 to 10.0 mm) |

#### Media
| Entity | Type | Description |
|---|---|---|
| Camera | Camera | Live MJPEG stream + snapshot |
| Cover | Image | Current print job cover image |

#### Maintenance
| Entity | Type | Description |
|---|---|---|
| Clear Plate | Button | Clear the build plate |
| Refresh Status | Button | Force a status update |

#### Diagnostics
| Entity | Type | Description |
|---|---|---|
| HMS Status | Sensor | HMS error information |
| Clear HMS Errors | Button | Clear HMS errors |
| SD Card | Binary Sensor | SD card presence |
| HMS Errors | Binary Sensor | Active HMS errors |
| Firmware Version | Sensor | *(Diagnostic)* |
| IP Address | Sensor | *(Diagnostic)* |
| Wi-Fi Signal | Sensor | *(Diagnostic)* |
| Wired Network | Binary Sensor | *(Diagnostic)* |
| Developer Mode | Binary Sensor | *(Diagnostic)* |

### BamBuddy instance

| Entity | Type | Description |
|---|---|---|
| Version | Sensor | BamBuddy app version |
| Health Status | Sensor | Instance health |
| Uptime | Sensor | Instance uptime in hours |
| Printers Total / Connected | Sensor | Printer counts |
| Total / Successful / Failed Prints | Sensor | Print statistics |
| Total Print Time | Sensor | Cumulative print hours |
| Total Filament Used | Sensor | Cumulative filament in grams |
| Archive Count | Sensor | Stored archives |
| Disk Free / Disk Used | Sensor | Storage info |

---

## 🔄 Update Interval

Status is polled every **10 seconds**.

---

## 🎯 Extended Controls (New)

This fork adds enhanced control capabilities to the original BamBuddy integration:

### 🔦 Lighting
- **Chamber Light** — Toggle printer chamber illumination
- **Work Light** — Toggle work area lighting
- **LED Light** — Toggle LED lighting

### 🔧 Calibration & Maintenance
- **Nozzle Calibration** — Start automatic nozzle calibration procedure
- **Auto Bed Leveling** — Initiate automatic bed leveling sequence

### 📏 Fine-Tuning Offsets
Adjust printer offsets with precise sliders:
- **Nozzle Offset (X, Y, Z)** — Fine-tune nozzle position
- **Bed Offset (X, Y)** — Adjust bed position

---

## ⚖️ Disclaimer

This is **not** an official release by the BamBuddy developer. This project provides a custom Home Assistant integration that connects to [BamBuddy](https://github.com/maziggy/bambuddy) via its REST API.

I am not affiliated with or the developer of BamBuddy itself — therefore I am unable to provide support for BamBuddy-related issues, bugs, or feature requests. For anything related to BamBuddy, please see:

👉 **[github.com/maziggy/bambuddy](https://github.com/maziggy/bambuddy)**

Support provided here is limited to the **Home Assistant integration** only.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
