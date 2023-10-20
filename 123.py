import numpy as np
import random as rand
from pprint import pprint
from colorama import Fore, Back, Style

def pretty_print_ndarray(array, emoji, coordinates):
    for row in range(10):
        print('│', end='')
        for col in range(10):
            if 9 - row == coordinates[1] and col == coordinates[0]:
                print(Back.GREEN + f'{emoji[array[row,9 - col], 1]}',end='')
                print(Style.RESET_ALL,end='|' )
            else:
                print(emojis[array[row,col], 1], end='|')

        print('')

def gen_coord(coordxy):
    coordinate[0] = rand.randint(0,9)
    coordinate[1] = rand.randint(0,9)

current_coords = [0,8]


readgrid = np.loadtxt("grid.csv", delimiter=',', dtype='int32')
emojis = np.loadtxt("emojis.csv", delimiter=',', dtype='U')


pretty_print_ndarray(readgrid, emojis, current_coords)