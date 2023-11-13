from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates, relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(reffered_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Pizza (db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # restaurants = assocition_proxy('restaurant_pizzas', 'restaurant')
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')

class RestaurantPizza (db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key = True)
    pizza_id = db.Column(db.Integer, db.Foreignkey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('price')
    def validates_price(self, key, price):
        if price >= 1 and price <= 30:
            return price
        raise ValueError({'error': "Invalid Input"})
    
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    # pizzas = association_proxy('restaurant_pizzas', 'pizza')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant")

# add any models you may need. 