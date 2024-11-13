import random

# Function to simulate rolling two dice
def roll_dice():
    for roll_number in range(1, 4):  # Roll dice three times
        die1 = random.randint(1, 6)  # First die roll
        die2 = random.randint(1, 6)  # Second die roll
        
        # Print results of each roll
        print(f"Roll {roll_number}: Die 1 = {die1}, Die 2 = {die2}")

# Main code to call the roll_dice function
roll_dice()
