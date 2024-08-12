from setuptools import setup, find_packages
from pathlib import Path
import os

readme_path = Path(os.path.join("..", "README.md"))
long_description = readme_path.read_text() if readme_path.is_file() else ""

setup(
    name="optiface",
    version="0.1.0",
    packages=find_packages(include=["optiface", "optiface.*"]),
    install_requires=[
        "numpy==1.20.*",
        "pandas==1.4.*",
    ],
    extras_require={
        "dev": [
            "black==24.3.0",
            "pylint==2.14.5",
            "pre-commit==3.0.0",
            "mypy==0.971",
        ],
    },
    entry_points={
        "console_scripts": [],
    },
    author="Luca Wrabetz",
    author_email="wrabetzluca@gmail.com",
    description="Python package for the components of opti-face, an (almost) turn-key suite of tools for heavily automated experiments in computational research.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/opti-face/optiface",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
