
"""

    ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function

    ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1

    ถ้าหากเป็น 2 argument -> range(a, b)         | start = a , end = b , step = 1

    ถ้าหากเป็น 3 argument -> range(a, b, c)      | start = a , end = b , step = c

"""

def new_range(lst) :
    result = []
    if len(lst) == 1 :
        start, end, step = 0, lst[0], 1
    elif len(lst) == 2 :
        start, end, step = lst[0], lst[1], 1
    elif len(lst) == 3 :
        start, end, step = lst[0], lst[1], lst[2]

    current = start
    while (step > 0 and current < end) :
        result.append(current)
        current += step

    result = tuple([round(float(e), 3) for e in result])
    return result

print("*** New Range ***")
input_lst = input("Enter Input : ").split(' ')
input_lst = [float(e) for e in input_lst]
result = new_range(input_lst)
print(result)