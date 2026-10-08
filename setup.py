from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="khamyang",
    version="1.0.0",
    author="Akshat Singh Bisht",
    author_email="infoakshatsinghbisht@gmail.com",
    maintainer="Akshat Singh Bisht",
    maintainer_email="infoakshatsinghbisht@gmail.com",
    description="A Python language library and revitalization toolkit for Tai Khamyang (ksu)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/infoakshatsinghbisht-eng/khamyang-language-library",
    project_urls={
        "Homepage": "https://akshatsinghbisht.com/",
        "GitHub": "https://github.com/infoakshatsinghbisht-eng/khamyang-language-library",
        "LinkedIn": "https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/",
        "Amazon Author": "https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28",
        "ResearchGate": "https://www.researchgate.net/profile/Akshat-Bisht-8",
        "Bug Tracker": "https://github.com/infoakshatsinghbisht-eng/khamyang-language-library/issues",
    },
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
