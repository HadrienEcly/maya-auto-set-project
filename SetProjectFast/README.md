# Maya Auto/Fast Set Project

**A Python script for Autodesk Maya to automatically set the project based on the current scene.**

## Features
- Automatically finds the correct project folder for your current scene.
- Traverses directories to locate a valid `workspace.mel` file. (Up to 20 iterations by default; customizable by changing the `max_iterations=20` parameter in the `find_valid_project` function.)
- Displays a discreet message in the **Script Editor** on success.
- Shows an error dialog in the UI if no valid project is found.
- Works seamlessly with different project structures.
- Provides **three installation options** for different use cases.

---

## Installation Options

### 1) **Shelf Integration**
Use this option to quickly access the script with a custom shelf button.

#### Installation:
1. Copy the content of `SetProjectFast.py` into Maya's Script Editor (Python tab).
2. Highlight the code and drag it to a shelf to create a custom shelf button.

---

### 2) **Script Installation**
Install the script as a module and call it directly from the Script Editor or other scripts.

#### Installation:
1. Clone or download the repository.
2. Place the `FastSetProject` folder in your Maya scripts directory:
   - **Windows**: `C:/Users/<YourUsername>/Documents/maya/scripts`
   - **macOS**: `~/Library/Preferences/Autodesk/maya/scripts`
   - **Linux**: `~/maya/scripts`
3. Restart Maya.

#### Usage:
Run the following code in Maya's Script Editor (Python tab):


import FastSetProject.SetProjectFast_script as sp
sp.set_project_to_valid()
