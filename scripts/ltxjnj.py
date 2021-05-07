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

    searchpath = pathlib.Path(searchpath).absolute()
    assert searchpath.exists(), f"searchpath `{searchpath}` does not exist."

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
