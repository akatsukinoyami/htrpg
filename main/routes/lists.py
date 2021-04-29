import os

from flask import render_template

from main.funcs import decorator, open_json

def render_list(address, template):
	charlist = []

	for char in os.listdir(f'main/static/json/{address}'):
		char = char.replace('.json', '')
		mychar = open_json(f'{address}/{char}')
		mychar['link'] = char
		charlist.append(mychar)
		
	mysort = lambda i: ord(i['link'][0])
	chars = sorted(charlist, key=mysort)
	
	return render_template(template, chars=chars)

@decorator
def list_info(_): 			
	return render_list('info', 'lists/info.html')

@decorator
def list_chars(_):	
	return render_list('chars', 'lists/chars.html')

@decorator
def list_enemies(_):
	return render_list('enemies', 'lists/enemies.html')