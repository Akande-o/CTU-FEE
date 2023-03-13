import random
rng = random.Random()
for i in range(1, 6001):
    dice = rng.randrange(1, 7)
    print(i, dice)
