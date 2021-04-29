from main.routes.tables	import index, about
from main.routes.char 	import char_profile, char_json
from main.routes.lists	import list_info, list_chars, list_enemies
from main.routes.auth 	import login, register, logout

def assign_routes(app):
	routeslist = (
		#information in tables
		('/',            	'index',       index       ),
		('/about',       	'about',       about       ),
		#lists
		('/info',        	'list_info',   list_info   ),
		('/chars/',      	'list_chars',  list_chars  ),
		('/enemies/',    	'list_enemies',list_enemies),
		#char
		('/chars/<arg>/',	'char_profile',char_profile),
		('/json/<arg>/', 	'char_json',   char_json   ),
		#authorization
		('/login', 			'login',   		login,		['GET', 'POST']),
		('/register', 		'register',    	register,	['GET', 'POST']),
		('/logout', 		'logout',    	logout		),
	)

	for i in routeslist:
		url = {
			'rule'		: i[0], 
			'endpoint'	: i[1], 
			'view_func'	: i[2]
			}

		if len(i) == 4: 
			url['methods'] = i[3]

		app.add_url_rule(**url)
	