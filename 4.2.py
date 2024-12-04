
#%%
with open("./data/4.1.txt") as f:
    grid = f.read().splitlines()

cols = len(grid[0])
rows = len(grid)
count = 0

directions = [
    [(-1,1),(0,0),(1,-1)],
    [(-1,-1),(0,0),(1,1)]
]

def check(grid, row, col, directions):
    local_count = 0
    count = 0
    for direction in directions:
        try:
            xmas = ''
            for irow, icol in direction:
                if row+irow >= 0 and col+icol >= 0:
                    xmas = xmas + ((grid[row+irow][col+icol]))
            if (xmas == "MAS") or (xmas == 'SAM'):
                local_count += 1
        except:
            pass
        if local_count == 2:
            count +=1
    return count

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "A":
            count += check(grid, row, col, directions)

print(count)
# %%
