#!/usr/bin/env python

from setuptools import setup

requirements = ['boto3']

setup(
    name='awx-credential-plugin-ecr-token',
    version='0.1',
    author='Ilya Lukuanov',
    author_email='ilya@luk.moe',
    description='',
    long_description='',
    license='MIT',
    keywords='ansible',
    url='http://github.com/ilyaluk/awx-credential-plugin-ecr-token',
    packages=['awx_credential_plugin_ecr_token'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'ecr_plugin = awx_credential_plugin_ecr_token:ecr_plugin',
        ]
    }
)
