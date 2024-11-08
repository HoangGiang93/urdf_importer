# urdf_importer

URDF Importer is an add-on for [Blender](https://www.blender.org/). It supports for importing robots from URDF format from ROS Packages and provides FBX Exporter with textures for further usage.

## Features

- Import robot from URDF format from ROS environment to Blender (please source the package first)
- Auto generate meshes, armatures and bones based on the URDF
- Remove duplicated materials
- Export robot to .fbx format with textures

## Prerequisite

- [Blender >= 3.1.x](https://www.blender.org/download)
- [ROS or ROS2](https://www.ros.org/)

## Installation

1. Setup python enviroment

```console
cd <blender_path>/<version>/python/bin/ # For example cd blender-3.1.2-linux-x64/3.1/python/bin/
./python3.10 -m ensurepip
./python3.10 -m pip install --upgrade pip
./python3.10 -m pip install pyyaml
./python3.10 -m pip install rospkg
./python3.10 -m pip install urdf_parser_py
```

Windows: If Blender is installed to i.e. `C:\Program Files\`, run `cmd.exe` as administrator! Define ROS_ROOT as system environment variable pointing to a folder containing your ROS packages.

2. Install add-on

- Compress the folder `urdf_importer_addon` into a ZIP file named `urdf_importer_addon.zip`.
- Open a terminal, source the ROS workspace that contains the URDF model, and then start Blender by running `blender` in the terminal.
- In Blender, go to the `Edit` menu and select `Preferences`.
- Click on `Install`.
- Navigate to and select the `urdf_importer_addon.zip` file, then click `Install Add-on`.
- Enable the add-on by checking the box next to `Import-Export: Import URDF Format`.
- Verify the installation by opening `File` → `Import`. You should see `URDF (.urdf)` listed in the menu.

https://user-images.githubusercontent.com/64316740/160031703-74b12638-89e8-4aed-a1c0-4ce39fa56783.mp4


## Quickstart

### Import a standard [PR2](http://wiki.ros.org/Robots/PR2) from ROS

https://user-images.githubusercontent.com/64316740/160031686-0263fd5f-013a-47c1-b760-d4723a0d95a3.mp4

### Export as .fbx format with textures for e.g. Unreal Engine

https://user-images.githubusercontent.com/64316740/160304519-1879882c-9229-4db5-8234-aac34a32c896.mp4
