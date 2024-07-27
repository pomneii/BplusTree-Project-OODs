
"""
    ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
    หา Factorial ของ input ที่รับมา โดยใช้ Recursive
"""

def factorial(num) :
    if num == 0 or num == 1 :
       return 1
    
    if num > 1 :
        return factorial(num - 1) * num 

inp = int(input("Enter Number : "))

print(f"{inp}! = {factorial(inp)}")