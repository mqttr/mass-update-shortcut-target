import winshell as ws
import os
import glob

def main(rootPath, remove, replace):
    mainPath = "D:\\Games\\"
    links = get_all_links_in(mainPath)

    for link in links:
        with ws.shortcut(os.path.join(mainPath, link)) as shortcut:
            newTarget = get_new_target(shortcut.path, remove, replace)

            shortcut.path = newTarget
            shortcut.icon = newTarget, 0
            shortcut.working_directory = get_new_working_directory(newTarget)

            shortcut.description = ""

def get_all_links_in(directory):
    return glob.glob(directory + "*.lnk")

def get_new_target(oldTarget, remove, replace):
    sTarget = oldTarget.split("\\")

    for i, dir in enumerate(sTarget):
        if dir == remove:
            sTarget[i] = replace

    return '\\'.join(sTarget)

def get_new_working_directory(newTarget):
    sTarget = newTarget.split('\\')
    sTarget.pop()

    return '\\'.join(sTarget)

if __name__ == "__main__":
    
    rootPath = "D:\\My Games\\"
    remove = "My Games"
    replace = "Games"

    main(rootPath, remove, replace)