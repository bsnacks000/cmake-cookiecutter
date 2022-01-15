#!/usr/bin/env python
import os
import shutil
import subprocess
import pathlib


import re 


if __name__ == '__main__':
    project_dirpath = pathlib.Path(os.path.realpath(os.path.curdir))

    dirs = ["src", "include", "app"]  # exclude tests... always in cpp
    
    # remove either C or C++ files depending on language option
    langs = {'c': ['cpp', 'hpp'], 'cpp': ['c', 'h']}
    lang, h = langs['{{ cookiecutter.language }}'.lower()]
    
    for d in dirs:
        for f in (project_dirpath / d).rglob(f"*.{lang}"):
            os.remove(f)
        for f in (project_dirpath / d).rglob(f"*.{h}"):
            os.remove(f)


    # maybe remove library 
    if '{{ cookiecutter.create_library }}'.lower() != 'y': 
        shutil.rmtree(project_dirpath / "src")

    if '{{ cookiecutter.create_library }}'.lower() == 'y' and '{{ cookiecutter.header_only }}'.lower() == 'y': 
        shutil.rmtree(project_dirpath / "src")

    if '{{ cookiecutter.add_gtest }}'.lower() != 'y': 
        shutil.rmtree(project_dirpath / "tests")

    if '{{ cookiecutter.create_application }}'.lower() != 'y': 
        shutil.rmtree(project_dirpath / "app")

    if '{{ cookiecutter.git_init}}'.lower() == 'y': 
        os.chdir(project_dirpath)
        os.system('git init')