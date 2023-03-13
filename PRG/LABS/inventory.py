inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['pocket'] = ["seashell", "strange berry", "lint"]
print(inventory)

inventory["backpack"].sort()
# new_sorted_list = sorted(list)- does not change list and returns a new list
# list.sort() - does not return anything
print(inventory)
inventory["backpack"].remove("dagger")
print(inventory)

inventory["gold"] += 50
print(inventory)