def get_user_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email_address = input("Enter your email address: ")

    return first_name, last_name, email_address

def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)


main()