#!/usr/bin/env python
import sys
from setuptools import setup, find_namespace_packages, sic

if sys.version_info < (3, 7):
    print('Error: Soda SQL requires at least Python 3.7')
    print('Error: Please upgrade your Python version to 3.7 or later')
    sys.exit(1)

package_name = "soda-sql-core"
package_version = "2.1.0-alpha1"
# TODO Add proper description
description = "Soda SQL Core"

requires = [
    'click>=7.1.2',
    'pyyaml>=5.4.1',
    'Jinja2>=2.11.3',
    'cryptography>=3.3.2'
]
# TODO Fix the params
# TODO Add a warning that installing core doesn't give any warehouse functionality

setup(
    name=package_name,
    version=sic(package_version),
    packages=find_namespace_packages(include=["sodasql*"]),
    install_requires=requires,
    entry_points={
        "console_scripts":
            [
                "soda=sodasql.cli.cli:main"
            ]
    },
)
