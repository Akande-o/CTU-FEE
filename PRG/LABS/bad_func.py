# local function shadowing a built-in one.
# REALLY BAD PRACTICE
# You should NEVER shadow a built-in function.
 
def abs(val):
    print("My abs() function")
    if  val >= 0:
        return val
    else:
        return -val
 
 
print(abs(-5))