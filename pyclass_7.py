class employee:
    __employee_count= 0
    def __init__(self,firstname,lastname,age,salary):
        self.fn=firstname
        self.ln=lastname
        self.age=age
        self.salary=salary
        self.email=self.fn+"."+self.ln+"@gmail.com"
        employee.__employee_count+=1
    def getcount(cls):
        return cls.__employee_count
    def printdetails(self):
        print("employee details")
        print("firstname:{},lastname:{},salary:{},age:{},email:{}",self.fn,self.ln,self.age,self.salary,self.email)

e1=employee("virat","kohli",32,500000)
e1.printdetails()
print("employee dict:",employee.__dict__)
print("e1 dict:",e1.__dict__)

e2=employee("ms","d",39,200000)
print("agter msd:",employee.__dict__)
print("get count:",employee.getcount())