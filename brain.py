
import random
import pandas as pd
import numpy as np

class Brain:
    def __init__(self, actions, learningRate = 0.01, gamma = 0.9, greedy = 0.9):
        self.actions = actions
        self.learningRate = learningRate
        self.gamma = gamma
        self.greedy = greedy
        self.qTable = pd.DataFrame(columns=actions)

    def chooseAction(self, state):
        if (np.random.uniform() < self.greedy) and (state in self.qTable.index):
            stateAction = self.qTable.ix[state, :]
            stateAction = stateAction.reindex(
                np.random.permutation(stateAction.index))
            action = stateAction.argmax()
        else:
            action = np.random.choice(self.actions)

        return action

    def updateActionReward(self, oldState, action, newState, reward):
        self.__appendStateIfNeeded(oldState)
        self.__appendStateIfNeeded(newState)

        qTarget = reward + self.gamma * self.qTable.ix[newState, :].max()
        self.qTable.ix[oldState, action] += self.learningRate * (qTarget)

    def __appendStateIfNeeded(self, state):
        if state not in self.qTable.index:
            self.qTable = self.qTable.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.qTable.columns,
                    name=state,
                )
            )