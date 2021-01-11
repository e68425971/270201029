class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def Display(self):
        self.information = f"Name : {self.name} \nSalary : {self.salary} "
        return self.information


employee1 = Employee("efe", 4000)
print(employee1.Display())


class Company:
    def __init__(self, employeeList):
        self.employeeList = list(employeeList)

    def newEmployee(self, name, salary):
        self.additionEmployee = name
        self.additionSalary = salary
        self.employeeList += [[self.additionEmployee, self.additionSalary]]

    def AverageSalary(self):
        total = 0
        for salary in self.employeeList:
            total += salary[1]
        average = total / len(self.employeeList)
        self.averageS = average
        return average


object1 = Company([["mert",7000],["genç",4000],["efe",8000]])

print(object1.AverageSalary())
object1.newEmployee("cenk",7000)
print(object1.AverageSalary())