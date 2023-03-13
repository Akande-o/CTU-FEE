mytuple = ("apple", "banana", "cherry")
# create an iterator object from that iterable
myit = iter(mytuple)
 
# infinite loop
while True:
    try:
        # get the next item
        element = next(myit)
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
for x in mytuple:
    print(x)