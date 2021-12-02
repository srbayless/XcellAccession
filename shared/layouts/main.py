from shared import names, routes, templates

# default values used by the main layout

TEMPLATE_PATH = 'layouts/main/index.html'

DEFAULT_STYLESHEETS = [
    'assets/css/main.css',
]

DEFAULT_CONTEXT_CONTENT = {}

DEFAULT_CONTEXT_MAIN = {
    'page_title': 'Page Title',
    'links_stylesheet': DEFAULT_STYLESHEETS,
    'template_header': templates.TEMPLATE_HEADER,
    'template_content': templates.TEMPLATE_DEFAULT,
    'context_content': DEFAULT_CONTEXT_CONTENT,    
}