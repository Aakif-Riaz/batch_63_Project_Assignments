def rolldice():

    import random

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"First dice roll result: {dice1}")
    print(f"Second dice roll result: {dice2}")

    total = dice1 + dice2

    print(f"Adding both dice rolls results: {total}")

rolldice()