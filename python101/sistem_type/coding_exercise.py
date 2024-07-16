# Defining variables with data types

# A string variable that holds the customer's name.
customer_name = "John Doe"

# A string variable for the base pizza type.
base_pizza = "Italian crust"

# An integer for pizza size. Here number 1 represents small, 2 represents medium and 3 represents large.
pizza_size = 2

# A tuple for ingredients contained in the base pizza.
ingredients = ("Tomato", "Mozzarella", "Basil", "Olive oil")

# A string variable for extra ingredient added on top of the base pizza.
extra_ingredient = "Mushrooms"

# A boolean variable to check if extra cheese has been added. It's true if extra cheese is added.
extra_cheese = True

# A float variable to hold the price of the pizza.
price = 14.99

# Printing defined variables with logical messages and f-string formatting.

# Option 1
print("* Option 1")
print(f"The customer's name is {customer_name}.")
print(f"The chosen base for the pizza is {base_pizza}.")
print(f"The pizza size selected is {pizza_size} inches.")
print(f"The ingredients for the {base_pizza} pizza are {ingredients}.")
print(f"An extra ingredient added to the pizza is {extra_ingredient}.")
print(f"It is {extra_cheese} that extra cheese has been added to the pizza.")
print(f"The total price of the pizza is {price} dollars.")

# Option 2
print("\n * Option 2")
order_details = f"""The pizza order is made by {customer_name}. They have selected a {base_pizza} pizza of size
{pizza_size} inches. The standard ingredients of this pizza are {ingredients}. 
They have chosen to add {extra_ingredient} as an extra topping. It is {extra_cheese} that an extra 
cheese topping has been included. "The total cost of this order is {price} dollars."""
print(order_details)

# Option 3
print("\n * Option 3")
print(f"""The pizza order is made by {customer_name}. They have selected a {base_pizza} pizza of size
{pizza_size} inches. The standard ingredients of this pizza are {ingredients}. 
They have chosen to add {extra_ingredient} as an extra topping. It is {extra_cheese} that an extra 
cheese topping has been included. "The total cost of this order is {price} dollars.""")
