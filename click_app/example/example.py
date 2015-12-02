'''
Created on 02-Dec-2015

@author: leslie
'''

import click_app

if __name__ == '__main__':
    #This will call click_app.run_string function in click_app
    #Arguments should be array of options that we need to pass
    #for example, if you need to print click help, call click_app.run_string with args like 
    #click_app.run_string(["--help"])
    click_app.run_string(["-s", "Nvent"])
