import flask
from . import app 
from .models import products


@app.route("/")
@app.route("/home")
def index():
    return flask.render_template("index.html", title="firas's online shope", title2="online shope")

@app.route("/product/<product_name>")
def profile_page(product_name):
    for product in products:
        if product['name'].lower() == product_name.lower(): 
            break
    else:
        return "product not found"

    return flask.render_template("product_page.html", product=product)

@app.route("/product/<int:product_id>")
def id_page(product_id):
    for product in products:
        if product['id'] == product_id: 
            break
    else:
        return "product not found"

    return flask.render_template("product_page.html", product=product)

@app.route("/search/by-category/<category>")
def cat_list(category):
    temp = [ ]
    for product in products:
        if product['category'] == category: 
              temp.append(product)
    if not temp:
        return "product not found"
    return flask.render_template("products_list.html", products=temp)

@app.route("/products_list")
def products_list():
    return flask.render_template("products_list.html", products=products)



    