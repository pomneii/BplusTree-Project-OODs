"""
    ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
    1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
    2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

    หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

    การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

    อธิบาย Input
    แบ่ง Data เป็น 2 ชุดด้วย /
        -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
        -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด
"""

class HashTable:
    def __init__(self, size, max_collisions, threshold):
        self.max_collisions = max_collisions
        self.threshold = threshold
        self.table = [None] * size
        self.element_count = 0

    def __len__(self):
        return len(self.table)
    
    def hash_function(self, key):
        return int(key) % len(self.table)
    
    def insert(self, data):
        if (((len(hash_table.table)-(hash_table.table.count(None))) + 1) / len(hash_table.table)) * 100 > threshold :
            print('****** Data over threshold - Rehash !!! ******')
            hash_table.rehashing()

        index = self.hash_function(data)
        collision_count = 0

        while self.table[index] is not None:
            collision_count += 1
            print(f"collision number {collision_count} at {index}")

            if collision_count >= self.max_collisions:
                print("****** Max collision - Rehash !!! ******")
                self.rehashing()
                self.element_count += 1
                return self.insert(data)

            index = (self.hash_function(data) + (collision_count ** 2)) % len(self)

        self.table[index] = data
        self.element_count += 1
    
    def find_next_prime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prime = n
        while not is_prime(prime):
            prime += 1

        return prime

    def rehashing(self):
        new_size = self.find_next_prime(len(self) * 2)
        old_table = self.table[::-1]
        self.size = new_size
        self.table = [None] * new_size
        self.element_count = 0

        for element in old_table:
            if element is not None:
                self.insert(element)
    
    def display(self):
        for i in range(len(self.table)):
            if self.table[i] is None:
                print(f"#{i+1}\tNone")
            else:
                print(f"#{i+1}\t{self.table[i]}")
        print("----------------------------------------")

print(" ***** Rehashing *****")

input_data = input("Enter Input : ")
left, right = input_data.split("/")
table_size, max_collisions, threshold = map(int, left.split())
data = list(map(int, right.split()))

hash_table = HashTable(table_size, max_collisions, threshold)
print("Initial Table :")
hash_table.display()
for item in data:
      print(f"Add : {item}")
      hash_table.insert(item)
      hash_table.display()