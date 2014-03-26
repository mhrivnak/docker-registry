#!/usr/bin/env python

import os
import setuptools

desc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'README.md')
long_desc = open(desc_path).read()

req_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'requirements.txt')
requirements = open(req_path).read()

setuptools.setup(
    name='docker_registry',
    # TODO: Load the version programatically, which is currently available in
    #       docker_registry.app. This is not possible yet because importing
    #       causes config files to be loaded
    version='0.6.7',
    description='Registry server for Docker',
    long_description=long_desc,
    packages=setuptools.find_packages(),
    license='Apache',
    author='Docker Registry Contributors',
    author_email='docker-dev@googlegroups.com',
    url='https://github.com/dotcloud/docker-registry',
    install_requires=requirements,
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ),
    entry_points={
        'console_scripts': [
            'docker-registry = docker_registry.wsgi:console_script'
        ]
    },
)
