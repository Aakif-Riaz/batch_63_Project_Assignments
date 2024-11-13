def shorten(list):
    # maximum_length : int = 4
    newlist=[]
    while len(list) > 4:
        newlist.append(list.pop())
    
    print(newlist)

def makelist():
    list = []
    element = input("Enter any element: ")
    
    while element:
        list.append(element)
        print(list)
        element = input("Enter another element: ")
    
    return list



vav = makelist()

shorten(vav)