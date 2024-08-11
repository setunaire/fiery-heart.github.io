from shop import app
from flask import render_template
from shop.models import Item
@app.route("/")
@app.route("/home/")
def home_page():
    return render_template('home.html')


@app.route("/shop/")
def shop_page():
 items = Item.query.all()
 return render_template('shop.html', items = items)
