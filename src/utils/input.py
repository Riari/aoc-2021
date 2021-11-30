import os
import string

def getInput(day: string, ext: string = '.txt'):
    file = open(f'input/{day}{ext}', 'r')
    return file.readlines()
