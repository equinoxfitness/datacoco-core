#!/usr/bin/env python

"""
setuptools install script.
"""
import os
import re
from setuptools import setup


def get_version():
    version_file = open(os.path.join("datacoco_core", "__version__.py"))
    version_contents = version_file.read()
    return re.search('__version__ = "(.*?)"', version_contents).group(1)


setup(
    name="datacoco_core",
    packages=["datacoco_core"],
    version=get_version(),
    license="MIT",
    description="Core features of common code utility",
    long_description=open("README.rst").read(),
    author="Equinox Fitness",
    url="https://github.com/equinoxfitness/datacoco-core",
    download_url="https://github.com/equinoxfitness/datacoco-core/archive/v-0.1.0.tar.gz",
    keywords=["helper", "config", "logging", "common"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
