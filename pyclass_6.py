class employee:
    employee_count= 0
    def __init__(self,firstname,lastname,age,salary):
        self.fn=firstname
        self.ln=lastname
        self.age=age
        self.salary=salary
        self.email=self.fn+"."+self.ln+"@gmail.com"
        employee.employee_count+=1
    def printdetails(self):
        print("employee details")
        print("firstname:{},lastname:{},salary:{},age:{},email:{}",self.fn,self.ln,self.age,self.salary,self.email)

e1=employee("virat","kohli",32,500000)
print("employee dict:",employee.__dict__)
print("e1 dict:",e1.__dict__)