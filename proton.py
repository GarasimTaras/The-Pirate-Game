import numpy as np
import random as rand

def gen_coord():
    coordinate = -1
    coordinate = rand.randint(0,9)
    
    return(coordinate)


grid = np.zeros((10, 10), dtype='int16')


grid[1, 2] = 100
grid[7, 7] = 3

#temp = [[2], [2]]   #gen_coord()


grid[gen_coord(),gen_coord()] = '11'



pregrid = np.loadtxt("grid.csv", delimiter=',', dtype='int32')

