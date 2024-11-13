def in_range(n):
    low: int = 20
    high: int = 50

    if n >= low and n <= high:
        return True
    
    else:
        return False
    
def main():
    n = int(input("Enter any number: "))
    print(in_range(n))

main()