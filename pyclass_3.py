class Employee:
    '''
      help: class is an object which can manage anf create the emlopyee data
      and pocesses of name ,age ,place etc
      '''

    def __init__(self,firstname,lastname):
        print("the value of self:",self)
        self.fn=firstname
        self.ln=lastname



e1=Employee("vorat","kohli")
e2=Employee("rohit","sharma")
print(e1)
print(e2)

print("e1 dict",e1.__dict__)
print("e2 dict",e2.__dict__)
print("Employee dict",Employee.__dict__)
