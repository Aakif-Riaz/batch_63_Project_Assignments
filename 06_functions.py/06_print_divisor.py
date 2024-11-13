def divisor():
    num = int(input("Enter number: "))

    divisors = []
    from itertools import count
    
    for i in count(1):
        if i > num :
            break

        if num % i == 0:
            divisors.append(i)
        
    print(divisors)

divisor()