class Employee (object):
    tempID=0
    projects=[]
    def __init__(self,name ,email, age , contact, salary,project):
        self.name = name
        self.age = age
        self.email=email
        self.contact = contact
        self.salary = salary
        Employee.tempID = Employee.tempID+1
        self.Id = Employee.tempID
        self.projects.append(project)

    def __str__(self):
        return  "Id : {}\nName : {}\nEmail:{} \nAge : {}  \nContact {} \nSalary : {}".format(
            self.Id,
            self.name,
            self.email,
            self.age,
            self.contact,
            self.salary
        )

    def __repr__(self):
        return "{},{},{},{},{},{},{}".format(
            self.Id,
            self.name,
            self.email,
            self.age,
            self.contact,
            self.salary,
            self.projects,
            '\n'
        )
