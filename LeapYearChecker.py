class CheckingOfYears:
    def __init__(self, year):
        self.year = year
    
    def year_kind(self):
        if self.year < 1582:
            print("Not within the Gregorian calendar period")
        elif self.year % 4 != 0:
            print("Common Year")
        elif self.year % 100 != 0:
            print("Leap Year")
        elif self.year % 400 != 0:
            print("Common Year")
        else:
            print("Leap Year")
    
year_check = CheckingOfYears(2024)

year_check.year_kind()