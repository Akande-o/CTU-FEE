# Python program processing 
# global vs local variable
 
count = 5
def some_method(): 
    count = 10
    print(count) 
    return 
 
some_method() 
print(count)