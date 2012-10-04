# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
import sys
import os

version = '0.1'

if __name__ == '__main__':
    setup(
        name='rejected377',
        version=version,
        description="Implementation of with block context managers that allow "
            "clearly defined skipping of the controlled block "
            "ala PEP 377 (which was rightly rejected)",
        classifiers=["Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Python Software Foundation License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Testing",
            ],
        keywords='',
        author='David Fraser',
        author_email='davidf@sjsoft.com',
        url='http://github.org/davidfraser/rejected377',
        license='GPL',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        )
