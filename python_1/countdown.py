
"""

    อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ

    โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

"""

"""
*** Fun with countdown ***
Enter List : 4 8 3 2 1 2
[1, [[3, 2, 1]]]
"""

print("*** Fun with countdown ***")
input_lst = input("Enter List : ").split(' ')
input_lst = [int(e) for e in input_lst]

temp_lst = []
for i in range(len(input_lst)) :
    if input_lst[i-1] - 1 == input_lst[i] :
        temp_lst.append(input_lst[i-1])
        if input_lst[i-1] == 2 :
            temp_lst.append(input_lst[i])
    elif input_lst[i-1] - input_lst[i] == 0 :
        temp_lst.append(input_lst[i-1])

result = []
check_lst = []
for num in temp_lst :
    if num != 1 :
        check_lst.append(num)
    elif num == 1 :
        check_lst.append(num)
        result.append(check_lst)
        check_lst = []

for i in range(len(result)) :
    result[i] = sorted(list(set(result[i])), reverse=True)

result = [len(result), result]

print(result)