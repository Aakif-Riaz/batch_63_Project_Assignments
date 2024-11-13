def min_height_to_ride():
    minimum_height: int = 40

    height = int(input("Enter your height: "))

    if height >= minimum_height:
        print("You are allowed to ride.")
    
    else:
        print("You are not allowed to ride.")
    
min_height_to_ride()