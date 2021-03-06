# version is a human-readable version number.

# http://legacy.python.org/dev/peps/pep-0440/#version-scheme
# Use the pep-0440 as a versioning guidline
# There are always four parts, although trailing parts 'may' be empty.
# Idealy the first 3 parts will always have a value
__version__ = "0.1.12"
__version_info__ = ('0', '1', '12')

default_app_config = 'django_email_user_model.apps.UserAppConfig'
