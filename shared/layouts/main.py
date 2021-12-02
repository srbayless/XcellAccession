from copy import deepcopy

from shared import names, routes, templates

# default values used by the main layout

TEMPLATE_PATH = 'layouts/main/index.html'

DEFAULT_STYLESHEETS = [
    'assets/css/main.css',
    'assets/css/main/header/half_up.css',
    'assets/css/main/header/half_down/index.css',
    'assets/css/main/header/half_down/menu.css',
    'assets/css/main/header/half_down/user_options.css',
]

DEFAULT_CONTEXT_CONTENT = {}
DEFAULT_CONTEXT_FACILITIES = {
    'count_pending': 0,
}
DEFAULT_CONTEXT_FOLLOW_UPS = {
    'count_pending': 0,
}
DEFAULT_CONTEXT_MENU = {
    'navigation_links': {
        names.NAME_ACCESSION: {
            'label': 'Add New Case',
            'link': routes.ROUTE_ACCESSION,
        },
        names.NAME_FLOFORM: {
            'label': 'Pre-Acessioning',
            'link': routes.ROUTE_FLOFORM,
        },
        names.NAME_DASHBOARD: {
            'label': 'Main Dashboard',
            'link': routes.ROUTE_DASHBOARD,
        },
        names.NAME_COMPLETED_CASES: {
            'label': 'Completed Cases',
            'link': routes.ROUTE_COMPLETED_CASES,
        },
        names.NAME_UTILITIES: {
            'label': 'Utilities',
            'link': routes.ROUTE_UTILITIES,
        },
        names.NAME_REPORTS: {
            'label': 'Reports',
            'link': routes.ROUTE_REPORTS,
        },
    }
}
DEFAULT_CONTEXT_USER_OPTIONS = {
    'count_favorites': 0,
    'count_to_do': 0,
}

DEFAULT_CONTEXT_MAIN = {
    'page_title': 'Page Title',
    'links_stylesheet': DEFAULT_STYLESHEETS,
    'template_header': templates.TEMPLATE_HEADER,
    'template_content': templates.TEMPLATE_DEFAULT,
    'context_content': DEFAULT_CONTEXT_CONTENT,
    'context_facilities': DEFAULT_CONTEXT_FACILITIES,
    'context_follow_ups': DEFAULT_CONTEXT_FOLLOW_UPS,
    'context_menu': DEFAULT_CONTEXT_MENU,
    'context_user_options': DEFAULT_CONTEXT_USER_OPTIONS,
}

def GENERATE_DEFAULT_CONTEXT():
    return deepcopy(DEFAULT_CONTEXT_MAIN)