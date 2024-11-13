def pythagoras():

    ab = float(input("Enter the length of one side: "))
    ac = float(input("Enter the length of second side: "))

    import math

    bc = math.sqrt(ab ** 2 + ac ** 2)

    print(bc)

pythagoras()