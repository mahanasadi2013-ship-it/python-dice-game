import random
print("—" * 41)
print("Dice Game")
print("—" * 41)
print("Version 0.0.0.1")
print("—" * 41)
while True:
    user = input("You: ")
    if user == "dice":
        dice = [1, 2, 3, 4, 5, 6]
        print("Dice: ", random.choice(dice))
        print("—" * 41)
