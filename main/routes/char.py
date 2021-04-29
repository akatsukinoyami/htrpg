from flask 		import render_template

from main.funcs import decorator, open_json

@decorator
def char_profile(char):
	char_stats = [	"никак", "слабо",	"обычно", "лучше среднего",	
					"хорошо",	"легко и умело","удивительно", 
					"блестяще",	"прославленно", "легендарно"]

	return render_template('character/main.html', 
							user  = open_json(f'chars/{char}'), 
							link  = char, 
							stats = char_stats)

@decorator
def char_json(char):
	return open_json(f'chars/{char}')