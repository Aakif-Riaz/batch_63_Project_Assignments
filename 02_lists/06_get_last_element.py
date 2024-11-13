def my_list():

    lst = []

    element = input("Enter any element: ")
    
    while element != "":
        lst.append(element)
        print(lst)
        element = input("Enter another element: ")
    
    return lst

new_list = my_list()

def get_last_element(lst):
    print(lst[-1])


get_last_element(new_list)

