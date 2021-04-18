import json

from flask import render_template

from __main__ import app

stats = ["никак", "слабо",	"обычно",
					"лучше среднего",	"хорошо",
					"легко и умело",	"удивительно",
					"блестяще",		"прославленно",
					"легендарно"]

@app.route('/chars/<char>/')
def user_profile(char):
	try:
		with open(f'static/chars/{char}.json', 'r') as char_form:
			return render_template(
															'character.html', 
															user=json.load(char_form), 
															link=char, 
															stats=stats
														)
	except Exception as e:
		print(e)
		return render_template('404.html')