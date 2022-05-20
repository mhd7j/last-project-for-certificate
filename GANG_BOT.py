from random import randint

is_finished = False
tool_board = 10
arz_board = 10
robot_x = 0
robot_y = 0
tool_cell = 5
cell_icon = ("-")
robot_icon = ("X")
hole_icon = ("O")
holes = [(2 , 7) , (8 , 1)]
final_cell = [(9 , 9)]

board = [[cell_icon] * tool_board for m in range(arz_board)]
board[robot_y][robot_x] = robot_icon


for x, y in final_cell:
    board[y][x] = ("#")
for hole_x , hole_y in holes:
    board[hole_y][hole_x] = hole_icon

def make_hole():
    global holes , board
    hole_x = randint(0 , 9)
    hole_y = randint(0 , 9)
    board[hole_y][hole_x] = hole_icon
    holes.append((hole_x , hole_y))

def print_board():
    saghf = cell_icon * ((tool_cell + 1) * tool_board + 1)
    for row in board:
        print(saghf)
        print("|" + "|".join([col.center(tool_cell) for col in row]) + "|")
    print(saghf)

def can_move(new_x , new_y):
    valid_move = True
    if not (0 <= new_x < tool_board):
        print("nemishe")
        valid_move = False
    elif not (0 <= new_y < tool_board):
        print("nemishe")
        valid_move = False
    else:
        valid_move = True
        return valid_move

def move(new_x , new_y):
    global robot_x, robot_y
    board[robot_y][robot_x] = cell_icon
    robot_x , robot_y = new_x , new_y
    board[robot_y][robot_x] = robot_icon

def move_right():
    new_x = robot_x + 1
    new_y = robot_y

    if can_move(new_x , new_y):
        move(new_x , new_y)

def move_left():
    new_x = robot_x -1 
    new_y = robot_y

    if can_move(new_x , new_y):
        move(new_x , new_y)

def move_down():
    new_x = robot_x
    new_y = robot_y + 1

    if can_move(new_x , new_y):
        move(new_x , new_y)

def move_up():
    new_x = robot_x 
    new_y = robot_y - 1

    if can_move(new_x , new_y):
        move(new_x , new_y)

controler = {
    "U": move_up,
    "D": move_down,
    "L": move_left,
    "R": move_right
}
round = 0
while not is_finished:
    print_board()
    jahat = input("kodoom var??? \'(U,D,R,L)\'")
    if jahat == "exit":
        is_finished = True
        continue

    move_function = controler.get(jahat.upper())
    if not move_function:
        print("mojood ni")
        continue

    move_function()
    round += 1
    if round % 3 == 0 :
        make_hole()
    for z , x in holes:
        if robot_x == z and robot_y == x:
            print("dige dire dige dire")
            is_finished = True
    for x , y in final_cell:
        if robot_x == x and robot_y == y:
            print("damet garm")
            is_finished = True



