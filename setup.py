from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="khamyang",
    version="1.0.0",
    author="Khamyang Language Revitalization Initiative",
    author_email="info@khamyang-language.org",
    description="A Python language library and revitalization toolkit for Tai Khamyang (ksu)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khamyang-revitalization/khamyang",
    packages=find_packages(),
    package_data={
        "khamyang": [
            "data/*.json",
            "web/static/*",
            "web/templates/*",
        ]
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "rich>=12.0.0",
        "fastapi>=0.80.0",
        "uvicorn>=0.18.0",
    ],
    entry_points={
        "console_scripts": [
            "khamyang=khamyang.cli:cli",
        ],
    },
)
