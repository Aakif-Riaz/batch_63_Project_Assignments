def get_list():

    list = []

    value = input("Enter any value: ")

    while value:
        list.append(value)
        value = input("Enter another value: ")

    print(list)

get_list()