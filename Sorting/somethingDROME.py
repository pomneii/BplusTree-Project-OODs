"""
    รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้
    - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"
    - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"
    - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"
    - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"
    - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"
    - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"
    ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
    
    Enter Input : 1357
    Metadrome

    Enter Input : 12344
    Plaindrome

    Enter Input : 7531
    Katadrome

    Enter Input : 9874441
    Nialpdrome

    Enter Input : 666
    Repdrome

    Enter Input : 1985
    Nondrome
"""

def custome_sort(inp) :
    num_str = str(inp)
    num_list = list(num_str)

    def is_sorted_ascending(lst) :
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
    def is_sorted_descending(lst) :
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    
    def has_duplicate(lst) :
        return len(lst) != len(set(lst))
    
    def all_same(lst) :
        return len(set(lst)) == 1
    
    if all_same(num_list) :
        return f"Repdrome"
    elif is_sorted_ascending(num_list) :
        if has_duplicate(num_list) :
            return f"Plaindrome"
        else :
            return f"Metadrome"
    elif is_sorted_descending(num_list) :
        if has_duplicate(num_list) :
            return f"Nialpdrome"
        else :
            return f"Katadrome"
    else :
        return f"Nondrome"

    
inp = input("Enter Input : ")
print(custome_sort(inp))