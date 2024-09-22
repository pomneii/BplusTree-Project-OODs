"""
    ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

    ***** อธิบาย Test Case 2:
    Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
    1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
    2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
    3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value
"""

def first_greater_value(key_lst, sorted_lst, low, high) :
    for key in key_lst :
        result = binary_search(sorted_lst, key, low, high)
        if result == -1 :
            print("No First Greater Value")
        else :
            print(sorted_lst[result])

def binary_search(arr, x, low, high):
    ans = -1

    while low <= high :
        mid = (low + high) // 2

        if arr[mid] > x :
            ans = mid        # collect current temp index 
            high = mid - 1   # find in the left for searching value that less than this and greater than x
        else :
            low = mid + 1    # if mid not greater than x -> find the right
        
    return ans

inp, key = input("Enter Input : ").split('/')
inp = [int(e) for e in inp.split(' ')]
key = [int(e) for e in key.split(' ')]
first_greater_value(key, sorted(inp), 0, len(inp) - 1)
