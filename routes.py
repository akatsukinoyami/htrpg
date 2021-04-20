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

def open_json(file):
	with open(file, 'r') as fp:
		return json.load(fp)

def render_table(name):
	mydict = dict(open_json(f'static/json/{name}.json'))
	return render_template('sub/table.html', **mydict)

def render_list(address, template):
	charlist = {}
	for char in os.listdir(f'static/json/{address}'):
		char = char.replace('.json', '')
		charlist[char] = open_json(f'static/json/{address}/{char}.json')
	return render_template(template, chars=charlist)

@decorator
def int_index(_):			return render_table('index')
@decorator
def int_info(_): 			return render_list('info', 'info.html')
@decorator
def int_char_list(_):	return render_list('chars', 'charlist.html')
@decorator
def int_enemy_list(_):return render_list('enemies', 'enemylist.html')

@decorator
def int_user_profile(char):
	kwargs = {
		'template_name_or_list' : 'character.html',
		'user' 									: open_json(f'static/json/chars/{char}.json'),
		'link' 									: char,
		'stats'									: ["никак", "слабо",	"обычно",	
			"лучше среднего",	"хорошо",	"легко и умело","удивительно", 
			"блестяще",	"прославленно", "легендарно"]}
	return render_template(**kwargs)

@decorator
def int_get_user_profile_json(char):
	return open_json(f'static/json/chars/{char}.json')