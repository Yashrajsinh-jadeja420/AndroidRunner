<p align="center">
  <img src="src/assets/banner.png" alt="AndroidRunner Banner" width="100%">
</p>


<h1 align="center">
  AndroidRunner 🚀
</h1>


<p align="center">
  Lightweight Android development workflow automation from your terminal.
</p>


<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Release](https://img.shields.io/github/v/release/Yashrajsinh-jadeja420/AndroidRunner)

</p>


---

# 🎬 Demo

Experience Android development automation with AndroidRunner:

https://github.com/user-attachments/assets/abc1cd79-0328-4980-9c60-2d554cd919ab


---

# 📖 About

AndroidRunner is a lightweight command-line Android development assistant.

It provides a unified CLI workflow for common Android development tasks:

- Building APKs
- Installing applications
- Launching apps
- Managing devices
- Debugging with ADB
- Checking Android development environments


Built using:

- Python
- Gradle
- Android SDK
- ADB


---

# ✨ Features


## 🔨 Build Automation

- ✅ Android project detection
- ✅ Gradle wrapper detection
- ✅ APK building
- ✅ Clean builds
- ✅ Release workflow


## 📱 Device Management

- ✅ Connected device detection
- ✅ APK installation
- ✅ Application launching
- ✅ Emulator management


## 🩺 Environment Diagnostics

- ✅ Java detection
- ✅ Android SDK detection
- ✅ Build Tools verification
- ✅ ADB health checks


## 🛠 Developer Utilities

- ✅ Logcat viewer
- ✅ Log filtering
- ✅ Log saving
- ✅ Screenshot support
- ✅ Screen recording


---

# 🚀 Installation


## Requirements

Before installing AndroidRunner, make sure you have:

- Windows 10/11
- Python 3.10+
- Java JDK 17+
- Android SDK
- Android Build Tools
- Android Platform Tools (ADB)


---

## Clone Repository

```bash
git clone https://github.com/Yashrajsinh-jadeja420/AndroidRunner.git

cd AndroidRunner
```


---

## Create Virtual Environment

```powershell
python -m venv .venv
```


Activate:

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```


### Command Prompt

```cmd
.venv\Scripts\activate.bat
```


---

## Install AndroidRunner

```powershell
pip install -e .
```


After installation verify:

```powershell
adr --help
```


---

# ⚡ Quick Start


Check Android environment:

```powershell
adr doctor
```


Example:

```
✓ Java detected
✓ Android SDK detected
✓ Build Tools detected
✓ ADB connected
```


---

# 📱 Commands


## Device Manager

```powershell
adr devices
```


## Build APK

```powershell
adr build
```


## Install APK

```powershell
adr install
```


## Launch App

```powershell
adr launch
```


## Logs

```powershell
adr logs
```


## Emulator

```powershell
adr emulator
```


## Complete Workflow

```powershell
adr run
```


Workflow:

```
Build APK
     ↓
Install APK
     ↓
Launch Application
```


Example:

```
$ adr run


AndroidRunner Run


[1/3] Building APK

BUILD SUCCESSFUL


[2/3] Installing APK

APK Installed Successfully


[3/3] Launching Application

Application started successfully.
```


---

# 💻 Platform Support


Currently supported and tested:

✅ Windows


---

# 📁 Project Structure


```
AndroidRunner/
│
├── src/
│   └── androidrunner/
│       ├── commands/
│       ├── core/
│       ├── android/
│       └── utils/
│
├── src/assets/
│   ├── banner.png
│   └── AndroidRunnerTrailer.mp4
│
├── README.md
├── CHANGELOG.md
├── LICENSE
└── pyproject.toml
```


---

# 🤝 Contributing


Contributions, bug reports, and feature requests are welcome.

Feel free to open an issue or submit a pull request.


---

# 📄 Changelog

See:

[CHANGELOG.md](CHANGELOG.md)


---

# 📜 License


Licensed under the MIT License.
