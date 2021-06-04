import os

dir_name = "my_project"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    midFolders = ['settings', 'mainapp', 'adminapp', 'authapp']
    for midFolders in midFolders:
        os.makedirs(os.path.join(dir_name, midFolders))