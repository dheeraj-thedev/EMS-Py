from com.tb.modals.Project import Project

class ReadUtils:
    def readString(self,userMsg,errMsg):
        data=input(userMsg)
        if not str.isalpha(data):#type(data)  is not str:
            print(errMsg)
            self.data=self.readString(userMsg,errMsg)
        return data

    def readProjects(self,useMsg,errMsg):
        listProjects=list()
        ctr=0
        while ctr <3 :
            proj = Project(
                self.readString('Enter the Project Name ','CError Could not read that '),
                self.readDate('Enter the Project Start  Date ','CError Could not read that '),
                self.readDate('Enter the Project End Date  ', 'CError Could not read that ')
            )
            listProjects.append(proj)
            ctr=ctr+1
        return listProjects


    def readDate(self,useMsg,errMsg):
        return input(useMsg)

    def readPhone(self,userMsg,errMsg):
        data = input(userMsg)
        if not str.isdigit(data):  # type(data)  is not str:
            print(errMsg)
            self.data = self.readPhone(userMsg, errMsg)
        return data

    def readInteger(self):
        pass
    def readFloat(self):
        pass

# if __name__ == '__main__':
#     ru=ReadUtils()
#     d= ru.readPhone('Enter The phone in String  ','Could not find relevant please enter String')
#     print(d)