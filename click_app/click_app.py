'''
Created on 02-Dec-2015

@author: leslie
'''

import click

@click.command()
@click.option('--string', '-s',               default='World', help="test string")
def run_string(string):
    click.echo('Hello '+string+"!")
