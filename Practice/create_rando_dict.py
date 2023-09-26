def make_dict_rando1():
    import random
    from datetime import datetime, timedelta

    # List of unique first names and last names
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack", "Kate", "Liam",
                   "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Thomas", "Isabella", "William", "Sophia",
                   "James", "Emma"]
    last_names = ["Smith", "Johnson", "Davis", "Anderson", "Brown", "Miller", "Wilson", "Jackson", "Thomas", "White",
                  "Harris", "Martin", "Clark", "Anderson", "Johnson", "Davis", "Smith", "Johnson", "Wilson", "Miller",
                  "Brown", "Davis", "Jones", "Williams", "Brown"]

    # List of grocery items with random prices
    grocery_items = [
        {"item": "Apples", "price": 2.99},
        {"item": "Bananas", "price": 1.99},
        {"item": "Milk", "price": 3.49},
        {"item": "Bread", "price": 2.79},
        {"item": "Eggs", "price": 2.19},
        {"item": "Chicken", "price": 5.99},
        {"item": "Pasta", "price": 1.49},
        {"item": "Rice", "price": 2.29},
        {"item": "Cereal", "price": 3.99},
        {"item": "Tomatoes", "price": 1.79},
        {"item": "Potatoes", "price": 1.99},
        {"item": "Carrots", "price": 1.49},
        {"item": "Spinach", "price": 2.49},
        {"item": "Orange Juice", "price": 3.29},
        {"item": "Coffee", "price": 4.99},
    ]

    # List of grocery stores
    grocery_stores = ["SuperMart", "FreshGrocers", "MegaMart", "FoodWorld", "QuickMart", "Marketplace", "BudgetMart"]

    # Generate customer data
    customers = []

    for i in range(25):
        # Randomly select a first name and last name
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        # Randomly select 5 unique grocery items with prices
        selected_items = random.sample(grocery_items, 5)

        # Calculate the total cost of groceries
        total_cost = sum(item["price"] for item in selected_items)

        # Randomly select a date of purchase between 2022 and 2023
        purchase_date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")

        # Randomly select a grocery store
        store = random.choice(grocery_stores)

        # Create a customer dictionary
        customer = {
            "first_name": first_name,
            "last_name": last_name,
            "groceries": selected_items,
            "date_of_purchase": purchase_date,
            "store": store,
        }

        customers.append(customer)

    # Create the parent dictionary
    customers_dict = {"customers": customers}

    # Print the dictionary
    print(customers_dict)

def make_dict_rando2():
    import random
    from datetime import datetime, timedelta

    # List of unique first names and last names
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack", "Kate", "Liam",
                   "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Thomas", "Isabella", "William", "Sophia",
                   "James", "Emma"]
    last_names = ["Smith", "Johnson", "Davis", "Anderson", "Brown", "Miller", "Wilson", "Jackson", "Thomas", "White",
                  "Harris", "Martin", "Clark", "Anderson", "Johnson", "Davis", "Smith", "Johnson", "Wilson", "Miller",
                  "Brown", "Davis", "Jones", "Williams", "Brown"]

    # List of grocery items with random prices
    grocery_items = [
        {"item": "Apples", "price": 2.99},
        {"item": "Bananas", "price": 1.99},
        {"item": "Milk", "price": 3.49},
        {"item": "Bread", "price": 2.79},
        {"item": "Eggs", "price": 2.19},
        {"item": "Chicken", "price": 5.99},
        {"item": "Pasta", "price": 1.49},
        {"item": "Rice", "price": 2.29},
        {"item": "Cereal", "price": 3.99},
        {"item": "Tomatoes", "price": 1.79},
        {"item": "Potatoes", "price": 1.99},
        {"item": "Carrots", "price": 1.49},
        {"item": "Spinach", "price": 2.49},
        {"item": "Orange Juice", "price": 3.29},
        {"item": "Coffee", "price": 4.99},
    ]

    # List of grocery stores
    grocery_stores = ["SuperMart", "FreshGrocers", "MegaMart", "FoodWorld", "QuickMart", "Marketplace", "BudgetMart"]

    # Generate customer data
    customers = []

    for i in range(25):
        # Randomly select a first name and last name
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        # Randomly select 5 unique grocery items with prices
        selected_items = random.sample(grocery_items, 5)

        # Calculate the total cost of groceries
        total_cost = sum(item["price"] for item in selected_items)

        # Randomly select a date of purchase between 2022 and 2023
        purchase_date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")

        # Randomly select a grocery store
        store = random.choice(grocery_stores)

        # Create a customer dictionary
        customer = {
            "first_name": first_name,
            "last_name": last_name,
            "groceries": selected_items,
            "date_of_purchase": purchase_date,
            "store": store,
        }

        customers.append(customer)

    # Create the parent dictionary
    customers_dict = {"customers": customers}

    # Print the dictionary with indentation
    import json

    print(json.dumps(customers_dict, indent=4))

def make_dict_rando3_mine():
    import random
    # List of first_names:
    first_names = ["Anne", "Jane", "Laura", "Tim", "Paul"]
    last_names = ["Peterson", "Hamid", "Egerton", "Fereirs", "Rajkumar"]

    # # To make random unique name combos from a list:
    # name_combos = []
    # for i in range(5):
    #     rand_first_name = random.choice(first_names)
    #     rand_last_name = random.choice(last_names)
    #     first_names.remove(rand_first_name)
    #     last_names.remove(rand_last_name)
    #     name_combos.append((rand_first_name, rand_last_name))
    # print(name_combos)

    grocery_items = ["Apples", "Bananas", "Milk", "Bread", "Eggs", "Cheese", "Chicken", "Pasta"]
    # # To make a random list of grocery items and prices
    groceries = []
    grocery = {}
    grocery_purchases = []
    # rand_price = random.random()
    # # Round to 2 decimal places
    # rand_price_2 = round(random.random() * 100, 2)
    # # Round to decimal place but within a range
    # rand_price_3 = round(random.uniform(0.50, 7.99), 2)
    #
    while len(grocery_purchases) < len(grocery_items) - 1:
        for i in range(len(grocery_items) - 1):
            item = random.choice(grocery_items)
            grocery_items.remove(item)
            price = round(random.uniform(2.39, 7.99), 2)
            grocery_purchases.append((item, price))

    for i in grocery_purchases:
        grocery["item"] = i[0]
        grocery["price"] = i[1]
        groceries.append(grocery)
        grocery = {}

    # print(f"grocery purchases: {grocery_purchases}")
    # print(f"groceries: {groceries}")
    # print(f"grocery: {grocery}")


    grocery_stores = ["Food Mart", "Price Cheap", "Bronzi's", "ShopCo"]

    customer_list = []
    for i in range(25):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        grocery_cart = random.sample(groceries, 3)
        store = random.choice(grocery_stores)

        customer = {
            "first_name" : first_name,
            "last_name" : last_name,
            "groceries" : grocery_cart,
            "store": store,
        }

        customer_list.append(customer)
    customers_dict = {"customers": customer_list}
    # print(customers_dict)
    return customers_dict
make_dict_rando3_mine()