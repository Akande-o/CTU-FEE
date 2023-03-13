#AND
# OR

# WANT: a>20 or b>20 or (a>20 and b>20)
#DON'T WANT: a<=20 AND b<=20

a = 0
b = 20
if a > 20 or b > 20:
    print("At least one of the variables is more than 20")
else:
    print("None of the variables is more than 20")