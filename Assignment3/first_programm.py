#Student ID: 700757140
#       CRN :23476

#Question 1

class Employee:
    countofNoEmp = 0  #help in the count of employees

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.countofNoEmp += 1  #  the employees count is incremented

    @staticmethod
    def average_salary(employees):
        total_salary = sum(employee.salary for employee in employees)
        return total_salary /len(employees)

class FulltimeEmployee(Employee):
    pass


e1 = Employee("Prasanna", "Prasanna Family",87, "Food")
e2 = Employee("kushi", "kushi  Family", 75, "business")


fulltime_e1 = FulltimeEmployee("Amara", "Amara's Family", 88, "Farming")
fulltime_e2 = FulltimeEmployee("sai", "sai's Family", 78, "Fancy")


employees = [e1, e2, fulltime_e1, fulltime_e2]
avg_sal = Employee.average_salary(employees)

print("Count of Number of Employees:", Employee.countofNoEmp)
print("Average Salary of a Employee:", avg_sal)