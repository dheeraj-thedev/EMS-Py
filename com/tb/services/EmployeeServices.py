from com.tb.modals.Employee import Employee
from com.tb.utils.readutils import ReadUtils
from com.tb.utils.fileutils import FileUtils
from com.tb.services.EmailServicesGoogle import GmailMailer
class EmployeeService:
    employees = list()
    fileLocation='d:\\aaa.csv'

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
        self.rUtils =  ReadUtils()
        self.fUtils= FileUtils()
        self.employees= self.fUtils.readFile(self.fileLocation)

    def addEmployee(self):
        emp = Employee(
            name=self.rUtils.readString('Enter the name in String ','Could not resolve input as String'),
            contact=self.rUtils.readPhone('Enter the Contact Number in Numeric ','Could not resolve input as numberic'),
            age=int(input("Enter the age")),
            email=input('Enter the Email address'),
            salary=input('Enter the salary'),
            project=self.rUtils.readProjects('Emter the project details ',"could not read  those")
            )
        GmailMailer().sendMail(emailAddress=emp.email,subject='Email Notification of '+str(emp.tempID),body=emp.__str__())
        self.employees.append(emp)

    def showAllEmployee(self):
        for emp in self.employees:
            print(emp)

    def showEmployeeByName(self):
        empName = input('Please enter the name looking for ').strip()
        for emp in self.employees:
            if str(emp.name).lower() == empName.lower():
                print(emp)

    def processEmployee(self, case):
        switcher = {
            1: self.addEmployee,
            2: self.showAllEmployee,
            3: self.showEmployeeByName,
            4: self.showEmployeeBySalary,
            5: self.saveToFile
        }
        return switcher.get(case, 'Can not process request as does not exist')

    def showEmployeeBySalary(self):
        pass

    def saveToFile(self):
        for emp in self.employees:
            status=self.fUtils.saveToFile(self.fileLocation,emp)
        print(status)

