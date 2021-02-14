#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_thunar_plugins.py
# Purpose: Install Xfce4 thunar-plugins into system
#
# version: 0.2
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import repo_arrays
from repodir import repodir

os.chdir(repodir('thunar-plugins'))

for item in repo_arrays.xfce_thunar_plugins_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
