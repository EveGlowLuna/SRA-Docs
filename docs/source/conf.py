# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SRA-Docs'
copyright = '2025 StarRailAssistant'
author = 'EveGlow'

release = '0.1'
version = '0.8.2.2'

# -- General configuration

language = 'zh_CN'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Enable syntax highlighting
pygments_style = 'sphinx'
highlight_language = 'python'
highlights_options = {
    'stripnl': True,
    'stripall': True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
