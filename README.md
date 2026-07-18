<p align="center">
  <img src="src/assets/banner.png" alt="AndroidRunner Banner" width="100%">
</p>


# AndroidRunner 🚀

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Release](https://img.shields.io/github/v/release/Yashrajsinh-jadeja420/AndroidRunner)

</p>


A lightweight command-line Android development assistant.

AndroidRunner helps developers build, install, launch, and manage Android applications directly from the terminal.

It provides a simple CLI workflow using:

- Gradle
- Android SDK tools
- ADB
- Python automation


---

# 🎬 Demo


<p align="center">
  <video src="[src/assets/AndroidRunnerTrailer.mp4](https://github.com/user-attachments/assets/abc1cd79-0328-4980-9c60-2d554cd919ab)" width="850" controls>
    Your browser does not support the video tag.
  </video>
</p>


---

# ✨ Features


## 🔨 Build & Project Management

✅ Detect Android projects  
✅ Detect Gradle wrapper  
✅ Build Android APKs  
✅ Clean build support  
✅ Release APK workflow  


## 📱 Device Management

✅ Install APKs to connected devices  
✅ Launch Android applications  
✅ Device detection  
✅ Emulator management  


## 🩺 Environment Diagnostics

✅ Java detection  
✅ Android SDK detection  
✅ Build Tools detection  
✅ ADB verification  


## 🛠 Developer Utilities

✅ Logcat viewer  
✅ Screenshot capture  
✅ Screen recording  
✅ Automated workflows  


---

# 📦 Installation


## Clone Repository

```bash
git clone https://github.com/Yashrajsinh-jadeja420/AndroidRunner.git

cd AndroidRunner
```


---

# 🐍 Python Setup


Create virtual environment:

```powershell
python -m venv .venv
```


Activate environment:


### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```


### Windows CMD

```cmd
.venv\Scripts\activate.bat
```


### Linux/macOS

```bash
source .venv/bin/activate
```


---

# Install AndroidRunner

Install in development mode:

```powershell
pip install -e .
```


---

# 🚀 Usage


## Check Environment

```powershell
adr doctor
```

Checks:

```
✓ Java
✓ Android SDK
✓ Build Tools
✓ ADB
✓ Connected Devices
```


---

## Detect Android Project

```powershell
adr detect
```

Detects:

```
✓ Gradle wrapper
✓ Android modules
✓ Project structure
✓ APK locations
```


---

## Build APK

```powershell
adr build
```

Builds Android application using Gradle.


---

## Install APK

```powershell
adr install
```

Installs generated APK using ADB.


---

## Launch Application

```powershell
adr launch
```

Launches installed Android application.


---

## View Logs

```powershell
adr logs
```

Starts Android Logcat monitoring.


---

## Device Management

```powershell
adr devices
```

Shows connected Android devices.


---

## Emulator Management

```powershell
adr emulator
```

Manages Android emulators.


---

# ⚡ Complete Workflow


```powershell
adr run
```


Runs:

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

# 🛠 Requirements


Required software:


- Python 3.10+
- Java JDK 17+
- Android SDK
- Android Build Tools
- Android Platform Tools (ADB)


---

# 💻 Platform Support


Currently tested:


✅ Windows


More platforms planned.


---

# 📁 Project Structure


```
AndroidRunner/
│
├── src/
│   ├── androidrunner/
│   │
│   ├── assets/
│   │   ├── banner.png
│   │   └── AndroidRunnerTrailer.mp4
│
├── README.md
├── CHANGELOG.md
├── LICENSE
└── pyproject.toml
```


---

# 🤝 Contributing


Contributions, bug reports, and suggestions are welcome.


Feel free to open an issue or submit a pull request.


---

# 📄 Changelog


See:

[CHANGELOG.md](CHANGELOG.md)


---

# 📜 License


This project is licensed under the MIT License.
