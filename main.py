from flask  import Flask

from routes import *

app = Flask(__name__)

routeslist = (
    ('/',             'index',             index),
    ('/info',         'info',              info),
    ('/chars/',       'char_list',         char_list),
    ('/enemies/',     'enemy_list',        enemy_list),
    ('/chars/<arg>/', 'user_profile',      user_profile),
    ('/json/<arg>/',  'user_profile_json', user_profile_json),
)

for i in routeslist:
    app.add_url_rule(*i)