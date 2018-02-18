# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():
    def search_path(i,j):
        list_up = []
        list_up.append([i,j])
        if j  > 0:
            if grid[i][j] + 1 == grid[i][j - 1]:
                list_up.append([i,j - 1])
        if j < len(grid[0]) - 1 :
            if grid[i][j] + 1 == grid[i][j + 1]:
                list_up.append([i,j + 1])
        if i > 0:
            if grid[i][j] + 1 == grid[i - 1][j]:
                list_up.append([i - 1,j])
        if i < len(grid) - 1:
            if grid[i][j] + 1 == grid[i + 1][j]:
                list_up.append([i + 1,j])
        return list_up
    main_list = []
    one_list = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            main_list.append(search_path(i,j))
            if grid[i][j] == 1:
                one_list.append([1,[i,j]])
                
    for j in main_list[:]:
        if len(j) == 1:
            main_list.remove(j)

    for i in one_list:
        if i[1][1]  > 0:
            if grid[i[1][0]][i[1][1]] + 1 == grid[i[1][0]][i[1][1] - 1]:
                one_list.append([i[0]+1,[i[1][0],i[1][1] - 1]])
        if i[1][1] < len(grid[0]) - 1 :
            if grid[i[1][0]][i[1][1]] + 1 == grid[i[1][0]][i[1][1] + 1]:
                one_list.append([i[0]+1,[i[1][0],i[1][1] + 1]])
        if i[1][0] > 0:
            if grid[i[1][0]][i[1][1]] + 1 == grid[i[1][0] - 1][i[1][1]]:
                one_list.append([i[0]+1,[i[1][0] - 1,i[1][1]]])
        if i[1][0] < len(grid) - 1:
            if grid[i[1][0]][i[1][1]] + 1 == grid[i[1][0] + 1][i[1][1]]:
                one_list.append([i[0]+1,[i[1][0] + 1,i[1][1]]])

                
                
    one_list.sort(reverse = True)


    for i in one_list[:]:
        for j in main_list[:]:
            if i[1] == j[0]:
                one_list.remove(i)

    #print(one_list)
    paths = defaultdict(int)
    for i in one_list:
        paths[i[0]] += 1
    return paths
    
    # Replace pass above with your code

# Insert your code for other functions
    
try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
