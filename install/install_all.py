#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_all.py
# Purpose: install oll of the local Xfce repositories pulled from
#           https://gitlab.xfce.org/
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import subprocess

os.chdir(os.path.dirname(os.path.realpath(__file__)))

subprocess.call("install_apps.py", shell=True)
subprocess.call("install_bindings.py", shell=True)
subprocess.call("install_core.py", shell=True)
subprocess.call("install_panel_plugins.py", shell=True)
subprocess.call("install_thunar_plugins.py", shell=True)