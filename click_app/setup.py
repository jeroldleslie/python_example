'''
Created on 02-Dec-2015

@author: leslie
'''

from setuptools import setup
#To understand more about click setup tools look http://click.pocoo.org/5/setuptools/
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

