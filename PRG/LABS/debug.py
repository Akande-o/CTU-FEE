def add_gold(inv, inc_gold):
    inv["gold"] += inc_gold
 
if __name__ == "__main__":
    inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    }
 
 
    add_gold(inventory, 50)
    print(inventory)