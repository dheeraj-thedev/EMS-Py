from com.tb.services.EmployeeServices import EmployeeService

if __name__ == '__main__':
    emps=EmployeeService()
    while True:
        emps.menu()
        userInp = int(input('Please enter the choice from above menu'))
        func= emps.processEmployee(userInp)
        func()