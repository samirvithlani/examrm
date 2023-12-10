class Bank:
    a = 10
    def bankData(self):
        print("This is a bank")

class Govt:
    a = 20
    def govtData(self):
        print("This is a govt")
        
        


class RBI( Govt,Bank):
    def rbiData(self):
        print(self.a)
        print("This is a RBI")


r = RBI()
r.rbiData()  