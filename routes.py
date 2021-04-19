import os
import json
import traceback

from flask import render_template

def decorator(func):
	def wrapper(args=None):
		try:
			return func(args)	
		except:
			print(traceback.format_exc(), flush=True)
			return render_template('404.html')
	return wrapper

def render_table(name):
	with open(f'static/json/{name}.json', 'r') as content:
		mydict = dict(json.load(content))
		return render_template('sub/table.html', **mydict)

def render_list(address, template):
	charlist = {}
	for char in os.listdir(address):
		char = char.replace('.json', '')
		with open(f'{address}/{char}.json', 'r') as file:
				charlist[char] = json.load(file)
	return render_template(template, chars=charlist)

@decorator
def int_index(_):
	return render_table('index')

@decorator
def int_info(_):
    return render_table('info')

@decorator
def int_char_list(_):
	return render_list('static/chars/info', 'charlist.html')

@decorator
def int_enemy_list(_):
	return render_list('static/json/enemies', 'enemylist.html')

@decorator
def int_user_profile(char):
	with open(f'static/chars/info/{char}.json', 'r') as char_form:
		kwargs = {
			'template_name_or_list' : 'character.html',
			'user' 									: json.load(char_form),
			'link' 									: char,
			'stats'									: ["никак", "слабо",	"обычно",	
				"лучше среднего",	"хорошо",	"легко и умело","удивительно", 
				"блестяще",	"прославленно", "легендарно"]}
	return render_template(**kwargs)

@decorator
def int_get_user_profile_json(char):
	with open(f'static/chars/info/{char}.json', 'r') as char_form:
		return json.load(char_form)


