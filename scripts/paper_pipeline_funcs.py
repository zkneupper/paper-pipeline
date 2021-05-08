#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Python standard library
import pathlib
import subprocess

# External packages
import jinja2


def get_jinja_environment_for_latex(searchpath=None):
    """
    Example:
    >>> template_dir = "templates"
    >>> file_name_latex_template = "template.tex"
    >>>
    >>> latex_jinja_env = get_jinja_environment_for_latex(template_dir)
    >>> template = latex_jinja_env.get_template(file_name_latex_template)
    """

    latex_jinja_env = jinja2.Environment(
        block_start_string="\BLOCK{",
        block_end_string="}",
        variable_start_string="\VAR{",
        variable_end_string="}",
        comment_start_string="\#{",
        comment_end_string="}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(searchpath),
    )

    return latex_jinja_env


def compile_latex_to_pdf(file_path_tex, verbose=False):
    pass
    """Builds pdf from latex file using `pdflatex` command."""
    file_path_tex_parent_dir = file_path_tex.parent
    cmd_cd = f"cd {str(file_path_tex_parent_dir)}"
    cmd_pdflatex = f"pdflatex {str(file_path_tex)}"
    cmd_pdflatex = cmd_cd + " && " + cmd_pdflatex

    if verbose:
        print(f"Executing:\n$ {cmd_pdflatex}\n...")

    subprocess.run(cmd_pdflatex, shell=True)


def open_pdf(file_path_pdf, verbose=False):
    """Opens pdf in default pdf viewer application."""
    cmd_open_pdf = f"open {str(file_path_pdf)}"

    if verbose:
        print(f"Executing:\n$ {cmd_open_pdf}\n...")

    subprocess.run(cmd_open_pdf, shell=True)
