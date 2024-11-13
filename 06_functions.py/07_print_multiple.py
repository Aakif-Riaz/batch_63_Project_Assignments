def print_multiple():
    message = input("Enter the message: ")
    repetition_count = int(input("Enter the count of the message: "))

    print(repetition_count, repetition_count * (message + " "))

print_multiple()