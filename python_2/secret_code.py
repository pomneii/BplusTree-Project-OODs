
"""

    ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
    โดยรหัสจะประกอบไปด้วย english word that have repeat character
    เช่น bon("ball") = 48 หรือ bon("aah") = 4

    def bon(w):
        ### Enter Your Code Here ###
    secretCode = input("Enter secret code : ")
    print(bon(secretCode))

"""

def bon(w):

    repeat_char = None

    for chars in w :
        if w.count(chars) > 1 :
            repeat_char = chars

    result = 4 * (ord(repeat_char) - 96)

    return result

secretCode = input("Enter secret code : ")
print(bon(secretCode))