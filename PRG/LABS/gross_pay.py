n_hours = int(input("Enter hours: "))
rate = int(input("Rate: "))
pay = n_hours * rate
if n_hours > 40:
    extra_hours = n_hours - 40
    extra_pay = extra_hours * 1.5 * rate
    pay = 40 * rate + extra_pay
print(pay)
