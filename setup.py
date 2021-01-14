#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'awspy-juanman2',
    version = '0.0.1',
    description='Python aws s3 tools for devops',
    long_description=long_description,
    author='Juan Tellez',
    author_email='juantellez64@gmail.com',
    url='https://github.com/juanman2/awspy',
    py_modules=['s3ls'],
    packages=setuptools.find_packages(),
    install_requires=['boto3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            's3ls=s3ls:main',
        ],
    },
    python_requires='>=3.8',
)
