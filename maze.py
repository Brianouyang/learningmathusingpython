class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0 
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazelist.append(rowList)
            columnsMaze = len(rowList)

maze = Maze("maze.txt")
# print(maze.mazelist)