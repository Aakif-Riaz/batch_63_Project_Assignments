def voting_age():

    age = int(input("How old are you? "))

    if age >= 16 and age < 25:
        print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.") 

    elif age >= 25 and age < 48:
        print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")

    elif age >= 48:
        print("You can vote in Peturksbouipo where the voting age is 16. You can also vote in Stanlau where the voting age is 25. You can also vote in Mayengua where the voting age is 48.")

    else:
        print("You are not eligible to vote anywhere.")
    
voting_age()