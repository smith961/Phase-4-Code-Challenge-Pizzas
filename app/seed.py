from random import choice as rc
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    #This will delete any existing rows
    #so you can run the seed file multiple times without having duplicate entries in your database
        print("Deleting data..")
        Pizza.query.delete()
        Restaurant.query.delete()
        RestaurantPizza.query.delete()

        print("Creating restaurants...")
        domino = Restaurant(name= "Domino's Pizza", address = '344 Herbert Macaulay Way')
        debonair = Restaurant(name= "Debonair's Pizza", address = '93 Awolowo Rd, Ikoyi 106104, Lagos')
        dodo = Restaurant(name= "Dodo Pizza", address = 'Way, Obafemi Awolowo Way, 194 100001, Lagos')
        restaurants = [domino, debonair,dodo]


        print("Creating pizzas...")

        cheese = Pizza(name = "Emma", ingredients = "Dough, Tomato Sauce, Cheese")
        pepperoni = Pizza(name = "Geri", ingredients = "Dough, Tomato Sauce, Cheese, Pepperoni")
        california = Pizza(name = "Melanie", ingredients = "Dough, Sauce, Ricotta, Red peppers, Mustard")
        pizzas = [cheese, pepperoni, california]

        
        
        
        print("Creating RestaurantPizza...")

        pr1 = RestaurantPizza(restaurant = domino, pizza = cheese, price = 1)
        pr2 = RestaurantPizza(restaurant = debonair, pizza = pepperoni, price = 4)
        pr3 = RestaurantPizza(restaurant = dodo, pizza = california, price = 5)
        restaurantPizzas = [pr1, pr2, pr3]

        db.session.add_all(restaurants)
        db.session.add_all(pizzas)
        db.session.add_all(restaurantPizzas)
        db.session.commit()

        print("Seeding done!")
