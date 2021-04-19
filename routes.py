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

@decorator
def int_index(_):
    return render_template('index.html')

@decorator
def int_char_list(_):
	charlist = {}
	for char in os.listdir('static/chars/info'):
		char = char.replace('.json', '')
		with open(f'static/chars/info/{char}.json', 'r') as file:
				charlist[char] = json.load(file)
	
	return render_template('charlist.html', chars=charlist)


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
