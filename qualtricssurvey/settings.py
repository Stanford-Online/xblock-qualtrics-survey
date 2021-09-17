"""
Stub Settings
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
INSTALLED_APPS = (
    'qualtricssurvey',
)
LOCALE_PATHS = [
    'qualtricssurvey/translations',
]
SECRET_KEY = 'SECRET_KEY'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
