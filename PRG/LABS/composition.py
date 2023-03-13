# a > 20 and at the same time b > 20

# 1st approach NESTED IF

a = 35
b = 5

if a > 20:
    if b > 20:
        print("YES, a and b are greater than 20")
    else:
        print("NO, a is more than 20 but b is not")
else:
    print("a is greater than or equal to 20")
