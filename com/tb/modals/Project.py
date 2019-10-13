class Project :
    tempid=0
    def __init__(self, name , startdate ,enddate):
        Project.tempid+=1
        self.id= Project.tempid
        self.name = name
        self.startdate= startdate
        self.enddate=enddate

    def __str__(self):
        return "ID : {}\nName : {}\nStartDate : {}\nEndDate : {}".format(
            self.id,
            self.name,
            self.startdate,
            self.enddate
        )

