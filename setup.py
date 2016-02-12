#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

install_requires = [x.strip() for x in requirements if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in requirements if "git+" not in x]

setup(
    name="cellbell",
    version="0.0.1",
    description="Bell magic for jupyter notebook",
    long_description=readme,
    author="Abhinav Tushar",
    author_email="abhinav.tushar.vs@gmail.com",
    url="https://github.com/lepisma/cellbell",
    include_package_data=True,
    install_requires=install_requires,
    license="MIT",
    keywords="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    dependency_links=dependency_links,
    packages=find_packages(exclude=["docs", "tests*"]),
)
