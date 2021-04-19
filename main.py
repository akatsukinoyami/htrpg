from flask import Flask
import routes

app = Flask(__name__)


@app.route('/')
def index():
    return routes.int_index()

@app.route('/info')
def info():
    return routes.int_info()

@app.route('/chars/')
def char_list():
    return routes.int_char_list()

@app.route('/enemies/')
def enemy_list():
    return routes.int_enemy_list()

@app.route('/chars/<char>/')
def user_profile(char):
    return routes.int_user_profile(char)

@app.route('/json/<char>/')
def get_user_profile_json(char):
    return routes.int_get_user_profile_json(char)

if __name__ == "__main__":
    app.run(host='192.168.1.101', port='12000', debug=False)
