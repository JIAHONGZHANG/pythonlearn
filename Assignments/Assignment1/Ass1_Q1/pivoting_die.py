# Insert your code here


def turn_right():
    global shang, xia, zuo, you
    shang, xia, zuo, you = zuo, you, xia, shang
def turn_left():
    global shang, xia, zuo, you
    shang, xia, zuo, you = you, zuo, shang, xia
def turn_forwards():
    global shang, xia, qian, hou
    shang, xia, qian, hou = hou, qian, shang, xia
def turn_backwards():
    global shang, xia, qian, hou
    shang, xia, qian, hou = qian, hou, xia, shang

while 1:
    cell = input ("Enter the desired goal cell number: ")
    shang = 3
    xia = 4
    zuo = 6
    you = 1
    qian = 2
    hou = 5
    turnpoint =[2,3]
    turn_range = 2
    try:
        if int(cell) < 1:
            print("Incorrect value, try again")
            continue
        while turnpoint[-1] < int(cell):
    ##        print(int(turn_range), end = ' ')
            turnpoint.append(turnpoint[-1] + int(turn_range))
            turn_range = turn_range + 0.5
            if turnpoint[-1] > int(cell):
                turnpoint.pop()
                turnpoint.append(int(cell))
                break
            
        need_turn_right = False
        need_turn_backwards = False
        need_turn_left = False
        need_turn_forwards = False
        for i in range(1,int(cell)+1):
            if i in turnpoint:
                turn_point_round = turnpoint.index(i) % 4
                if turn_point_round == 0:
                    need_turn_right = False
                    need_turn_backwards = False
                    need_turn_left = False
                    need_turn_forwards = True
                    turn_right()
    ##                print(i,shang,qian,you)
                if turn_point_round == 1:
                    need_turn_backwards = False
                    need_turn_right = False
                    need_turn_left = True
                    need_turn_forwards = False
                    turn_forwards()
    ##                print(i,shang,qian,you)
                if turn_point_round == 2:
                    need_turn_left = False
                    need_turn_right = False
                    need_turn_forwards = False
                    need_turn_backwards = True
                    turn_left()
    ##                print(i,shang,qian,you)
                if turn_point_round == 3:
                    need_turn_forwards = False
                    need_turn_backwards = False
                    need_turn_left = False
                    need_turn_right = True
                    turn_backwards()
    ##                print(i,shang,qian,you)
            else:
                if need_turn_right == True:
                    turn_right()
    ##                print(i,shang,qian,you)
                if need_turn_left == True:
                    turn_left()
    ##                print(i,shang,qian,you)
                if need_turn_backwards == True:
                    turn_backwards()
    ##                print(i,shang,qian,you)
                if need_turn_forwards == True:
                    turn_forwards()
    ##                print(i,shang,qian,you)

        print(f"On cell {cell}, {shang} is at the top, {qian} at the front, and {you} on the right.")
        break
    except ValueError:
        print("Incorrect value, try again")


