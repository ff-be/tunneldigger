#!/usr/bin/env python
from setuptools import setup

setup(
    name="tunneldigger-broker",
    version="0.2.0",
    packages=["tunneldigger"],
    package_dir={"tunneldigger": "broker"},
    entry_points={
        "console_scripts": [
            "tunneldigger = tunneldigger.main",
        ]
    },

    author="wlan slovenija",
    description="Client and broker for our custom L2TPv3 NAT-traversing tunnel setup protocol based on L2TPv3 support in the Linux kernel.",
    license="AGPL",
    url="http://tunneldigger.readthedocs.org/",
)
