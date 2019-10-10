#!/usr/bin/env python

from setuptools import setup

DESCRIPTION = """\
This is a meta package which can be installed to download and install other dependencies \
used for development in python.\
"""

setup(
    name="my-dev-env",
    version="0.2",
    author="Stepan Henek",
    author_email="stepan@henek.name",
    url="https://github.com/shenek/my-dev-env",
    license="BSD",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["black", "python-language-server", "ipython", "ipdb", "mypy"],
    extras_require={
        "node": ["nodeenv"],
        "django": ["my-dev-env[node]", "django-extensions", "django-debug-toolbar"],
        "release": ["twine"],
    },
    zip_safe=False,
    keywords="virtualenv dev",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
    ],
)
