from .base import *

# ENVIRONMENT = 'development'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = not DEBUG

# INSTALLED_APPS = globals().get('INSTALLED_APPS', [])
# INSTALLED_APPS += [
#     'debug_toolbar',
# ]