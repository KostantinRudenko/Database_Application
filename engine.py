import webbrowser
import os
import re

from config import *

def open_help_link():
    try:
        os.system(WEBBROWSER_PROMPT)
    except:
        os.system(EDGE_PROMPT)
    
def write_txt_file(text, file_name): # This func. saves queries you have written
    file = open(file_name, 'w')
    file.write(text)
    file.close()

def read_txt_file(file_name): # This function reads file
    with open(file_name +'.txt', 'r') as file:
        result = file.read()
        file.close()
    return result

def save_txt_file(data, file_name = SAVE_TXT_PATH, mode = 'w'): # This func. saves results of SELECT-queries in a text file
    with open(file_name, mode) as file:
        file.write(data)
        file.close()

def find_select_stmt(query):
    select_values = query.upper()
    select_result = ''
    for value in select_values.split('\n'):
        if 'SELECT' in value:
            select_result += value
    return select_result
