
import tkinter as tk
from maze import Maze
import time

GRID_HEIGHT = 60
GRID_WIDTH = 60

class MazeView(tk.Tk, object):
    def __init__(self, grid_per_column, grid_per_row):
        super(MazeView, self).__init__()
        self.grid_per_column = grid_per_column
        self.grid_per_row = grid_per_row
        self.title('maze')
        self.geometry('{0}x{1}'.format(grid_per_row * GRID_WIDTH, grid_per_row * GRID_HEIGHT))
        self.canvas = tk.Canvas(self,
                                bg='white',
                                width = grid_per_row * GRID_WIDTH,
                                height = grid_per_column * GRID_HEIGHT)
        self.canvas.pack()
        self.updateMaze(None)

    def updateMaze(self, maze):
        time.sleep(0.001)
        self.canvas.delete("avatar")
        if (maze):
            self.__paintMaze(maze)
        self.update()

    def __paintMaze(self, maze):
        width = self.grid_per_column
        height = self.grid_per_row
        for x in range(height):
            for y in range(width):
                if (maze.currentState[y][x] == Maze.WALL):
                    centerX = x * GRID_WIDTH + GRID_WIDTH / 2
                    centerY = y * GRID_HEIGHT + GRID_HEIGHT / 2
                    self.canvas.create_rectangle(
                        centerX - GRID_WIDTH / 2, centerY - GRID_HEIGHT / 2,
                        centerX + GRID_WIDTH / 2, centerY + GRID_WIDTH / 2,
                        fill='black')
                if (maze.currentState[y][x] == Maze.AVATAR):
                    centerX = x * GRID_WIDTH + GRID_WIDTH / 2
                    centerY = y * GRID_HEIGHT + GRID_HEIGHT / 2
                    self.canvas.create_oval(
                        centerX - 15, centerY - 15,
                        centerX + 15, centerY + 15,
                        fill='green', tags="avatar")
                if (maze.currentState[y][x] == Maze.TRAP):
                    centerX = x * GRID_WIDTH + GRID_WIDTH / 2
                    centerY = y * GRID_HEIGHT + GRID_HEIGHT / 2
                    self.canvas.create_rectangle(
                        centerX - GRID_WIDTH / 2, centerY - GRID_HEIGHT / 2,
                        centerX + GRID_WIDTH / 2, centerY + GRID_WIDTH / 2,
                        fill='red')
                if (maze.currentState[y][x] == Maze.GOAL):
                    centerX = x * GRID_WIDTH + GRID_WIDTH / 2
                    centerY = y * GRID_HEIGHT + GRID_HEIGHT / 2
                    self.canvas.create_rectangle(
                        centerX - 15, centerY - 15,
                        centerX + 15, centerY + 15,
                        fill='blue')