import os
import requests

from flask import Flask
from flask import render_template
from flask import redirect, url_for, request, make_response

# Internal
from lib.mongo import get_all, find, insert_one, get_menu
from lib.menu_utils import transform_menu, filter_by_calories

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', restaurants=get_all("rest_name"))

@app.route('/restaurant/<webname>', methods= ['GET'])
def restaurant(webname):
    menu = transform_menu(get_menu(webname))
    name = ""
    try:
        name = menu[0]['items'][0]['name']
    except:
        name = ""

    return render_template('restaurant.html', name=name, menu=menu)

@app.route('/restaurant/<webname>/<calorie_limit>', methods= ['GET'])
def restaurant_calories(webname, calorie_limit):
    menu = get_menu(webname)
    filtered_menu = transform_menu(
        filter_by_calories(menu, float(calorie_limit))
    )
    name = ""
    try:
        name = filtered_menu[0]['items'][0]['name']
    except:
        name = ""

    return render_template('restaurant.html', name=name, menu=filtered_menu, calorie_limit=calorie_limit)
