
"""

    สร้าง class Spherical โดยต้อง
    มี function [changeR , findVolume , findArea]
    มี ตัวแปร radius
    pi = 3.1415926535897932384626433832795028841

    class Spherical:

        def __init__(self,r):

            ### Enter Your Code Here ###

        def changeR(self,Radius):

            ### Enter Your Code Here ###

        def findVolume(self):

            ### Enter Your Code Here ###

        def findArea(self):

            ### Enter Your Code Here ###

        def __str__(self):

            ### Enter Your Code Here ###

    r1, r2 = input("Enter R : ").split()
    R1 = Spherical(int(r1))
    print(type(R1))
    print(dir(R1))
    print(R1)
    R1.changeR(int(r2))
    print(R1)

"""

class Spherical:

    pi = 3.1415926535897932384626433832795028841

    def __init__(self,r1):
        self.radius = r1

    def changeR(self,Radius):

        self.radius = Radius
        return self.radius

    def findVolume(self):
        volume = 4/3 * Spherical.pi * (self.radius ** 3)
        return volume

    def findArea(self):

        area = 4 * Spherical.pi * (self.radius ** 2)
        return area

    def __str__(self):

        print("Radius =", self.radius, end=' ', sep='')
        print("Volumn =", R1.findVolume(), end=' ')
        print("Area =", R1.findArea(), end='\n')

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))

R1.__str__()

R1.changeR(int(r2))

R1.__str__()