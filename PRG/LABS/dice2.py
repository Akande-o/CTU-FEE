import random

rng = random.Random()

count = [0, 0, 0, 0, 0, 0]
for i in range(6000):
    dice_throw = rng.randrange(1,7)
    count[dice_throw - 1] += 1
print(count)