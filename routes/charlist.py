import os

from flask import render_template

from __main__ import app

@app.route('/chars/')
def char_list():
    listchars = [f.replace('.json', '') for f in os.listdir('chars') if 'template' not in f]
    return render_template('chars.html', chars=listchars)
