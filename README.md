
<p align="center">
  <img src="assets/banner.png" alt="AndroidRunner Banner" width="100%">
</p>


# AndroidRunner 🚀

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A command-line Android development assistant.

AndroidRunner helps developers build, install, launch, and manage Android applications directly from the terminal.

It provides a simple CLI interface for common Android development workflows using Gradle, Android SDK tools, and ADB.

---

## ✨ Features

### Build & Project Management

✅ Detect Android projects  
✅ Detect Gradle wrapper  
✅ Build Android APKs  
✅ Clean build support  
✅ Release APK workflow  

### Device Management

✅ Install APKs to connected devices  
✅ Launch Android applications  
✅ Device detection  
✅ Emulator management  

### Environment Diagnostics

✅ Java detection  
✅ Android SDK detection  
✅ Build Tools detection  
✅ ADB verification  

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Yashrajsinh-jadeja420/AndroidRunner.git

cd AndroidRunner
```

---

## 🐍 Setup Python Environment

Create virtual environment:

```powershell
python -m venv .venv
```

### Activate Environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

#### Linux/macOS

```bash
source .venv/bin/activate
```

---

## Install AndroidRunner

Install in development mode:

```powershell
pip install -e .
```

---

# 🚀 Usage

## Check Android Environment

```powershell
adr doctor
```

Checks:

- Java
- Android SDK
- Build Tools
- ADB
- Connected devices

---

## Detect Android Project

```powershell
adr detect
```

Detects:

- Gradle wrapper
- Android modules
- Project structure
- APK locations

---

## Build APK

```powershell
adr build
```

Builds the Android application using Gradle.

---

## Install APK

```powershell
adr install
```

Installs the generated APK using ADB.

---

## Launch Application

```powershell
adr launch
```

Launches the installed Android application.

---

## Complete Workflow

```powershell
adr run
```

Runs the complete workflow:

```
Build APK
    ↓
Install APK
    ↓
Launch Application
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
├── README.md
├── CHANGELOG.md
├── LICENSE
└── pyproject.toml
```

---

# 📸 Demo

Example:

```
$ adr run

AndroidRunner Run

1/3 Building APK

BUILD SUCCESSFUL


2/3 Installing APK

APK Installed Successfully


3/3 Launching App

Application started successfully.
```

---

# 🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

Feel free to open an issue or submit a pull request.

---

# 📄 Changelog

See [CHANGELOG.md](CHANGELOG.md)

---

# 📜 License

This project is licensed under the MIT License.
