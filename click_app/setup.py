'''
Created on 02-Dec-2015

@author: leslie
'''

from setuptools import setup

setup(
    name='click_app',
    version='0.1',
    py_modules=['click_app'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        click_app=click_app:run_string
    ''',
)

