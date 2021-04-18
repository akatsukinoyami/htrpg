from flask import Flask

app = Flask(__name__)

import routes

if __name__ == "__main__":
    app.run(host='192.168.1.101', port='12000', debug=False)
