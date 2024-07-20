
"""

จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

"""

def find_sum(lst) :

    target_sum = 5
    result = []

    if len(lst) <= 2 :
        return "Array Input Length Must More Than 2"
    
    for i in range(len(lst) - 2) :
        for j in range(i + 1, len(lst) - 1) :
            for k in range(j + 1, len(lst)) :
                if lst[i] + lst[j] + lst[k] == target_sum :
                    if list(sorted([lst[i], lst[j], lst[k]])) not in result :
                        result.append(list(sorted([lst[i], lst[j], lst[k]])))

    return result

input_lst = input("Enter Your List : ").split(' ')
input_lst = [int(e) for e in input_lst]
result = find_sum(input_lst)
print(result)
