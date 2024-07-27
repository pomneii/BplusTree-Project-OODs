
"""
เขียนโปรแกรมสำหรับหา หรม. ของเลข 2 ตัว

****ห้ามใช้คำสั่ง len, for, while, do while หรือ *****
หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว

บทนิยาม
ตัวหารร่วมมาก หรือ ห.ร.ม. (อังกฤษ: greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว
"""

def findGCD(num1, num2) :
    if num2 == 0 and num1 > 0 :
        return num1
    if num2 < 0 :
        num2 = num2 * (-1) 
        
    return findGCD(num2, num1 % num2)
    
def findMinMax(num1, num2) :
    maxNum = num1
    minNum = num2

    if num2 > num1 :
        maxNum, minNum = num2, num1
    
    return minNum, maxNum

num1, num2 = input("Enter Input : ").split(' ')
minNum, maxNum = findMinMax(int(num1), int(num2))
if minNum == 0 and maxNum == 0 :
    print(f"Error! must be not all zero.")
else :
    print(f"The gcd of {maxNum} and {minNum} is : {findGCD(maxNum, minNum)}")

