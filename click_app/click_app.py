'''
Created on 02-Dec-2015

@author: leslie
'''

import click

#Simple click command implementation to demonstrate click_app installation and usage
#Get details more about click in http://click.pocoo.org/5/
@click.command()
@click.option('--string', '-s',               default='World', help="test string")
def run_string(string):
    click.echo('Hello '+string+"!")
