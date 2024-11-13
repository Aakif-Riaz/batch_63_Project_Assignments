adult_age: int = 18

def is_adult(age:int):
    if age >= adult_age:
        return True
    
    else:
        return False
    
def main():
    age = int(input("Enter Age: "))
    print(is_adult(age))


main()