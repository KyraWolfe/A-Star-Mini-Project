import heapq
class Environment:

    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.lastRow = 0
        self.lasCol = 0
        self.totalCost = float('inf')
        self.actualCost = float('inf')
        self.estimatedCost = 0
        self.row = 4
        self.col = 4

    def depth_first(self, grid, start):
        seen = set()
        group = [start]
        cost = 0

        while group:
            item  = group.pop()
            if item not in seen:
                if item == 'd':
                    grid[item] = 'c'
                    print(item, end = " ")
                    seen.add(item)
                    cost += 2
                    group.extend(reversed(grid[item]))
                elif item == "#":
                    group.extend(reversed(grid[item]))
                else:
                    print(item, end = " ")
                    seen.add(item)
                    cost += 1
                    group.extend(reversed(grid[item]))
            print("The cost of this trip was ", cost)

    def inBounds(self, r, c):
        return 0 <= r < self.row and 0 <= c < self.col

    def noObstacle(self, grid, r, c):
        return grid[r][c] == "#"

    def isDirty(self, grid, r, c):
            return grid[r][c] == "d"

    def endReached(self, r, c, end):
        return r == end[1] and c == end[0]

    def findEstimatedCost(self, r, c, end):
        return ((r - end[1] ** 2 + (c - end[0]) ** 2) ** 0.5)

    def path(self, cell, end):
        trip = []

        row, col  = end

        while not (cell[row][col].lastRow == row and cell[row][col].lastCol == col):
            trip.append((row,col))
            row = cell[row][col].lastRow
            col = cell[row][col].lastCol
        trip.append((row, col))
        trip.reverse()

        print("The trip is: ")
        for item in trip:
            print("->", item, end=" ")
        print()

    def aStar(self, grid, start, end):
        if not self.inBounds(start[0], start[0] or not self.endinBounds(end[1], end[0])):
            print("Start or End is out of bounds")
            return
        if not self.noObstacle(grid, start[0], start[0]) or not self.noObstacle(grid, end[1], end[0]):
            print("Start or End is obstructed")
            return
        if self.endReached(start[0], start[0], end):
            print("The end has been reached")
            return
        
        cellInfo = [[Environment() for _ in range(self.col) for _ in range(self.row)]]

        r, c = start

        cellInfo[r][c].totalCost = 0
        cellInfo[r][c].actualCost = 0
        cellInfo[r][c].estimatedCost = 0
        cellInfo[r][c].lastRow = r
        cellInfo[r][c].lastCol = c

        tempList = 0
        heapq.heappush(tempList, (0.0, r, c))

        moves = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

        while tempList:
            _, r, c = heapq.heappop(tempList)

            if tempList[r][c]:
                continue

            tempList[r][c] = True

            for mR, mC in moves:
                newR = r + mR
                newC = c + mC

                if not self.inBounds(newR, newC):
                    continue

                if not self.noObstacle(grid, newR, newC):
                    continue

                if self.Dirty(grid, newR, newC):
                    cellInfo[newR][newC] = "c"
                    return

                if tempList[newR][newC]:
                    continue

                if self.endReached(newR, newC):
                    cellInfo[newR][newC].lastRow = r
                    cellInfo[newR][newC].lastCol = c

                    print("The end has been reached")

                    self.path(cellInfo, end)
                    return

                newActualCost = cellInfo[r][c].actualCost + 1.0
                newEstimatedCost = self.findEstimatedCost(newR, newC, end)
                newTotalCost = newActualCost + newEstimatedCost

                if cellInfo[newR][newC].totalCost > newTotalCost:
                    cellInfo[newR][newC].totalCost = newTotalCost
                    cellInfo[newR][newC].actualCost = newActualCost
                    cellInfo[newR][newC].estimatedCost = newEstimatedCost

                    cellInfo[newR][newC].lastRow = r
                    cellInfo[newR][newC].lastCol = c

                    heapq.heappush(tempList, (newTotalCost, newR, newC))
                
                print("failed to find the end cell")

#information
grid4 = [["c", "c", "d", "c"],
        ["c", "#", "c", "d"],
        ["d", "#", "c", "c"],
        ["c", "c", "d", "c"]
    ]
keys = ['row1', 'row2', 'row3', 'row4']
grid4_dict = dict(zip(keys, grid4))
start = grid4[0][0]
end = grid4[1][0]
roomba = Environment(grid4, start, end)
roomba.depth_first(grid4_dict, 'row1')
print(grid4)
grid4 = [["c", "c", "d", "c"],
        ["c", "#", "c", "d"],
        ["d", "#", "c", "c"],
        ["c", "c", "d", "c"]
    ]
roomba.aStar(grid4, start, end)
print(grid4)