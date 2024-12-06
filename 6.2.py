# %%

def print_board(board):
    print('\n'.join([''.join([e for e in l]) for l in board]))
    print("-"*10)

data = './data/6.1.txt'
board = []
steps = 0
direction = 0

directions = [
            (-1,0), #up
            (0,1)  , #rigth
            (1,0)  , #down
            (0,-1) , #left 
            ]

for line in open(data,'r'):
    board.append(list(line.strip()))

x_boundary = len(board[0]) - 1
y_boundary = len(board) - 1


for i, line in enumerate(board):    
    if "^" in line:
        position = [i,line.index('^')]

next_step = position
visited = []


while (next_step[1] < x_boundary) and (next_step[1] >= 0) and (next_step[0] < y_boundary) and (next_step[0] >= 0):
        next_step = [position[0] + directions[direction][0] ,  position[1] + directions[direction][1]]
        
        if "#" == board[next_step[0]][next_step[1]]:
            direction = (direction + 1 ) % 4
            next_step = [position[0] + directions[direction][0] ,  position[1] + directions[direction][1]]
        board[next_step[0]][next_step[1]] = "*"        
        position = next_step
        visited.append(next_step)
print(visited)
print(''.join([''.join([e for e in l]) for l in board]).count('*'))

def print_board(board):
    print('\n'.join([''.join([e for e in l]) for l in board]))
    print("-"*10)

def get_board():
    board = []
    for line in open(data,'r'):
        board.append(list(line.strip()))
    return board

def get_initial():
    for i, line in enumerate(board):    
        if "^" in line:
            position_initial = [i,line.index('^')]
    return position_initial, position_initial

def check_loop(board, point, position_initial, x_boundary, y_boundary):
    i,j = point[0], point[1]
    next_step = position_initial
    position = position_initial
    direction = 0
    
    path = []
    loop = False
    tyle = board[i][j]
    
    board[i][j] = '0'
    
    while (next_step[1] < x_boundary) and (next_step[1] >= 0) and (next_step[0] < y_boundary) and (next_step[0] >= 0) and loop == False:
            next_step = [position[0] + directions[direction][0] ,  position[1] + directions[direction][1]]
            
            if ("#" == board[next_step[0]][next_step[1]]) or ("0" == board[next_step[0]][next_step[1]]):
                direction = (direction + 1 ) % 4
                next_step = [position[0] + directions[direction][0] ,  position[1] + directions[direction][1]]
            
            position = next_step
            point = ''.join([str(i) for i in [position[0],position[1],direction]])

            if point in path:
                loop = True  
                board[i][j] = tyle
                return 1         
            else:
                path.append(point)
    board[i][j] = tyle
    
    return 0

data = './data/6.1.txt'

loop_count = 0
direction = 0

directions = [
            (-1,0), #up
            (0,1)  , #rigth
            (1,0)  , #down
            (0,-1) , #left 
            ]

board = get_board()

x_boundary = len(board[0]) - 1
y_boundary = len(board) - 1

position_initial, next_step = get_initial()
for c, point in enumerate(visited):
        print(round(c/len(visited),2)*100)
        loop_count += check_loop(board, point,position_initial, x_boundary, y_boundary)

print(loop_count)

# %%
