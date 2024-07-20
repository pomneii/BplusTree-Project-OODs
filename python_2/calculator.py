
"""

    จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)

    class Calculator :

        ### Enter Your Code Here ###

        def __add__(self):

            ###Enter Your Code For Add Number###

        def __sub__(self):

            ###Enter Your Code For Sub Number### 

        def __mul__(self):

            ###Enter Your Code For Mul Number###

        def __truediv__(self):

            ###Enter Your Code For Div Number###

    x,y = input("Enter num1 num2 : ").split(",")

    x,y = Calculator(int(x)),Calculator(int(y))

    print(x+y,x-y,x*y,x/y,sep = "\n")

"""

class Calculator :

    def __init__(self, a, b):
        self.__num1 = a
        self.__num2 = b

    def __add__(self):
        result = self.__num1 + self.__num2
        return result

    def __sub__(self):
        result = self.__num1 - self.__num2
        return result

    def __mul__(self):
        result = self.__num1 * self.__num2
        return result

    def __truediv__(self):
        result = self.__num1 / self.__num2
        return result

x,y = input("Enter num1 num2 : ").split(",")

cal = Calculator(int(x), int(y))

print(cal.__add__(), cal.__sub__(), cal.__mul__(), cal.__truediv__(), sep='\n')