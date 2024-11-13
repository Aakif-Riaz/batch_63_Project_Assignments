count_dict = {}

while True:
    num = input("Enter a number (or press Enter to stop): ")
    
    if num == "":
        break
    
    num = int(num)
    
    if num in count_dict:
        count_dict[num] += 1

    else:
        count_dict[num] = 1

for number, count in count_dict.items():
    print(f"{number} appears {count} times.")
