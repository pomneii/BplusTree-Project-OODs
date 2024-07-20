
"""

    โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน 
    โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ 
    แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด

    ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ

"""

print("*** Election ***")
voters = (input('Enter a number of voter(s) : '))
vote_lst = input().split(" ")

counter = 2 
num = []

for number in vote_lst :
    if int(number) <= 0 or int(number) > 20 :
        continue
    current = vote_lst.count(number)
    if current >= counter :
        if current > counter and len(number) != 0 :
            num.pop()
        counter = current
        num.append(number)

if len(num) == 0 :
    print("*** No Candidate Wins ***")
else :
    num = list(set(num))
    num = [int(number) for number in num]
    num.sort()
    for ans in num :
        print(ans, end=' ')

