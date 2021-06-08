class Student:
    def __init__(self,name):
        self.name=name
        self.grades=[]
    def addgrade(self,grade):
        self.grades.append(grade)

    def getaverrage(self):
        if len(self.grades):
            return sum(self.grades) / len(self.grades)
        else:
             return 'empty'



s1=Student("viarat")
s2=Student("ms dhoni")
print("s1 dict:",s1.__dict__)
s1.addgrade(10)
s1.addgrade(20)
print("aftewr addinf grades:",s1.__dict__)
print("aftewr addinf grades:",s2.__dict__)
print("aerarge:",s1.getaverrage())
print("aerarge:",s2.getaverrage())