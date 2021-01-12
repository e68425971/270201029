class Employee:
    def __init__(self, name, salary):  # Bunu atamadan set veya get de çalışmıyor
        if (type(name) is str) and (type(salary) is int):
            self.name = name
            self.salary = salary
        else:
            print("Employee didn't assigned. Please try again after checked")

    def Salary(self, salary):
        if salary >= 0:
            self.salary = salary
        else:
            print("Salary can't be less than zero try again")

    def Name(self, name):
        if type(name) is str:
            self.name = name
        else:
            print("Name have to be string try again")

    def SalaryGet(self):
        return self.salary

    def NameGet(self):
        return self.name

    def Information(self):
        self.information = f"Name: {self.name}\n" \
                           f"Salary: {self.salary}"
        print(self.information)


class Company:
    def __init__(self, employeeList):
        self.employeeList = employeeList

    def AddEmployee(self, newEmployee):
        if isinstance(newEmployee, Employee):
            newEmployeeAdd = [newEmployee.NameGet(), newEmployee.SalaryGet()]
            self.employeeList += [newEmployeeAdd]
        else:
            print("New employee didn't assigned, try again")

    def Average(self):
        total = 0
        for innerLists in self.employeeList:
            total += innerLists[1]
        print(round(total / len(self.employeeList)))

    def Display(self):
        for innerlist in self.employeeList:
            print(f"Name:{str(innerlist[0]).title()} Salary: {innerlist[1]}")

    def EmployeeListGet(self):
        return self.employeeList

    def EmployeeListSet(self,newList):
        if type(newList) is list:
            self.employeeList = newList


list = [["gaye", 4000], ["cansu", 3000], ["egemen", 8000]]
NcrTech = Company(list)
Stajyer = Employee("dido", 2300)
NcrTech.AddEmployee(Stajyer)
NcrTech.Display()
NcrTech.Average()
