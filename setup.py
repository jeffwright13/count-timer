#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="count-timer",
    version="0.3.5",
    author="Jeff Wright",
    author_email="jeff.washcloth@gmail.com",
    license="MIT",
    url="https://github.com/jeffwright13/count-timer",
    description="A count-timer with optional expiry that can be paused, resumed, and reset.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["count_timer"],
    python_requires=">=3.7",
    install_requires=[
        "blessed>=1.19.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="python counter timer count-timer count_timer",
    entry_points={
        "console_scripts": [
            "demo1=count_timer.demo:main",
            "demo2=count_timer.demo_thread:main",
        ]
    },
)
