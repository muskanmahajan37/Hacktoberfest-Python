from abc import ABC, abstractmethod

class Polygon(ABC):

    def noofsides(self):
        pass

class Triangle(Polygon):

    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):

    def noofsides(self):
        print("I have 5 sides")

class Hexagon(Polygon):


    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):

     def noofsides(self):
         print("I have 4 sides")


r1 = Triangle()
r1.noofsides()


m1 = Quadrilateral()
m1.noofsides()


s1 = Pentagon()
s1.noofsides()


t1= Hexagon()
t1.noofsides()

        


        
        





        


        
