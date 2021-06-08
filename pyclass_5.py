class Investment:
    def __init__(self,amount,roi,type):
        self.amount=amount
        self.roi=roi
        self.type=type

    def yearstodouble(self):
        try:
            return 72/self.roi
        except ZeroDivisionError:
            return "invalid roi"
        except ValueError:
            return "invalid roi"


i1=Investment(1000,10,"stock")
print("years to double i1:",i1.yearstodouble())


i2=Investment(10000,8,"savings")
print("years to double i2:",i2.yearstodouble())