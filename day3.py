def read():
    with open("./day3.txt") as f:
        return [l.strip() for l in f.readlines()]



def task_one():
    def build_grid():
        lines = read()
        grid = [list('.' * (len(lines[1]) + 2))]
        for line in lines:
            grid.append(list('.' + line + '.'))
        grid.append(list('.' * (len(lines[1]) + 2)))
        return grid
    
     
    grid = build_grid()    
    for row in grid:
        print(row)
    # for i, row in enumerate(grid):
    #     for j, col in enumerate(row):
    #         if col.isnumeric():
                
                
            

task_one()

