"""
    ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

    ***** อธิบาย Input
    1. ด้านซ้าย  จะเป็น list ของ Data
    2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

    def bi_search(l, r, arr, x):
        # Code Here

    inp = input('Enter Input : ').split('/')
    arr, k = list(map(int, inp[0].split())), int(inp[1])
    print(bi_search(0, len(arr) - 1, sorted(arr), k))
"""

def bi_search(low, high, arr, x):
    if high < low :
        return False
    
    mid = (high + low) // 2 

    # if middle value = x
    if arr[mid] == x :
        return True
    elif arr[mid] > x :   
        return bi_search(low, mid - 1, arr, x)  # left subarray
    else :                
        return bi_search(mid + 1, high, arr, x) # right subarray

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))