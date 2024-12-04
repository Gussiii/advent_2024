with open("./data/4.1.txt") as f:
    grid = f.read().splitlines()

cols = len(grid[0])
rows = len(grid)
count = 0

directions = [
    [(0,0),(0,1),(0,2),(0,3)], #horizontal
    [(0,0),(0,-1),(0,-2),(0,-3)],
    
    [(0,0),(1,0),(2,0),(3,0)], #vertical
    [(0,0),(-1,0),(-2,0),(-3,0)],            
    
    [(0,0),(1,1),(2,2),(3,3)], #diagonal
    [(0,0),(-1,-1),(-2,-2),(-3,-3)],
    
    [(0,0),(-1,1),(-2,2),(-3,3)],
    [(0,0),(1,-1),(2,-2),(3,-3)],
]

def check(grid, row, col, directions):
    local_count = 0
    for direction in directions:
        try:
            xmas = ''
            for irow, icol in direction:
                if row+irow >= 0 and col+icol >= 0:
                    xmas = xmas + ((grid[row+irow][col+icol]))
            if xmas == "XMAS":
                local_count += 1
        except:
            pass
    return local_count

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "X":
            count += check(grid, row, col, directions)

print(count)