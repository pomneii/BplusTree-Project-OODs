"""
    รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง
    ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import***
    Enter Input : 4 3 2 1
    1 step : [3, 2, 1, 4] move[4]
    2 step : [2, 1, 3, 4] move[3]
    last step : [1, 2, 3, 4] move[2]

    Enter Input : 3 2 1 5 6 7
    1 step : [2, 1, 3, 5, 6, 7] move[3]
    2 step : [1, 2, 3, 5, 6, 7] move[2]
    last step : [1, 2, 3, 5, 6, 7] move[None]

    Enter Input : 1 2 3 4 5
    last step : [1, 2, 3, 4, 5] move[None]

    Enter Input : 5 3 1 9 8 2 4 7
    1 step : [3, 1, 5, 8, 2, 4, 7, 9] move[9]
    2 step : [1, 3, 5, 2, 4, 7, 8, 9] move[8]
    3 step : [1, 3, 2, 4, 5, 7, 8, 9] move[5]
    4 step : [1, 2, 3, 4, 5, 7, 8, 9] move[3]
    last step : [1, 2, 3, 4, 5, 7, 8, 9] move[None]

    Enter Input : 5 6 7 8 4 3 2 1 9 25
    1 step : [5, 6, 7, 4, 3, 2, 1, 8, 9, 25] move[8]
    2 step : [5, 6, 4, 3, 2, 1, 7, 8, 9, 25] move[7]
    3 step : [5, 4, 3, 2, 1, 6, 7, 8, 9, 25] move[6]
    4 step : [4, 3, 2, 1, 5, 6, 7, 8, 9, 25] move[5]
    5 step : [3, 2, 1, 4, 5, 6, 7, 8, 9, 25] move[4]
    6 step : [2, 1, 3, 4, 5, 6, 7, 8, 9, 25] move[3]
    7 step : [1, 2, 3, 4, 5, 6, 7, 8, 9, 25] move[2]
    last step : [1, 2, 3, 4, 5, 6, 7, 8, 9, 25] move[None]
"""

def bubbleSort(lst) :
    lst = list(map(int, lst))
    swapped = True
    step = 0

    for last in range(len(lst) - 1, 0, -1) :
        swapped = False
        step += 1
        move = None

        for i in range(last) :
            if lst[i] > lst[i + 1] :
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                move = lst[i + 1]
        
        if not swapped or step == len(lst) - 1 :
            print(f"last step : {lst} move[{move}]")
            break
        else :
            print(f"{step} step : {lst} move[{move}]")
        
inp = input("Enter Input : ").split(' ')
bubbleSort(inp)
