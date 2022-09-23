#!/usr/bin/env python3

"""
Name: clone_django.py
Purpose: Clones Django repositories pulled from
           https://gitlab.com/kevinbowen/

source: https://gitlab.com/kevinbowen/django-repocapp
version: 0.1.0
updated: 20220922
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import subprocess
import sys

from cappdata import component_list

parser = argparse.ArgumentParser(
    description="clone groups of Django components"
    " from https://github.com/kevinbowen777 repositories."
)
parser.add_argument(
    "-c",
    "--component",
    action="store",
    choices=[
        "apps",
        "all_components",
    ],
    help="specify an Django component group to clone"
    " from https://github.com/kevinbowen777/",
)
parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
args = parser.parse_args()
if args.component is None:
    print(
        "No component was specified. Default to cloning"
        " the 'apps' components...."
    )
    args.component = "apps"


def clone_xfce(component, comp_list):
    """Run 'git clone' for selected components."""
    # print(f"Cloning the Django {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        # grandparent directory (../../) relative to script.
        installpath = os.path.abspath(
            os.path.join(os.getcwd(), os.pardir, os.pardir)
            # os.path.join(os.getcwd(), os.pardir, os.pardir, comp_group)
        )

        return installpath

    repopath = get_path(component)
    success_count = 0

    os.makedirs(repopath, exist_ok=True)
    os.chdir(repopath)

    for item in component_list(comp_list):
        if os.path.isdir(item):
            print(f"\nThe '{item}' directory already exists. Skipping...\n")
            print("\u2248" * 16)
        else:
            try:
                url = f"https://github.com/kevinbowen777/{item}.git"
                # url = f"https://gitlab.xfce.org/{component}/{item}.git"
                subprocess.run(["git", "clone", url], stdout=None, check=True)
                success_count += 1
                print("\u2248" * 16)
                print(f"{item} repository cloned successfully.")
            except subprocess.CalledProcessError:
                # On error, returns a non-zero exit status 128.
                print("\u2248" * 16)
                print(f"Failed to clone {item} repository.")

            print(
                f"{success_count}/{len(component_list(comp_list))} "
                f"'{component}' repositories cloned successfully."
            )
            print("\u2248" * 16)


def main(component_group_name):
    """Build arguments to pass to clone_django() with a call to
    cappdata for component name list.
    command format:
            clone_django(component='apps',
                       comp_list='apps')
    """
    cgroup_listname = component_list(component_group_name)
    # All cgroup_listnames will return a string, except 'all'
    if isinstance(cgroup_listname, dict):
        for comp, cglist in cgroup_listname.items():
            clone_xfce(component=comp, comp_list=cglist)
    else:
        clone_xfce(
            component=component_group_name, comp_list=component_group_name
        )


if __name__ == "__main__":
    try:
        component_group = args.component
        main(component_group)
    except KeyboardInterrupt:
        print()
        print("Stopped django-repocapp. Exiting...")
        sys.exit()
