import json
import traceback

from flask import render_template

def decorator(func):
	def wrapper(arg=None):
		try:
			print(arg)
			return func(arg)
		except:
			print(traceback.format_exc(), flush=True)
			return render_template('404.html')
	return wrapper

def open_json(file):
	with open(f'main/static/json/{file}.json', 'r') as fp:
		return json.load(fp)