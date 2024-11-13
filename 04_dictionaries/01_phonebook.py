def make_phonebook():
    phonebook = {}

    while True:
        name = input("Enter the name: ")
        if name == "":
            break

        number = input("Enter the number: ")
        if number == "":
            break
        phonebook[name] = number
    
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookup_numbers(phonebook):
    name = input("Enter name to find number: ")

    if name == "":
        return

    if name not in phonebook:
        print(f"Sorry, the name '{name}' is not in the phonebook.")
    else:
        print(f"The number for {name} is {phonebook[name]}")

phonebook = make_phonebook()

make_phonebook()

print_phonebook(phonebook)

lookup_numbers(phonebook)
