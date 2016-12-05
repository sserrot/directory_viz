# !/usr/bin/python

import os

connections = {}
folders = ''
folpath = 'C:\\Users\\Santiago\\Documents'
exclude = ['.git', '.idea', '.settings', '__pycache__','.vscode']

for root, dirs, files in os.walk(folpath, topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in dirs:
        folders = folders + os.path.join(root, name) + ", "
    connections[folpath] = folders
print(connections)