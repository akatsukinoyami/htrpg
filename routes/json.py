import json

from flask import render_template

from __main__ import app

@app.route('/json/<char>/')
def get_user_profile_json(char):
	try:
		with open(f'static/chars/{char}.json', 'r') as char_form:
			return json.load(char_form)
	except Exception as e:
		print(e)
		return render_template('404.html')