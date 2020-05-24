#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version('djangocms_redirect', '__init__.py')

if sys.argv[-1] == 'publish':
    try:
        import wheel  # NOQA
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print('Tagging the version on github:')
    os.system('git tag -a %s -m "version %s"' % (version, version))
    os.system('git push --tags')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-redirect',
    version=version,
    description="""A django CMS enabled application to handle redirects""",
    long_description=readme + '\n\n' + history,
    maintainer='Nephila',
    maintainer_email='web@nephila.it',
    author='Paolo Romolini',
    author_email='p.romolini@nephila.it',
    url='https://github.com/nephila/djangocms-redirect',
    packages=[
        'djangocms_redirect',
    ],
    include_package_data=True,
    install_requires=[
        'django-cms'
    ],
    license='BSD',
    zip_safe=False,
    keywords='djangocms-redirect',
    test_suite='cms_helper.run',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
