from . import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)

    # Define a relationship with RestaurantPizza
    pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

    # Define a relationship with RestaurantPizza
    restaurants = db.relationship('RestaurantPizza', backref='pizza', lazy=True)

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False, CheckConstraint('price >= 1 AND price <= 30'))

    # Define foreign keys for the relationships
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, price, restaurant_id, pizza_id):
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id
