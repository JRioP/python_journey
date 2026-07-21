class taxCalculator:
    def __init__(self, income):
        self.income = income
    
    def calculate_tax(self):
        if self.income <= 85528:
            tax = self.income * 0.18 - 556.02
        else:
            tax = 14839.02 + (self.income - 85528) * 0.32
        return round(tax, 0)

calculator = taxCalculator(float(input("Enter your income: ")))

print(f"Your tax is: {calculator.calculate_tax():.2f} PLN")