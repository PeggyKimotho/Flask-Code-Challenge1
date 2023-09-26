from flask import jsonify, request, abort
from . import app, db
from .models import Restaurant, Pizza, RestaurantPizza

# Define a route to get a list of all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [{
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address
    } for restaurant in restaurants]
    return jsonify(restaurant_list)

# Define a route to get a restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    pizzas = [{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    } for pizza in restaurant.pizzas]

    restaurant_data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas
    }

    return jsonify(restaurant_data)

# Define a route to delete a restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    # Delete associated RestaurantPizzas first
    RestaurantPizza.query.filter_by(restaurant_id=restaurant.id).delete()
    
    # Now, delete the restaurant
    db.session.delete(restaurant)
    db.session.commit()

    return '', 204

# Define a route to get a list of all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    } for pizza in pizzas]
    return jsonify(pizza_list)

# Define a route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate input data here (e.g., check if the pizza and restaurant exist)

    new_restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(new_restaurant_pizza)
    db.session.commit()

    # Return the related Pizza data as a response
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        return jsonify({'error': 'Pizza not found'}), 404

    pizza_data = {
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }

    return jsonify(pizza_data), 201

# Define a route to create a new Pizza
@app.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.json

    # Extract pizza data from the request JSON
    name = data.get('name')
    ingredients = data.get('ingredients')

    # Validate input data as needed

    # Create a new pizza
    new_pizza = Pizza(name=name, ingredients=ingredients)

    # Add the pizza to the database
    db.session.add(new_pizza)
    db.session.commit()

    # Return a response indicating success
    return jsonify({'message': 'Pizza created successfully'}), 201

# Define a route to create a new Restaurant
@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.json

    # Extract restaurant data from the request JSON
    name = data.get('name')
    address = data.get('address')

    # Validate input data as needed

    # Create a new restaurant
    new_restaurant = Restaurant(name=name, address=address)

    # Add the restaurant to the database
    db.session.add(new_restaurant)
    db.session.commit()

    # Return a response indicating success
    return jsonify({'message': 'Restaurant created successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
