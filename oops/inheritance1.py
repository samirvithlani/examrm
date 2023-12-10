#there are 5 types of inheritance
#1.single inheritance 1 --> 1 child
#2.multiple inheritance : --> 1 parent many child    many parent can have same child
#3.multilevel inheritance
#4.hierarchical inheritance
#5.hybrid inheritance


class Vehicle:
    
    name = ""
    noOfSeats = 0
    
    def vehTest(self):
        print("This is a vehicle")



class Car(Vehicle):
    
    def getCarData(self):
        self.name = input("Enter car name")
        self.noOfSeats = int(input("Enter no of seats"))      
   
    def showCarData(self):
        print("Car name is", self.name)
        print("No of seats is", self.noOfSeats)


class Bus(Vehicle):
    
    def getBusData(self):
        self.name = input("Enter bus name")
        self.noOfSeats = int(input("Enter no of seats"))      
   
    def showBusData(self):
        print("Bus name is", self.name)
        print("No of seats is", self.noOfSeats)

c = Car()
c.getCarData()
c.showCarData()
               