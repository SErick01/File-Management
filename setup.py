from setuptools import setup, find_packages

setup(
    name="finalproject",
    version="1.0.0",
    license="GPL-3.0",
    description="A file management application with a GUI built using PyQt6.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Samantha Ann Erickson",
    author_email="serick01@rams.shepherd.edu",
    packages=find_packages(),
    install_requires=["PyQt6"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
