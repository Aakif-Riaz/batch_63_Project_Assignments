def count_even():
    lst = []
    
    while True:
        user_input = input("Enter an integer or press Enter to stop: ")
        if user_input == "":
            break
        lst.append(int(user_input))
    
    print(lst)

    even_count = 0
    for i in lst:
        if i % 2 == 0:
            even_count += 1

    print("Number of even numbers:", even_count)

count_even()
