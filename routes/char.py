import json

from flask import render_template

from __main__ import app

@app.route('/chars/<char>/')
def user_profile(char):
	try:
		with open(f'chars/{char}.json', 'r') as char_form:
			return render_template('character.html', user=json.load(char_form))
	except:
		return render_template('404.html')