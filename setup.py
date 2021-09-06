#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="robot naoborot",
    author_email='robotnaoborot@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Allows to add sections to django admin which are not tied to any model. They can render some template for example.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='django_nonmodel_admin',
    name='django_nonmodel_admin',
    packages=find_packages(include=['django_nonmodel_admin', 'django_nonmodel_admin.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pawnhearts/django_nonmodel_admin',
    version='0.1.1',
    zip_safe=False,
)
