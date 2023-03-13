class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
 
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
 
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
 

 
    
if __name__ == "__main__":
 
    p1 = Person("Jane", "Doe")
    # p2 = Person("Jane", "Doe", 2019) won't work
    p1.printname()
    # p1.welcome() won't work
    s1 = Student("Mike", "Olsen", 2019)
    s1.printname()
    s1.welcome()      