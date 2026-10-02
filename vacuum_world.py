class VacuumWorld:
   
    def __init__(self, grid, dirty, row, col, cost, actions):
        self.grid = grid
        self.dirty = dirty
        self.row = row
        self.col = col
        self.cost = cost
        self.actions = actions

    def initial_state(self):
        return [self.row, self.col]

    def move_up(self, row, cost):
        if (row < 3 and row >=0):
            row += 1
            cost += 1
            actions.append ("move up")

    def move_down(self, row, cost):
        if (row <= 3 and row > 0):
            row -= 1
            cost += 1
            actions.append ("move down")

    def move_left(self, col, cost):
        if (col > 0 and col <=3):
            col -= 1
            cost += 1
            actions.append ("move left")

    def move_right(self, col, cost):
        if (col >= 0 and col < 3):
            col += 1
            cost += 1
            actions.append ("move right")

    def clean(self, state, dirty, cost):
        if (state in dirty):
            dirty.remove(state)
            cost += 1
            actions.append ("clean")

    def results(self):
        print("Steps taken: " + self.actions)
        print("Cost of steps: " + cost)

grid_4_x_4 = [["c", "c", "d", "c"],
              ["c", "#", "c", "d"],
              ["d", "#", "c", "c"],
              ["c", "c", "d", "c"]
             ]
row = 0
col = 0
cost = 0
actions = []
dirtySet = [[0,2], [1,3], [2,0], [3,2]]
start = [0][0]
end = [1][0]
'''depth first search'''
roomba = VacuumWorld(grid_4_x_4, dirtySet, row, col, cost, actions)
while(col != 3):
    if(grid_4_x_4[row][col] == "d"):
        roomba.clean([row][col], dirtySet, cost)
    roomba.move_right(col, cost)
if (col == 3):
    roomba.move_down(row, cost)
while(col != 0):
    if(grid_4_x_4[row][col] == "d"):
        roomba.clean([row][col], dirtySet, cost)
    if(grid_4_x_4[row][col] == "#"):
        roomba.move_down(row, cost)
    elif(grid_4_x_4[row][col]!= "#"):
        roomba.move_left(col, cost)
while(col != 3):
    if(grid_4_x_4[row][col] == "d"):
        roomba.clean([row][col], dirtySet, cost)
    if(grid_4_x_4[row][col] == "#"):
        roomba.move_down(row, cost)
    elif(grid_4_x_4[row][col]!= "#"):
        roomba.move_right(col, cost)
if (col == 3):
    roomba.move_down(row, cost)
while(col != 0):
    if(grid_4_x_4[row][col] == "d"):
        roomba.clean([row][col], dirtySet, cost)
    if(grid_4_x_4[row][col]!= "#"):
        roomba.move_left(col, cost)
if(row == 3 and col == 0):
    roomba.move_up(row, cost)
while(row != 1 and col != 0):
    if(grid_4_x_4[row][col] == "d"):
        roomba.clean([row][col], dirtySet, cost)
    if(grid_4_x_4[row][col]!= "#"):
        roomba.move_up(col, cost)
if(row == 1 and col == 0):
    roomba.results
