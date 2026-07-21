class findingTheLargestNumber:
    def __init__(self, num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    def compare(self):
        if self.num1 >= self.num2 and self.num1 >= self.num3:
            print(f"{self.num1} is the largest")
        elif self.num2 >= self.num1 and self.num2 >= self.num3:
            print(f"{self.num2} is the largest")
        else:
            print(f"{self.num3} is the largest")
            
find = findingTheLargestNumber(45,125,76)
find.compare()