#Created by Hadrien Clement [https://github.com/HadrienEcly] Completely free to use !

import os
import maya.cmds as cmds

##FUNCTIONS

def find_valid_project(start_path, max_iterations=20): #CUSTOM MAX ITERATIONS HERE
    
    
# Function that searches for the location of workspace.mel to find a valid project
    
    validproject_path = start_path
    iteration_count = 0

    while validproject_path and iteration_count < max_iterations : #prevent infinite loop
        workspace_file = os.path.join(validproject_path, "workspace.mel")
        #.mel in this file ?
        if os.path.exists(workspace_file):
            return validproject_path #yes
        # no, go up one level
        parent_path = os.path.dirname(validproject_path)
        if parent_path == validproject_path:
            break
        validproject_path = parent_path
        
        #increment iteraction count
        iteration_count += 1

    return None

def set_project_to_valid():
    # get actual scene file name
    file_path = cmds.file(query=True, sceneName=True)
    
    if not file_path:
        print("The scene is not saved. Unable to set a project.")
        return

    # Get the folder where is located the scene
    start_path = os.path.dirname(file_path)

    # Find a valid maya project
    project_path = find_valid_project(start_path)

    if project_path:
        # Set project on a valid path
        cmds.workspace(project_path, openWorkspace=True)
        print(f"Workspace set to: {project_path}")
    else:
        cmds.confirmDialog(title="Error", message="No valid project found", button=["OK"], icon="critical")

# MAIN SCRIPT

set_project_to_valid()