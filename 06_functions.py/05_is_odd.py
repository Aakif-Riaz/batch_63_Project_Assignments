def is_odd():
    list = range(20)

    for i in list:
        if i % 2 == 0:
            print(f"{i} is even")
        
        else:
            print(f"{i} is odd")

is_odd()