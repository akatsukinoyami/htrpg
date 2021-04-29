from flask import render_template

from main.funcs import decorator, open_json

def render_table(name):
	json = open_json(name)
	return render_template('templs/table.html', **json)

@decorator
def index(_):			
	return render_table('index')

@decorator
def about(_):			
	return render_table('about')