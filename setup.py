#!/usr/bin/env python
from setuptools import setup

setup(
    name="tunneldigger-broker",
    version="0.1",
    packages=["tunneldigger"],
    package_dir={"tunneldigger": "broker"},
    entry_points={
        "console_scripts": [
            "tunneldigger = tunneldigger.main",
        ]
    },
)
