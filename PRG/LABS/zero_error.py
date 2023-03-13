import random 
 
def get_inverted(x):
    return 1/x
 
if __name__ == "__main__":
    random.seed(128)
    for _ in range(10):
        value = random.randrange(0,10)
        inv_value = get_inverted(value)
        print("1/{} is {}.".format(value, inv_value))