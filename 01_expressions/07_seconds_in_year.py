def sec_in_year():

    years = int(input("Number of Years: "))

    sec_in_year = 365 * 24 * 60 * 60

    result = years * sec_in_year

    print(f"There are {result} seconds in {years} years.")

sec_in_year()