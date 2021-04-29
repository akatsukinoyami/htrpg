from flask          import Flask

from main.models    import UserModel, db, login
from main.routes    import assign_routes

app = Flask(__name__)
app.secret_key = 'xyz'
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login.init_app(app)
login.login_view = 'login'

assign_routes(app)

@app.before_first_request
def create_all():
    db.create_all()