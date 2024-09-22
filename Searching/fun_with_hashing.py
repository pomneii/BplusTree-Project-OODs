"""
    ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

    1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
    2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
    3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
    4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

    อธิบาย Input
    แบ่ง Data เป็น 2 ชุดด้วย /
        -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
        -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ

    class Data:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __str__(self):
            return "({0}, {1})".format(self.key, self.value)

    class hash:

        # Code Here
"""

class Data :
    def __init__(self, key, value) :
        self.key = key
        self.value = value

    def __str__(self) :
        return "({0}, {1})".format(self.key, self.value)

class HashTable :
    def __init__(self, size, max_collision) :
        self.size = size
        self.max_collison = max_collision
        self.table = [None] * size
        self.is_full_msg_shown = False          # for show message in one time
        self.is_full = False                    # table is full or not
    
    def hash_function(self, key) :
        return sum(ord(c) for c in key) % self.size
    
    def insert(self, data) :

        if self.is_full_msg_shown :
            return
        
        if self.is_full :
            print("This table is full !!!!!!")
            self.is_full_msg_shown = True
            return
        
        key = data.key
        index = self.hash_function(key)
        collision_count = 0

        while self.table[index] != None :
            print(f"collision number {collision_count + 1} at {index}")
            collision_count += 1
            if collision_count >= self.max_collison :
                print("Max of collisionChain")
                self.display()
                return
            index = (self.hash_function(key) + (collision_count ** 2)) % self.size

        self.table[index] = data 

        if all(self.table) :     # table is full
            if not self.is_full :
                self.is_full = True
        
        self.display()
    
    def display(self) :
        for i in range(self.size) :
            print(f"#{i + 1}	{self.table[i]}")
        print("-" * 27)

print(" ***** Fun with hashing *****")
# Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
left, right = input("Enter Input : ").split('/')
size, max_collision = map(int, left.split())
right = right.split(',')
hash_table = HashTable(size, max_collision)
for element in right :
    key, value = element.split(" ")
    data = Data(key, value)
    hash_table.insert(data)