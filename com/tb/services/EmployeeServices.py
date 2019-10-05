from com.tb.modals.Employee import Employee
class EmployeeService:
    employees = list()

    def menu(self):
        print('---MAIN MENU---')
        print('1. To add an Employee')
        print('2. To show All Employees')
        print('3. To Search Employee by Name')
        print('4. To Search Employee by project')
        print('5. To save to csv')
        print('5. max Salary')

    def saveData(self):
        pass
    def __init__(self):
        # to load data from file ad populate employees list thiss has to be called everytime
        pass

    def addEmployee(self):
        emp = Employee(name=input('Enter the name'),
                       contact=input('Enter the contact number'),
                    age=int(input("Enter the age")),
                        email=input('Enter the Email address'),
                        salary=input('Enter the salary'),
                        project=list(input('Please enter  the project'))
                    )
        self.employees.append(emp)

    def showAllEmployee(self):
        for emp in self.employees:
            print(emp)

    def showEmployeeByName(self):
        empName = input('Please enter the name looking for ').strip()
        for emp in self.employees:
            if str(emp.name).lower() == empName.lower():
                print(emp)

    def showEmployeeBySalary(self):
        pass

    def processEmployee(self, case):
        switcher = {
            1: self.addEmployee,
            2: self.showAllEmployee,
            3: self.showEmployeeByName,
            4: self.showEmployeeBySalary
        }
        return switcher.get(case, 'Can not process request as does not exist')
