def leap_year():
    year = int(input("Enter year: "))

    if year >= 1583:  # Gregorian calendar started in 1582
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        elif year % 100 == 0:
            print(f"{year} is not a leap year.")
        elif year % 4 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print("Year should be 1583 or later, as the Gregorian calendar started from 1582.")

leap_year()
