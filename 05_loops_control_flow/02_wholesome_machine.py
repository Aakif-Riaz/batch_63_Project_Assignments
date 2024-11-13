def affirmation():
    
    typed_input = "I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to."

    user_input = input(f"Please type this affirmation as it is. {typed_input}")
    while user_input != typed_input:
        print("That was not the affirmation. Please type again below.")
        user_input = input("Type here: ")
    
    else:
        print("That's right. :)")


affirmation()