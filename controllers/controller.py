from app import app
from flask import render_template
from models.orders_list import orders

@app.route('/')
def index():
    return "My Shop"

@app.route('/orders')
def get_orders():
    return render_template('index.html', title='Orders', orders=orders)

# @app.route('/orders/')
# def get_single_order():
#     return render_template('order.html')