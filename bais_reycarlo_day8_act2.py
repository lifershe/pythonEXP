class Employee:
    def __init__(self, name, email, mobile):
        self.myname = name
        self.myemail = email
        self.mymobile = mobile
    def __str__(self):
        return f"""Employee: {self.myname}
Email: {self.myemail}
Mobile #: {self.mymobile}"""

emp1 = Employee("Reycarlo Bais", "reycarlo@gmail.com","0966123456")
emp2 = Employee("Lebron James","lb@hotmail.com","+9874562100")
print(emp1)
print("\nEmployee: "+emp2.myname)
print("Email: "+emp2.myemail)
print("Mobile #: "+emp2.mymobile)