
"""
    นักสำรวจชื่ออลิซได้เข้ามาผจญภัยในเขาวงกตลึกลับซึ่งถูกสร้างขึ้นโดยนักเวทย์ผู้ชั่วร้าย เขาวงกตนี้ประกอบไปด้วยกำแพงที่ไม่สามารถทะลุผ่านได้ 
    ช่องว่างที่อลิซสามารถเดินทางไปได้ จุดเริ่มต้นที่อลิซเริ่มต้นการผจญภัย และจุดสิ้นสุดที่อลิซต้องไปถึงเพื่อที่จะออกจากเขาวงกตนี้และกลับบ้านได้อย่างปลอดภัย

    อลิซต้องการความช่วยเหลือจากคุณในการค้นหาเส้นทางที่ปลอดภัยจากจุดเริ่มต้นไปยังจุดสิ้นสุด 
    คุณจะต้องสร้างฟังก์ชันที่สามารถตรวจสอบเส้นทางในเขาวงกตและทำเครื่องหมายเส้นทางที่ถูกต้องเพื่อให้อลิซสามารถเดินตามไปได้

    คุณได้รับเขาวงกตที่แสดงเป็นตารางสองมิติ ซึ่งประกอบด้วย:

        ช่องว่าง  (แทนด้วย '.')
        กำแพง   (แทนด้วย '#')
        จุดเริ่มต้น (แทนด้วย 'S')
        จุดสิ้นสุด (แทนด้วย 'E')

    งานของคุณคือการสร้างฟังก์ชันเพื่อหาทุกเส้นทางที่เป็นไปได้จากจุดเริ่มต้นไปยังจุดสิ้นสุด และทำเครื่องหมายเส้นทางที่ถูกต้องในเขาวงกตโดยแทนที่ '.' ด้วย '*'

    กำหนดให้ Input เป็น 2 มิติขั้นด้วย ","
    ตัวอย่าง Input : S#.#,....,#.##,#..E

    Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.
    Separate each row with a comma (,).
    Enter the maze: S#.#,....,#.##,#..E
    Your maze:
    S#.#
    ....
    #.##
    #..E
    Solution found:
    S#.#
    **..
    #*##
    #**E

"""

def printMaze(maze) :
    return '\n'.join([''.join(row) for row in maze])

def findPath(x, y, maze) :

    # Base case
    if x < 0 or y < 0 or x >= len(maze[0]) or y >= len(maze) :
        return False
    if maze[y][x] == "E" :
        return True
    if maze[y][x] != "." and maze[y][x] != "S" :
        return False
    
    temp = maze[y][x]
    maze[y][x] = "o"
    
    # marking
    if findPath(x, y + 1, maze) :     # piority of down is the most
        maze[y][x] = '*'
        return True
    if findPath(x + 1, y, maze) or \
            findPath(x - 1, y, maze) or findPath(x, y - 1, maze):
        maze[y][x] = '*'  # Mark the path with an asterisk
        return True

    maze[y][x] = temp
    return False

def solveMaze(maze) :
    maze = [list(row) for row in maze]
    start = None

    for y in range(len(maze)) :   # row
        for x in range(len(maze[0])) :  # column
            if maze[y][x] == 'S' :
                start = (x, y)
                break 
        if start :
            break
    
    if start and findPath(start[0], start[1], maze) :
        maze[start[1]][start[0]] = 'S'    # remark the start point
        return printMaze(maze)
    else :
        return None
    
print("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.\nSeparate each row with a comma (,).")
inp = input("Enter the maze: ").split(',')
print(f"Your maze:\n{printMaze(inp)}")
result = solveMaze(inp)
if result == None :
    print("No solution found")
else :
    print(f"Solution found:\n{result}")

