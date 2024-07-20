
"""

    โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

            Speed (km/h)		ระดับพายุ
                0-51.99			Breeze
                52.00-55.99		Depression
                56.00-101.99	        Tropical Storm
                102.00-208.99	        Typhoon
                >= 209			Super Typhoon

    โดยแสดงผลตามตัวอย่างการแสดงผล

"""

print(" *** Wind classification *** ")
wind = float(input("Enter wind speed (km/h) : "))

if wind >= 209 :
    print("Wind classification is Super Typhoon.")
elif 102.00 <= wind <= 208.99 :
    print("Wind classification is Typhoon.")
elif 56.00 <= wind <= 101.99 :
    print("Wind classification is Tropical Storm.")
elif 52.00 <= wind <= 55.99 :
    print("Wind classification is Depression.")
elif 0 <= wind <= 51.99 :
    print("Wind classification is Breeze.")