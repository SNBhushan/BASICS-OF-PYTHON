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
# sub class / inherited / subclass / child
class develpoer(employee):
    def __init__(self,fn,ln,adr,salary,prolong):
        super().__init__(fn,ln,adr,salary,prolong)
        self.prolong=prolong
    def printdetails(self):
        super().printdetails()
        print("langyage",self.prolong)

    pass
class gandu(employee):
    pass
e1 = employee("virat", "kohli", 32, 500000)
print(e1.__dict__)

e2=develpoer("ms","d",39,200000,"python")
print("agter msd:",e2 .__dict__)