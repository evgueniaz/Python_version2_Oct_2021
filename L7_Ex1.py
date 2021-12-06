# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os

folders = ['settings', 'mainapp', 'adminapp', 'authapp']
for el in folders:
    dir_path = os.path.join('my_project', el)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
