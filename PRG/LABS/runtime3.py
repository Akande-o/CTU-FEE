def div_numbers(a, b):
    return a / b
 
if __name__ == "__main__":
    nr_1 = float(input("Enter first number: "))
    nr_2 = float(input("Enter second number: "))
    sum = div_numbers(nr_1, nr_2)
    print("Quotient = " + str(sum))