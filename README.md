# Flask-Code-Challenge1

## Introduction
The Flask Pizza Restaurant API is a web application built using Flask. This API allows users to manage pizza restaurants and the pizzas they offer. It provides a set of endpoints to perform various operations related to restaurants and pizzas.

## API Endpoints
The API provides the following endpoints:

- GET /restaurants: Get a list of all restaurants.
- GET /restaurants/:id: Get details of a restaurant by its ID.
- POST /restaurants: Create a new restaurant.
- DELETE /restaurants/:id: Delete a restaurant by its ID.
- GET /pizzas: Get a list of all pizzas.
- POST /pizzas: Create a new pizza.
- GET /restaurant_pizzas: Get a list of all restaurant-pizza associations.
- POST /restaurant_pizzas: Create a new restaurant-pizza association.

## Database Models
The application uses SQLAlchemy to interact with the database. It defines the following models:

- Restaurant: Represents a pizza restaurant.
- Pizza: Represents a type of pizza.
- RestaurantPizza: Represents a relationship between a restaurant and a pizza, including the price.
