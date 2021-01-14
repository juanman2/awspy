#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'awspy-juanman2',
    version = '0.01',
    description='Python aws s3 tools for devops',
    author='Juan Tellez',
    author_email='juantellez64@gmail.com',
    url='https://github.com/juanman2/awspy',
    py_modules=['s3ls'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    )
