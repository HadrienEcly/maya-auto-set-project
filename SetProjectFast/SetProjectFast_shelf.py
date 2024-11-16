#Created by Hadrien Clement [https://github.com/HadrienEcly] Completely free to use !

import os
import maya.cmds as cmds

def find_valid_project(start_path, max_iterations=20): #CUSTOM MAX ITERATIONS HERE 
    validproject_path = start_path
    iteration_count = 0

    while validproject_path and iteration_count < max_iterations :
        workspace_file = os.path.join(validproject_path, "workspace.mel")
        if os.path.exists(workspace_file):
            return validproject_path
        parent_path = os.path.dirname(validproject_path)
        if parent_path == validproject_path:
            break
        validproject_path = parent_path
        iteration_count += 1
    return None

def set_project_to_valid():
    file_path = cmds.file(query=True, sceneName=True)
    
    if not file_path:
        print("The scene is not saved. Unable to set a project.")
        return
    start_path = os.path.dirname(file_path)

    project_path = find_valid_project(start_path)

    if project_path:
        cmds.workspace(project_path, openWorkspace=True)
        print(f"Workspace set to: {project_path}")
    else:
        cmds.confirmDialog(title="Error", message="No valid project found", button=["OK"], icon="critical")

set_project_to_valid()
