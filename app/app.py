#!/usr/bin/env python3

from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_restful import Api

from models import db, Restaurant, RestaurantPizza, Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1> Code Challenge 1 </h1>'

@app.route('/restaurants', methods= ['GET'])
def restaurants():
    if request.method == 'GET':
        restaurant_list = [r.to_dict() for r in Restaurant.query.all()]
        response = make_response(
            restaurant_list, 
            200
        )

        return response
@app.route('/restaurant_pizzas', method = ['POST'])
def new_restaurant():
    data = request.get_json()
    new_pizza_restaurant = RestaurantPizza(
        price = data['price'],
        pizza_id = data['pizza_id'],
        restaurant_id = data['restaurant_id']
    )
    db.session.add(new_pizza_restaurant)
    db.session.commit()

    try:
        return make_response(new_pizza_restaurant.to_dict(rules=('pizza', '-restaurant')),201)
    except ValueError:
        return make_response({'error': ['Invalid input']}, 400)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
