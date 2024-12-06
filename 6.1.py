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

while (next_step[1] < x_boundary) and (next_step[1] >= 0) and (next_step[0] < y_boundary) and (next_step[0] >= 0):
        next_step = [position[0] + directions[direction][0] ,  position[1] + directions[direction][1]]
        if "#" == board[next_step[0]][next_step[1]]:
            direction = (direction + 1 ) % 4
            next_step = [position[0] + directions[direction][0] ,  position[1] + directions[direction][1]]
        board[next_step[0]][next_step[1]] = "*"
        position = next_step

print(''.join([''.join([e for e in l]) for l in board]).count('*'))

# %%
