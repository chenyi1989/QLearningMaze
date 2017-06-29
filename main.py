
from maze import Maze
import numpy as np
import time
from brain import Brain
from maze_view import MazeView

FRAME_TIME = 0.01
EPISODE_COUNT = 200

np.random.seed(42)

initialMaze = np.array([[Maze.TRAP,     0,          Maze.WALL, 0],
                        [0,             0,          0,         0],
                        [0,             Maze.WALL,  Maze.TRAP, 0],
                        [Maze.AVATAR,   0,          Maze.WALL, Maze.GOAL]])

def startLearning():
    brain = Brain([Maze.ACTION_UP, Maze.ACTION_DOWN, Maze.ACTION_LEFT, Maze.ACTION_RIGHT])
    for episode in range(EPISODE_COUNT):
        maze = Maze(initialMaze)
        mazeView.updateMaze(maze)
        steps = 0
        while True:
            oldState = maze.avatarCoodinate()
            action = brain.chooseAction(str(oldState))
            maze.moveAvatar(action)
            steps += 1
            mazeView.updateMaze(maze)
            reward = maze.currentReward()
            newState = maze.avatarCoodinate()
            brain.updateActionReward(str(oldState), action, str(newState), reward)
            if (maze.isTerminated()):
                if (reward > 0):
                    print("Success with {0} steps in training episode {1}.".format(steps, episode))
                else:
                    print("Failed with {0} steps in training episode {1}.".format(steps, episode))
                break
    print(brain.qTable)

mazeView = MazeView(initialMaze.shape[1], initialMaze.shape[0])
mazeView.after(100, startLearning)
mazeView.mainloop()