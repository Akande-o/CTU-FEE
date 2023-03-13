def sum_numbers(a, b):
    return a + b
 
if __name__ == "__main__":
    nr_1 = 8
    nr_2 = 10
    nr_3 = -6
    s = sum_numbers(nr_1, nr_2)
    sum = sum_numbers(s, nr_3)
    print("sum = ", sum)