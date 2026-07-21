class employee:
    def __init__(self, firstname, lastname, department):
        self.firstname = firstname
        self.lastname = lastname
        self.department = department

    def print_badge(self):
        print("[ID Badge] \nFirst Name:", self.firstname ,"\nLast Name: ", self.lastname , "\nDepartment:", self.department ,"\n")

new_employee = employee("Joshua","Rio", "IT Department")
new_employee.print_badge()

new_employee2 = employee("Jane","Doe", "HR Department")
new_employee2.print_badge()