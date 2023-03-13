class Fraction:
    """A class consisting of operations that can be done on a fraction"""
    def __init__(self, numerator, denominator):
        """Initializing the numerator and denominator of the fraction
        Parameters:
        numerator - the top value in a fraction
        denominator - the bottom value in a fraction
        The function raises an error when denominator is zero
        """
        self.numerator = numerator # top 
        self.denominator = denominator # bottom
        # the denominator cannot be zero and if it is we raise an error
        if denominator == 0:
            raise ZeroDivisionError ("The denominator cannot be zero in a fraction")

    def __str__(self):
        """The string consisting of the simplified fraction"""
        #First we compute the actual fraction to get the float value
        result = self.numerator/self.denominator
        # The case of which the fraction is an integer we return the integer value of the simple division
        if result == int(result):
            return "{}".format(int(result))
        #The case when the fraction is not an integer but a real number or float
        else:
            top = abs(self.numerator)                # using the absolute value of the numerator
            bottom = abs(self.denominator)           # using the absolute value of the denominator
            
            #iterating through all numbers from 1 to the minimum of absolute values of numerator and denominator
            for n in range(1, min(top,bottom) + 1):  
                if top % n == 0 and bottom % n == 0:   # computing the factors of both numbers
                    com_divisor = n                    # getting the greatest common divisor of the two numbers
            
            frac_num = top/com_divisor                 # computing the numerator to an irreducible number in the fraction
            frac_denum = bottom / com_divisor         # computing the denominator to an irreducible number in the fraction
            
            # the case when both numerator and denominator are negative values
            if self.numerator < 0 and self.denominator < 0:
                return "{}/{}".format(int(frac_num), int(frac_denum)) # minus/minus => plus(positive)
            # the case when only one of the numerator and denominator is a negative value since the first 
            # if statement would be executed so the condition of both being true has been eliminated
            elif self.numerator < 0 or self.denominator < 0:
                return "-{}/{}".format(int(frac_num), int(frac_denum)) # minus/plus => plus/minus => minus(negative)
            # the condition when both numerator and denominator are positive values
            else:
                return "{}/{}".format(int(frac_num), int(frac_denum)) # plus/plus => plus

    # overwriting the arithmetic operations in python for computation of the fraction class
    def __add__(self, other):
        """The function overwrites the addition operator in python and computes the addition of two fraction classes
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        added - the fraction class of the addition of the two fraction class
        """
        new_num = other.denominator * self.numerator + self.denominator * other.numerator
        new_denum = other.denominator * self.denominator
        added = Fraction(new_num, new_denum)
        return added
    def __sub__(self, other):
        """The function overwrites the subtraction operator in python and computes the subtraction of two fraction classes
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        subtracted - the fraction class of the subtraction of the two fraction class
        """
        new_num = other.denominator * self.numerator - self.denominator * other.numerator
        new_denum = other.denominator * self.denominator
        subtracted = Fraction(new_num, new_denum)
        return subtracted
    def __mul__(self, other):
        """The function overwrites the multiplication operator in python and computes the multiplication of two fraction classes
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        multiplied - the fraction class of the multiplication of the two fraction class
        """
        new_num = self.numerator * other.numerator
        new_denum = self.denominator * other.denominator
        multiplied = Fraction(new_num, new_denum)
        return multiplied
    def __truediv__(self, other):
        """The function overwrites the true division operator in python and computes the true division of two fraction classes
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        true_div - the fraction class of the true division of the two fraction class
        """
        new_num = self.numerator * other.denominator
        new_denum = self.denominator * other.numerator
        true_div = Fraction(new_num, new_denum)
        return true_div

    # overwriting the comparison operations in python to confirm some comparisons between two fractions
    def __eq__(self, other):
        """The function overwrites the comparison operation of equality(==) in python to confirm if two fractions are equal
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        True or False - boolean value which tells us if the two vectors are equal or not
        """
        new_frac = self - other
        return new_frac.numerator == 0
    def __lt__(self, other):
        """The function overwrites the comparison operation of less than(<) in python to confirm if
        one fraction (self) is less than another fraction (other) 
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        True or False - boolean value which tells us if the one fraction (self) is less than another fraction (other) or not
        """
        new_frac = self - other 
        if new_frac.denominator > 0:
            return new_frac.numerator < 0
        else:
            return new_frac.numerator > 0
    def __le__(self, other):
        """The function overwrites the comparison operation of less than or equal to(<=) in python to confirm if
        one fraction (self) is less than or equal to another fraction (other) 
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        True or False - boolean value which tells us if the one fraction (self) is less or equal to than another fraction (other) or not
        """
        new_frac = self - other
        if new_frac.denominator > 0:
            return new_frac.numerator <= 0
        else:
            return new_frac.numerator >= 0
    def __gt__(self, other):
        """The function overwrites the comparison operation of greater than(>) in python to confirm if
        one fraction (self) is greater than another fraction (other) 
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        True or False - boolean value which tells us if the one fraction (self) is greater than another fraction (other) or not
        """
        new_frac = self - other
        if new_frac.denominator > 0:
            return new_frac.numerator > 0
        else:
            return new_frac.numerator < 0
    def __ge__(self, other):
        """The function overwrites the comparison operation of greater than or equal to (>=) in python to confirm if
        one fraction (self) is greater than or equal to another fraction (other) 
        Parameters:
        self - the first fraction class
        other - the second fraction class
        Returns:
        True- boolean value which tells us if the one fraction (self) is greater than or equal to another fraction (other)
        False - a boolean value for if it is not greater than or equal to
        """
        new_frac = self - other
        if new_frac.denominator > 0: 
            return new_frac.numerator >= 0
        else:
            return new_frac.numerator <= 0


            

    
f3 = Fraction(8,2)
print(f3)
f4 = Fraction(-2,3)
print(f4)
f6 = Fraction(-2,-3)
print(f6)
f2 = Fraction(12,18)
print(f2)
f1 = Fraction(2,3)
print(f1)
f5 = Fraction(2,-3)
print(f5)
print(Fraction(2,4))
print(f5+f6)
f1 = Fraction(12,18)
f2 = Fraction(4,9)
print("f1 = " + str(f1))
print("f2 = " + str(f2))
print("f1 + f2 = " + str(f1+f2))
print("f1 - f2 = " + str(f1 - f2))
print("f1 * f2 = " + str(f1 * f2))
print("f1 / f2 = " + str(f1 / f2))
print(f1 == f2)
print(f1 < f2)
print(f1 <= f2)
print(f1 > f2)
print(f1 >= f2)


