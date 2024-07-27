
"""
    ในยุคสมัยที่กระแสวงการสายมูมาแรงมากแซงทางโค้ง ท่านประธานบริษัทป็อปมู้ด (Pop Mood) ต้องการออกไลน์โปรดักส์ใหม่เป็นสินค้าอาร์ตทอย (Art Toy) 
    ที่กำลังได้รับความนิยมสุดๆ ขายดีเป็นเทน้ำเทท่าจนต้องไปต่อคิวรอกันเลยทีเดียว โดยการเกิดขึ้นของโปร์ดักส์ใหม่นี้ก็เพราะว่าท่านประธานต้องการขยายฐานลูกค้าบุกตลาดผู้ชื่นชอบของสะสมเสริมดวงชะตาชีวิต 
    ซึ่งคุณเจ๊บหัวหน้าฝ่ายโปรดักส์จะต้องไปขูดเพื่อหาตัวเลขศักดิ์สิทธิ์ ณ สถานที่แห่งนึง โอ้ พระเจ้า คุณเจ๊บพบตัวเลขนั้นจริงด้วย คุณเจ๊บต้องออกแบบตัวเลขที่เป็นไปได้ทั้งหมด 
    เพื่อเสนอไปที่ท่านประธานให้เลือกว่าอยากจะทำคอลเลกชันใหม่นี้ด้วยเลขเซตไหนดี คุณเจ๊บค่อนข้างจะเหนื่อยกับงานมากๆ แค่ขูดหาตัวเลขก็หมดพลังจึงได้ขอร้องให้คุณที่เป็นโปรแกรมเมอร์ไฟแรง 
    “ช่วยเขียนโปรแกรมเพื่อแสดงผลคำตอบทั้งหมดที่เป็นไปได้จากเลขโดดให้หน่อย”

    ปล. ใช้ฟังก์ชั่น sort ได้ (ควร)
"""

def sort_lst(lst) :
    for element in lst :
        if not element.isdigit() or len(element) > 1 :
            return None

    def recursion_sort(current, remaining) :
        if current :
            result.append(current)

        for i in range(len(remaining)) :
            recursion_sort(current + remaining[i], remaining[:i] + remaining[i + 1:])

    result = []
    recursion_sort("", lst)
    result = sorted(list(set([int(e) for e in result])))
    return result


inp = input("Enter digits : ").split(' ')

result = sort_lst(inp)
if result == None :
    print("Invalid input")
else :
    print("Output :", result)
