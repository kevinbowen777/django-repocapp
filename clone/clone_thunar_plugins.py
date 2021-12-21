#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_thunar_plugins.py
# Purpose: Clones Xfce thunar-plugins repositories pulled from
#           https://gitlab.xfce.org/thunar-plugins
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.clone_xfce(component='thunar-plugins',
                    comp_list=cappdata.thunar_plugins_list())
