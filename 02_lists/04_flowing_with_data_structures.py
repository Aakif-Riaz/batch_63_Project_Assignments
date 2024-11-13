def add_three_copies(my_list, message):
    for i in range(3):
        my_list.append(message)


def test():
    message = input("Enter the message to append in the list: ")
    my_list = []

    print(f"My List before appending the message: {my_list}")

    add_three_copies(my_list, message)

    print(f"My List after appending the message: {my_list}")

test()