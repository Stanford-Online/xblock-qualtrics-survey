"""
XBlock for linking to a Qualtrics survey
"""
from setuptools import setup
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.base'
description = __doc__

setup(
    name='xblock_qualtrics_survey',
    version='0.1.3',
    description=description,
    long_description=description,
    author='David Adams',
    author_email='dcadams@stanford.edu',
    url="https://github.com/Stanford-Online/xblock-qualtrics-survey",
    license='AGPL-3.0',
    packages=[
        'qualtricssurvey',
    ],
    install_requires=[
        'Django<2.0.0',
        'edx-opaque-keys',
        'mock',
        'XBlock',
        'xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'qualtricssurvey = qualtricssurvey:QualtricsSurvey',
        ],
    },
    package_dir={
        'qualtricssurvey': 'qualtricssurvey',
    },
    package_data={
        '': [
        ],
        "qualtricssurvey": [
            'public/*',
        ],
    },
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='qualtricssurvey.tests',
)
