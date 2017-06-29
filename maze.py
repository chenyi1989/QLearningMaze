
import numpy as np
import copy

class Maze:
    GOAL = 1000
    TRAP = -1000
    WALL = 1
    AVATAR = 2

    ACTION_UP = 0
    ACTION_DOWN = 1
    ACTION_LEFT = 2
    ACTION_RIGHT = 3

    def __init__(self, mazeArray):
        self.initialMaze = mazeArray
        self.currentState = copy.copy(self.initialMaze)
        return

    def avatarCoodinate(self):
        coodinate = np.where(self.currentState == self.AVATAR)
        return [coodinate[0][0], coodinate[1][0]]

    def isTerminated(self):
        coodinate = self.avatarCoodinate()
        if (self.initialMaze[coodinate[0]][coodinate[1]] == self.TRAP):
            return True
        if (self.initialMaze[coodinate[0]][coodinate[1]] == self.GOAL):
            return True
        return False

    def currentReward(self):
        currentCoodinate = self.avatarCoodinate()
        return self.__rewardAt(currentCoodinate[0], currentCoodinate[1])

    def moveAvatar(self, direction):
        if (self.isTerminated()):
            return

        currentCoodinate = self.avatarCoodinate()
        targetCoodinate = currentCoodinate
        if (direction == self.ACTION_UP):
            targetCoodinate[0] = targetCoodinate[0] - 1
        if (direction == self.ACTION_DOWN):
            targetCoodinate[0] = targetCoodinate[0] + 1
        if (direction == self.ACTION_LEFT):
            targetCoodinate[1] = targetCoodinate[1] - 1
        if (direction == self.ACTION_RIGHT):
            targetCoodinate[1] = targetCoodinate[1] + 1

        if (self.__canMoveTo(targetCoodinate[0], targetCoodinate[1])):
            self.__doMove(targetCoodinate[0], targetCoodinate[1])

    def __canMoveTo(self, x, y):
        if (x < 0) or (y < 0):
            return False
        if (x >= self.initialMaze.shape[0]) or (y >= self.initialMaze.shape[1]):
            return False
        if (self.initialMaze[x][y] == self.WALL):
            return False
        return True

    def __doMove(self, x, y):
        currentCoodinate = self.avatarCoodinate()
        self.currentState[x][y] = self.AVATAR
        self.currentState[currentCoodinate[0]][currentCoodinate[1]] = 0

    def __rewardAt(self, x, y):
        if (self.initialMaze[x][y] == 0):
            return 0
        if (self.initialMaze[x][y] == self.GOAL):
            return 1
        if (self.initialMaze[x][y] == self.TRAP):
            return -1
        return 0