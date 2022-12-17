class Student:
    def __init__(self,name,math,sci,eng):
        self.myname = name
        self.mymath = math
        self.mysci = sci
        self.myeng = eng

    def ave(self):
        return (self.mymath + self.mysci + self.myeng) /3

    def __str__(self):
        return f"""Name: {self.myname}
Math: {self.mymath}
Science: {self.mysci}
English: {self.myeng}
Average: {round(self.ave(),2)}"""


s2 = Student("Reycarlo", 80, 75, 90)
a = Student.ave(s2)

def test():
    if a <= 74:
        print("Failed")
    else:
        print("Passed")

print(s2)
test()