from numba.cuda import selp

from com.tb.modals.Employee import Employee

class FileUtils:
    def saveToFile(self,path,emp):
        with open(path,'a') as file:
            file.write(emp.__repr__())
        file.close()
        return "Done With  {}".format(emp)
    employees=[]
    def readFile(self,path):
        with open(path,'r')  as file:
            lines=file.readlines()
            for line in lines:
                l = line.split(',')
                e=Employee(
                    name=l[1],
                    email=l[2],
                    age=int(l[3]),
                    contact=l[4],
                    salary=int(l[5]),
                    project='dhjjdsjdhsjhd'
                )
                e.Id=l[0]
                self.employees.append(e)
        return self.employees
#
# if __name__ == '__main__':
#     emp=FileUtils().readFile('d:\\aaa.csv')
#     for e in emp:
#         print(e)
#
# # if __name__ == '__main__':
# #     emp = Employee(
# #         name='fjkdjfkdsjf',
# #         age=65,
# #         contact='47837483',
# #         salary=6643,
# #         email='bond@gmail.com',
# #         project='fjdfkdjfksdjs'
# #     )
# #     FileUtils().saveToFile('d:\\aaa.csv',emp)