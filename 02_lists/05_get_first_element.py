def get_list():

    lst = []

    elem = input("Enter any element: ")

    while elem != "":
        
        lst.append(elem)

        print(lst)

        elem = input("Enter another element: ")

        lst.append(elem)
        
        
    return lst
    
my_new_list = get_list()

def get_first_element(lst):
    print(lst[0])

get_first_element(my_new_list)