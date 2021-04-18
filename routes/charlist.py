import os
import json

from flask import render_template

from __main__    import app

@app.route('/chars/')
def char_list():
    charlist = {}
    for char in os.listdir('static/chars'):
        if 'template' not in char:
            char = char.replace('.json', '')
            with open(f'static/chars/{char}.json', 'r') as file:
                charlist[char] = json.load(file)
    
    return render_template('charlist.html', chars=charlist)
