def get_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name+" "+last_name
    

def greeting():
    name = get_name()
    print(f"Howdy, {name} :)")

greeting()