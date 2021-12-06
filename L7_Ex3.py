# |--my_project_2
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

import os
import shutil


folders = ['settings', 'mainapp', 'authapp']
for el in folders:
    dir_path = os.path.join('my_project_2', el)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

path_1 = '.\my_project_2\settings'
setting_files = ['__init__.py', 'dev.py', 'prod.py']
for n, sfile in enumerate(setting_files):
    filepath_1 = os.path.join(path_1, sfile)
    with open(filepath_1, "x") as s:
        pass

path_2 = '.\my_project_2\mainapp'
mainapp_files = ['__init__.py', 'models.py', 'views.py']
for n, mfile in enumerate(mainapp_files):
    filepath_2 = os.path.join(path_2, mfile)
    with open(filepath_2, "x") as mf:
        pass
os.mkdir(os.path.join(path_2, 'templates'))
os.mkdir(os.path.join('.\my_project_2\mainapp\\templates', 'mainapp'))
mainapp_files_2 = ['base.html', 'index.html']
for n, mafile in enumerate(mainapp_files_2):
    filepath_3 = os.path.join('.\my_project_2\mainapp\\templates\mainapp', mafile)
    with open(filepath_3, "x") as maf:
        pass

path_4 = '.\my_project_2\\authapp'
authapp_files = ['__init__.py', 'models.py', 'views.py']
for n, afile in enumerate(authapp_files):
    filepath_4 = os.path.join(path_4, afile)
    with open(filepath_4, "x") as mf:
        pass
os.mkdir(os.path.join(path_4, 'templates'))
os.mkdir(os.path.join('.\my_project_2\\authapp\\templates', 'authapp'))
authapp_files_2 = ['base.html', 'index.html']
for n, atfile in enumerate(authapp_files_2):
    filepath_5 = os.path.join('.\my_project_2\\authapp\\templates\\authapp', atfile)
    with open(filepath_5, "x") as atf:
        pass



root_dir = '.\my_project_2'
new_path = os.path.join('my_project_2', 'templates')
for root, dirs, files in os.walk(root_dir):
    for dir in dirs:
        if dir == 'templates':
            source = os.path.join(root, dir)
            if not os.path.exists(new_path):
                shutil.copytree(source, new_path, symlinks=False, ignore=None)
            else:
                for rt, drs, fls in os.walk(source):
                    for dr in drs:
                        newest_path = os.path.join(new_path, dr)
                        inner_source = os.path.join(rt, dr)
                        shutil.copytree(inner_source, newest_path, symlinks=False, ignore=None)


