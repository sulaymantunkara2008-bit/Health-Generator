def Health(dice_one, dice_two):
    Health = dice_one * dice_two
    return Health

print("🏹CHARACTER STATS GENERATOR🏹")

for i in range(3):
    print("")
    import random
    Name = input("Enter your name: ")
    six_side = random.randint(1, 6)
    eight_side = random.randint(1, 8)
    print("Their health is", "\033[33m", Health(six_side, eight_side), "hp.", "\033[0m")
    



