import numpy as np
import random as rand

def randDouble():
    return 1 / (rand.randint(0, 5) + 1) +  1 / (rand.randint(0, 10) + 1)

def getLoss(x, y):
    return y - x

def getLossTotal(x, y):
    loss = getLoss(x, y)
    result = 0.0

    for value in loss:
        result += value;

    return result

def getAverageLoss(x, y):
    return getLossTotal(x, y) / len(x)

def randomSet(count):
    set = []

    for i in range(count):
        set.append(randDouble())

    return np.array(set)

def getMES(x, y):
    return getLossTotal(x, y) ** 2

if __name__ == "__main__":
   inputLayer = np.array([0.25, 0.3, 0.45, 0.6])
   predict = np.array([0.25, 0.3, 0.45, 0.6])
   actual = randomSet(len(predict))

   print("Actual:", actual)
   print("Predict:", predict) 
   print("Loss:", getLoss(actual, predict))
   print("Loss-Total:", getLossTotal(actual, predict))
   print("Average-Loss:", getAverageLoss(actual, predict))
   print("MES:", getMES(actual, predict))