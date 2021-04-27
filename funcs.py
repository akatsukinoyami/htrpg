import os
import json
import traceback

from flask import render_template

def decorator(func):
	def wrapper(arg=None):
		try:
			print(arg)
			mytemplate = func(arg)	

		except:
			print(traceback.format_exc(), flush=True)
			mytemplate = {'template_name_or_list' : '404.html',}

		finally:
			return render_template(**mytemplate)

	return wrapper

def open_json(file):
	with open(file, 'r') as fp:
		return json.load(fp)

def render_table(name):
	mydict = open_json(f'static/json/{name}.json')
	mytemplate = dict(template_name_or_list='sub/table.html', **mydict) 

	return mytemplate

def render_list(address, template):
	charlist = []

	for char in os.listdir(f'static/json/{address}'):
		char = char.replace('.json', '')
		mychar = open_json(f'static/json/{address}/{char}.json')
		mychar['link'] = char
		charlist.append(mychar)
		
	mysort = lambda i: ord(i['link'][0])
	
	mytemplate = {
		'template_name_or_list' : template,
		'chars' : sorted(charlist, key=mysort),
	} 
	return mytemplate