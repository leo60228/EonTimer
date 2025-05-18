#!/usr/bin/env python3

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='EonTimer',
    version='3.0.0',
    packages=['eon_timer'] + list(map(lambda it: f'eon_timer.{it}', find_packages('eon_timer'))),
    include_package_data=True,
    package_data={
        'eon_timer/resources': ['*.png'],
        'eon_timer/resources/fonts': ['*.ttf'],
        'eon_timer/resources/sounds': ['*.wav'],
        'eon_timer/resources/themes': ['*.zip'],
        'eon_timer': ['properties.json']
    },
    install_requires=required,
    entry_points={
        'gui_scripts': [
            'EonTimer = eon_timer.main:main'
        ]
    }
)
