
"""
    สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด ให้ return list 
    ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)

    def num_grid(lst):

        #Code Here

        return lst

    '''lst_input = [

        ["-","-","-","-","-"],

        ["-","-","-","-","-"],

        ["-","-","#","-","-"],

        ["-","-","-","-","-"],

        ["-","-","-","-","-"]

    ]'''

    lst_input = []

    input_list = input().split(",")

    for e in input_list:

    lst_input.append([i for i in e.split()])

    print("\n",*lst_input,sep = "\n")

    print("\n",*num_grid(lst_input),sep = "\n")

"""

def num_grid(lst):

    rows = len(lst)
    if rows > 1 :
        cols = len(lst[0])
    else :
        cols = 0

    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
               # left-up | up | right-up | left | right | left-down | down | right-down

    result = []

    for i in range(rows) :
        row = []
        for j in range(cols) :
            if lst[i][j] == "-" :
                count_mines = 0
                for x, y in directions :
                    m, n = i + x, j + y
                    if 0 <= m < rows and 0 <= n < cols and lst[m][n] == "#" :
                        count_mines += 1
                row.append(str(count_mines))
            else :
                row.append("#")
        
        result.append(row)

    return result

print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")
lst_input = []

for e in input_list:

    lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")