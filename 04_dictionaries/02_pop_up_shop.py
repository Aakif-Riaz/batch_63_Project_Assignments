def fruit_items():
    fruits = {"apple":50, "banana": 40, "mango": 45, "orange":30}

    total_cost = 0

    for fruit in fruits:
        price = fruits[fruit]

        amount_bought = int(input(f"How many {fruit} do you want to buy? "))

        total_cost += price * amount_bought
    
    print(f"Your total amount will be {total_cost}.")

fruit_items()