class dailyTaskOne:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def ageInTenYears(self):
        self.age += 10
        print(f"Hi {self.first_name} in 10 years you will be {self.age} years old.")
    
    def ageInTwentyYears(self):
        self.age += 20
        print(f"Hi {self.first_name} in 20 years you will be {self.age} years old.")

    def ageInThirtyYears(self):
        self.age += 30
        print(f"Hi {self.first_name} in 30 years you will be {self.age} years old.")
    
    def ageInFortyYears(self):
        self.age += 40
        print(f"Hi {self.first_name} in 40 years you will be {self.age} years old.")

person = dailyTaskOne(str(input("Enter your first name: ").title()), str(input("Enter your last name: ").title()), int(input("Enter your age: ")))
person.ageInTenYears()
person.ageInTwentyYears()
person.ageInThirtyYears()
person.ageInFortyYears()