class ReadUtils:
    def readString(self,userMsg,errMsg):
        data=input(userMsg)
        if not str.isalpha(data):#type(data)  is not str:
            print(errMsg)
            self.data=self.readString(userMsg,errMsg)
        return data
    
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