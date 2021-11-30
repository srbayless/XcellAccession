# default values used by the main layout

TEMPLATE_PATH = 'layouts/main/index.html'

DEFAULT_STYLESHEETS = [
    'assets/css/main.css',
]

DEFAULT_CONTEXT_LOGO = {}
DEFAULT_CONTEXT_USER = {}
DEFAULT_CONTEXT_MENU = {}
DEFAULT_CONTEXT_CONTENT = {}

DEFAULT_CONTEXT_MAIN = {
    'page_title': 'Page Title',
    'links_stylesheet': DEFAULT_STYLESHEETS,
    'template_logo': 'layouts/main/logo.html.part',
    'template_user': 'layouts/main/user.html.part',
    'template_menu': 'layouts/main/menu.html.part',
    'template_content': 'layouts/main/contents/default.html.part',
    'context_logo': DEFAULT_CONTEXT_LOGO,
    'context_user': DEFAULT_CONTEXT_USER,
    'context_menu': DEFAULT_CONTEXT_MENU,
    'context_content': DEFAULT_CONTEXT_CONTENT,    
}