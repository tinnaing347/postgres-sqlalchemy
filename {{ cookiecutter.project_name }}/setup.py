 #!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os 


######### NOTE this should be changed in cookie-cutter
NAME = '{{cookiecutter.package_name}}'
DESCRIPTION = 'This is boilerplate for project description'
############

with open('README.md') as f: 
    readme = f.read()

with open('HISTORY.md') as f:
    history = f.read()

with open('requirements.txt') as f:
    requirements_txt = f.read().split('\n')

test_requirements = [
    'pytest',
    'pytest-cov'
]


# build the version from _version.py
here = os.path.abspath(os.path.dirname(__file__))
about = {}
project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
with open(os.path.join(here, project_slug, '_version.py')) as f:
    exec(f.read(), about)


setup(
    name=NAME,
    description= '',
    version=about['VERSION'],
    long_description=readme,
    history=history,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "scripts"]),
    include_package_data=True,
    install_requires=requirements_txt,
    test_suite='pytest',
    tests_require=test_requirements, 
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
)