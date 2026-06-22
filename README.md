# Digital Twin for QoE Monitoring in Edge Devices

## Overview

This repository presents a Digital Twin-based prototype for real-time monitoring and Quality of Experience (QoE) assessment in Edge Computing environments.

The system collects telemetry from an Edge/IoT device, processes the monitored variables, estimates a QoE score, and displays the current Digital Twin state through a Streamlit dashboard.

## Main Features

- Serial telemetry collection from ESP32/Raspberry Pi environments.
- Simulation mode for testing without hardware.
- QoE score calculation from network and device metrics.
- Digital Twin state classification.
- Interactive dashboard with network, device and QoE views.
- Modular structure for research and GitHub publication.

## Architecture

```text
Physical Device / ESP32
        |
        v
Serial Collector
        |
        v
Telemetry Storage (CSV)
        |
        v
QoE Engine + Digital Twin Core
        |
        v
Streamlit Dashboard
```

## Repository Structure

```text
digital-twin-qoe-edge/
|
├── README.md
├── requirements.txt
├── .gitignore
|
├── src/
│   ├── backend/
│   │   ├── serial_collector.py
│   │   └── data_service.py
│   │
│   ├── core/
│   │   ├── digital_twin.py
│   │   ├── qoe_engine.py
│   │   └── metrics.py
│   │
│   ├── frontend/
│   │   ├── app.py
│   │   └── components/
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
|
├── docs/
├── assets/
└── tests/
```

## Monitored Metrics

| Category | Metric | Description |
|---|---|---|
| Network | RSSI | Signal strength in dBm |
| Device | Heap | Available memory from the device |
| Device | Uptime | Device operating time |
| Energy | Voltage | Voltage reading from the device |
| Energy | Current | Current raw reading |
| Energy | Power | Power raw reading |

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USER/digital-twin-qoe-edge.git
cd digital-twin-qoe-edge
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Dashboard Without Raspberry Pi

The dashboard works in simulation mode when no CSV telemetry file exists.

```bash
streamlit run src/frontend/app.py
```

or:

```bash
python -m streamlit run src/frontend/app.py
```

## Running the Serial Collector

Use this only when the device is connected by serial port.

```bash
python -m src.backend.serial_collector
```

Default serial configuration is defined in:

```text
src/config/settings.py
```

## Research Context

This prototype is part of an experimental study on Digital Twins, Edge Computing and QoE monitoring for intelligent network-aware applications.

## Citation

```bibtex
@misc{machado2026digitaltwinqoe,
  title={Digital Twin for QoE Monitoring in Edge Devices},
  author={Machado da Silva, Joao Victor Neves},
  year={2026}
}
```

## Author

João Victor Neves Machado da Silva  
Federal University of Amazonas (UFAM)  
Mob4AI Research Group
