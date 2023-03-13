def sum_even_numbers(lst):
    sum = 0
    for item in lst:
        if item % 2 == 0:
            sum += item
    return sum
 
if __name__ == "__main__":
    input_list = [9, 1, 0, 2, 8]
    sum_of_list = sum_even_numbers(input_list)
    print(sum_of_list)
x = float(input('Enter a number: '))
y = float(input('Enter a number: '))
 
z = (x+y)/2
print ('The average of the two numbers you have entered is:',z)


# A function to append a list onto itself, with the intention of
# returning a new list, but leaving the input unaltered
def double_list(in_list):
    """Append a list to itself."""
    out_list = list(in_list)
    out_list += in_list
    return out_list
 
# Make a list
my_list = [3, 2, 1]
 
# Double it
my_list_double = double_list(my_list)
 
# Later on in our program, we want a sorted my_list
my_list.sort()
 
# Let's look at my_list:
print('We expect [1, 2, 3]')
print('We get   ', my_list)