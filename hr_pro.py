print("Welcome to HR Pro 2019")
def options():
    print("""1. Show Employees
2. Show Managers
3. Add Employee
4. Add Manager
5. Exit""")
    print()
options()
class Employee:
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        today = 2020
        years =  today - int(self.employment_year)
        return years
    def __str__(self):
        return "Name: %s, Age: %d, Salary: %d, Working Years: %d" % (self.name,int(self.age), int(self.salary), self.get_working_years())
class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name,age,salary,employment_year)
        self.bonus_percentage = bonus_percentage
    def get_bonus(self):
        return float(self.bonus_percentage) * int(self.salary)
    def __str__(self):
        return "Name: %s, Age: %d, Salary: %d, Working Years: %d, Bonus: %f" % (self.name,self.age,self.salary,self.get_working_years(),self.get_bonus())
employees = []
managers = []
option = int(input("What would you like to do? "))
while option != 5:
    if option == 1:
        for employee in employees:
            print(employee)
        options()
        option = int(input("What would you like to do? "))
    elif option == 2 :
        for manager in managers:
            print(manager)
        options()
        option = int(input("What would you like to do? "))
    elif option == 3:
        name= input("Name: ")
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        employment = (int(input("Employment Year: ")))
        employee = Employee(name,age,salary,employment)
        employees.append(employee)
        options()
        option = int(input("What would you like to do? "))
    elif option == 4:
        name= input("Name: ")
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        employment = (int(input("Employment Year: ")))
        bonus = float(input("Bonus Percentage: "))
        manager = Manager(name,age,salary,employment,bonus)
        managers.append(manager)
        options()
        option = int(input("What would you like to do? "))
