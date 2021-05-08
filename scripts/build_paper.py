#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Python standard library
import pathlib
import shutil
import subprocess

# External packages
import jinja2

# Internal modules
import ltxjnj


def main():

    file_name_latex_template = "template.tex"
    file_name_rendered_template = "template_rendered.tex"

    dir_templates = "templates"
    dir_build = "build"

    file_path_project_root = pathlib.Path("__file__").absolute().parents[1]
    file_path_dir_templates = file_path_project_root / dir_templates
    file_path_dir_build = file_path_project_root / dir_build
    file_path_rendered_template = file_path_dir_build / file_name_rendered_template

    assert file_path_dir_templates.exists()

    latex_jinja_env = ltxjnj.get_jinja_environment_for_latex(
        searchpath=file_path_dir_templates,
    )

    template = latex_jinja_env.get_template(file_name_latex_template)

    # template_rendered = template.render(author_1="Author 1", author_2="Author 1")
    template_rendered = template.render()
    # print(template_rendered)

    if file_path_dir_build.exists():
        shutil.rmtree(file_path_dir_build)

    # shutil.copytree(src, dest)
    shutil.copytree(file_path_dir_templates, file_path_dir_build)

    print(f"file_path_rendered_template: {file_path_rendered_template}")

    with open(file_path_rendered_template, "w") as f:
        f.write(template_rendered)

    assert file_path_rendered_template.exists()

    # Commands

    # build pdf
    cmd_cd = f"cd {str(file_path_dir_build)}"
    cmd_pdflatex = f"pdflatex {str(file_path_rendered_template)}"
    cmd_pdflatex = cmd_cd + " && " + cmd_pdflatex
    print(f"Executing:\n$ {cmd_pdflatex}\n...")
    subprocess.run(cmd_pdflatex, shell=True)

    # open pdf
    file_path_rendered_pdf = file_path_rendered_template.with_suffix(".pdf")

    assert file_path_rendered_pdf.exists()

    cmd_open_pdf = f"open {str(file_path_rendered_pdf)}"
    print(f"Executing:\n$ {cmd_open_pdf}\n...")
    subprocess.run(cmd_open_pdf, shell=True)


if __name__ == "__main__":
    main()
