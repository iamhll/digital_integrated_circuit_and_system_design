# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'digital_integrated_circuit_and_system_design'
copyright = '2023, llhuang'
author = 'llhuang'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

#--- BEGIN OF "COMMENTED BY HLL" ---
## The theme to use for HTML and HTML Help pages.  See the documentation for
## a list of builtin themes.
##
#html_theme = 'alabaster'
#
## Add any paths that contain custom static files (such as style sheets) here,
## relative to this directory. They are copied after the builtin static files,
## so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
#--- END   OF "COMMENTED BY HLL" ---

#--- BEGIN OF "ADDED BY HLL" ---
html_theme = 'classic'
html_theme_options = {
    "stickysidebar"     : "true",
    "sidebarwidth"      : "280",
    "collapsiblesidebar": "false",
    "body_min_width"    : 0,
    "body_max_width"    : "none",
    "footerbgcolor"     : "#426d96",
    "footertextcolor"   : "#ffffff",
    "sidebarbgcolor"    : "#527da6",
    "sidebarbtncolor"   : "#ffffff",
    "sidebartextcolor"  : "#ffffff",
    "sidebarlinkcolor"  : "#ffffff",
    "relbarbgcolor"     : "#426d96",
    "relbartextcolor"   : "#ffffff",
    "relbarlinkcolor"   : "#ffffff"
}
#--- END   OF "ADDED BY HLL" ---
