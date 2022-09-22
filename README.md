[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.com/kevinbowen/django-repocapp/-/blob/master/LICENSE)

# django-repocapp

repocapp - repository (C)lone (A)utogen (P)ull (P)urge
              (This also includes clean & installation scripts)

A collection of scripts to maintain local Django repositories.

The purpose of the scripts contained in the `django-repocapp` repository is to
facilitate managing your local Django repositories in bulk.
Cloning, running automake, installing, purging and updating tasks are performed in groups

----
### List of scripts
#### Menu scripts
`repocapp.py` - provides a rudimentary menu-driven option to run the scripts.
  This is entirely optional. All of these scripts can be run independently.

----
#### Individual action scripts

 - `clone_django.py` - Clone Xfce repositories from https://gitlab.xfce.org
 - `build_django.py` - Run autogen & make against local component repositories

**N.B.: These scripts perform _ABSOLUTELY NO CHECKS_ for missing system libraries or the
order of component compilation. It is assumed that you know what you are
doing. Use at your own risk. No guarantees.**

 - `pull_django.py` - Update local component repositories with git pull
 - `purge_django.py` - Delete local component repositories by category
 - `install_django.py` - Install components locally or system-wide with `sudo make install`
 - `clean_django.py` - Clean local component directories (make clean)

#### Running individual scripts
Note: This section is currently deprecated
All of the *-django.py scripts take the argument `-c` and the name of the
component group to be acted upon. The following names are used:
 - apps
 - bindings
 - xfce
 - panel-plugins
 - thunar-plugins
 - www
 - all

For example:
 - `clone_django.py -c panel-plugins`
 - `purge_django.py -c all`

Running the script without an argument will, by default, act upon the `apps`
components. This is the equivalent of running, for example, `pull_xfce -c apps`.

----

### Installation of django-repocapp project

    Master: git clone https://gitlab.com/kevinbowen/django-repocapp.git
    Mirror: git clone https://github.com/kevinbowen777/django-repocapp.git



----
### Reporting Bugs

   Visit the [Issues page](https://gitlab.com/kevinbowen/xfce-repocapp/-/issues)
     to view currently open bug reports or open a new issue.
