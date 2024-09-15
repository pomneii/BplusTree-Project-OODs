"""
    ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน
    ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

    Enter Input : 6 3 -2 5 -8 2 -2
    2 3 -2 5 -8 6 -2    

    Enter Input : 6 5 4 -1 3 0 2 -99 1
    0 1 2 -1 3 4 5 -99 6
"""

def bubble_sort(lst) :
    n = len(lst)
    for step in range(n - 1):
        swapped = False
        for j in range(n - 1 - step):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j] 
                swapped = True

        # if there is no swap in the lst = finish
        if not swapped :
            break

def custom_sort(input_lst) :

    # seperate positive number from input_lst
    positives = [x for x in input_lst if x >= 0]

    # sort positive list
    bubble_sort(positives)

    result = []
    pos_index = 0

    for element in input_lst :
        if element < 0 :
            result.append(element)
        else :
            # append the sort positive list in the result
            result.append(positives[pos_index])
            pos_index += 1
    
    return result

input_lst = input("Enter Input : ").split(' ')
input_lst = list(map(int, input_lst))
sorted_lst = custom_sort(input_lst)
print(" ".join(map(str, sorted_lst)))
