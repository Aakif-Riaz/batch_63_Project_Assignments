def num_in_stock(fruit):
    if fruit == 'apple':
        return 50
    elif fruit == 'banana':
        return 200
    elif fruit == 'orange':
        return 80
    else:
        return 0

def main():
    fruit = input("Enter fruit name: ")
    stock = num_in_stock(fruit)
    if stock > 0:
        print(f"This fruit is in stock. Here is how many: {stock}")
    else:
        print("This fruit is not in stock.")

main()
