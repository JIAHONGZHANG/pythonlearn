# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randrange

from stack_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def explore_depth_first(x, y, target):
    #path = None
    check_point = False
    if grid[x][y] > target:
        return
    else:
        path = Stack()
        path.push((x,y))
        sum_path = grid[x][y]
        #change_point = y
        #unchange_point = x
        while 1:
            if sum_path == target:
                return path._data
                break
            change_point = path._data[-1][0]
            unchange_point = path._data[-1][1]
            if change_point > 0:
                i = change_point
                while i > 0:
                    i -= 1
                    if (i,unchange_point) in path._data:
                        break
                    elif sum_path + grid[i][unchange_point] < target:
                        sum_path = sum_path + grid[i][unchange_point]
                        path.push((i,unchange_point))
                    elif sum_path + grid[i][unchange_point] > target:
                        break
                    elif sum_path + grid[i][unchange_point] == target:
                        path.push((i,unchange_point))
                        return path._data
            
            change_point = path._data[-1][1]
            unchange_point = path._data[-1][0]
            if change_point < 9:
                i = change_point
                while i < 9:
                    i += 1
                    if (unchange_point,i) in path._data:
                        break
                    elif sum_path + grid[unchange_point][i] < target:
                        sum_path = sum_path + grid[unchange_point][i]
                        path.push((unchange_point,i))
                    elif sum_path + grid[unchange_point][i] > target:
                        break
                    elif sum_path + grid[unchange_point][i] == target:
                        path.push((unchange_point,i))
                        return path._data
                    
            change_point = path._data[-1][0]
            unchange_point = path._data[-1][1]
            if change_point < 9:
                i = change_point
                while i < 9:
                    i += 1
                    if (i,unchange_point) in path._data:
                        break
                    elif sum_path + grid[i][unchange_point] < target:
                        sum_path = sum_path + grid[i][unchange_point]
                        path.push((i,unchange_point))
                    elif sum_path + grid[i][unchange_point] > target:
                        break
                    elif sum_path + grid[i][unchange_point] == target:
                        path.push((i,unchange_point))
                        return path._data
                    
            change_point = path._data[-1][1]
            unchange_point = path._data[-1][0]
            if change_point > 0:
                i = change_point
                while i > 0:
                    i -= 1 
                    if (unchange_point,i) in path._data:
                        break
                    elif sum_path + grid[unchange_point][i] < target:
                        sum_path = sum_path + grid[unchange_point][i]
                        path.push((unchange_point,i))
                    elif sum_path + grid[unchange_point][i] > target:
                        break
                    elif sum_path + grid[unchange_point][i] == target:
                        path.push((unchange_point,i))
                        return path._data
            
    pass 


try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
