#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_bindings.py
# Purpose: Install Xfce bindings into system
#
# version: 0.1
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')
from repo_arrays import xfce_bindings_list


os.chdir('../bindings')

for item in xfce_bindings_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
