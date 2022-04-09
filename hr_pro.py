from datetime import date
from multiprocessing import managers
from select import select

class Employee:
   #Employee class here
   def __init__(self,name, age, salary, employment_year):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year

   def get_working_years(self):
       return date.today().year - int(self.employment_year)

   def __str__(self):
       workingYears = str(self.get_working_years())
       return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {workingYears}"

class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        Employee.__init__(self, name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return float(self.bonus_percentage)*int(self.salary)

    def __str__(self):
       workingYears = str(self.get_working_years())
       bonus = str(self.get_bonus())
       return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {workingYears} Bonus: {bonus}"

def print_options():
    print("Options: ")
    print("\t1. Show Employees: ")
    print("\t2. Show Managers: ")
    print("\t3. Add An Employee: ")
    print("\t4. Add A Manager: ")
    print("\t5. Exit: \n")


def main():
	# main code here
    employees = []
    managers = []

    def getEmployees():
        print("-" * 20)
        print("Employees")
        for employee in employees:
            print(employee)
        print("-" * 20)

    def getManagers():
        print("-" * 20)
        print("Managers")
        for manager in managers:
            print(manager)
        print("-" * 20)

    def addNew(type):
        print("-----------------")
        name = input("Name: ")
        age = input("Age: ")
        salary = input("Salary: ")
        workingYears = input("Working Years: ")
        if(type=="employee"):
            employees.append(Employee(name, age, salary, workingYears))
            print("Employee added succesfully!\n")
            return 
        bonus = input("Bonus Percentage: ")
        managers.append(Manager(name, age, salary, workingYears, bonus))
        print("Manager added succesfully!\n")

    print("Welcome to HR Pro 2019")
    while True:
        print_options()

        selections = input("What would you like to do? (choose a number) ")

        match str(selections):
            case "1":
                getEmployees()
            case "2":
                getManagers()
            case "3":
                addNew("employee")
            case "4":
                addNew("manager")
            case "5":
                break
            case _:
                print("-" * 20)
                print("Please choose from the list")
                print("-" * 20)
        if(selections == 5):
            break        



if __name__ == '__main__':
	main()
