from main.funcs import *

json_folder = 'main/static/json'

@decorator
def index(_):			
	return render_table('index')
@decorator
def info(_): 			
	return render_list('info', 'infolist.html')
@decorator
def char_list(_):	
	return render_list('chars', 'charlist.html')
@decorator
def enemy_list(_):
	return render_list('enemies', 'enemylist.html')

@decorator
def user_profile(char):
	mytemplate = {
		'template_name_or_list' : 'character.html',
		'user' 									: open_json(f'{json_folder}/chars/{char}.json'),
		'link' 									: char,
		'stats'									: ["никак", "слабо",	"обычно",	
			"лучше среднего",	"хорошо",	"легко и умело","удивительно", 
			"блестяще",	"прославленно", "легендарно"]}
	return mytemplate

@decorator
def user_profile_json(char):
	myjson = open_json(f'{json_folder}/chars/{char}.json')

	mytemplate = {
		'template_name_or_list' : 'sub/empty.html',
		'var' : myjson}
		
	return mytemplate