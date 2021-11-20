#!/usr/bin/env python
from setuptools import setup, find_packages

app_name = "authserv"
version = "0.22"
long_description = "authserv package"

setup(
    name = app_name,
    version = version,
    packages = find_packages(),
    include_package_data = True,
    install_requires=["requests"],
    author = "V.Egorov",
    author_email = "v.egorov@millionagents.com",
    description = long_description,
    long_description = long_description,
)
