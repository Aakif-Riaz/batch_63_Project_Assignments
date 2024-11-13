def double_it():

    user_input = int(input("Enter any number: "))

    while user_input > 0 and user_input < 100:
        user_input = user_input * 2
        print(user_input, end=" ")

double_it()