#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Python standard library
import pathlib
import subprocess

# External packages
import jinja2

# Internal modules
import ltxjnj


def main():

    build_dir = "build"

    file_path_project_root = pathlib.Path("__file__").absolute().parents[1]

    file_path_build_dir = file_path_project_root / build_dir

    file_path_build_dir.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()

# """
# Example:
# >>> template_dir = "templates"
# >>> file_name_latex_template = "template.tex"
# >>>
# >>> latex_jinja_env = ltxjnj.get_jinja_environment_for_latex(searchpath=template_dir)
# >>> template = latex_jinja_env.get_template(file_name_latex_template)
# """
