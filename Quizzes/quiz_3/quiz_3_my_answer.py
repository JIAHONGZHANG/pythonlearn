# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
## we have dim
    ## grid[i][j], top-left is 0
    ## dict is stairs = {step_size : [(nb_steps, nb_stairs)]}
    ## step_stairs_list = [(nb_steps, nb_stairs)]
    ## steps = {nb_steps : nb_stairs}

    def check_vertical_line(x, y, step_size):
        ## from point (x, y),
        ## down-right
        ## has 0 -> return true
        for _ in range(step_size):
            if grid[x][y] == 0:
                return True
            x += 1
        return False

    def check_horizontal_line(x, y, step_size):
        ## from point (x, y)
        ## down-right
        ## has 0 -> return true
        return grid[x][y : y + step_size].count(0) != 0       
    
    def get_max_steps(i, j, step_size, nb_steps):
        ## check the deep, i + step_size is the deep of the stair
        ## check if this step is out of the world
        ##
        if i + step_size > dim:
            return nb_steps

        ## check the length, j + step_size * 2 - 1 is the length of the stair
        ## 
        elif j + step_size * 2 - 1 > dim:
            return nb_steps

        ## check the vertical line
        ## true means this has 0
        ##
        elif check_vertical_line(i, j + step_size - 1, step_size):
            return nb_steps

        ## check the horizontal line
        ## true means this has 0
        elif check_horizontal_line(i + step_size - 1, j + step_size - 1, step_size):
            return nb_steps

        else:

            return get_max_steps(i + step_size - 1, j + step_size - 1, step_size, nb_steps + 1)

    stairs = dict()
    step_size = 2
    while step_size <= dim // 2 + 1:

        ## steps = {max_step : nb_stairs}
        steps = dict()
        step_stairs_list = list()
        
        for i in range(dim):
            for j in range(dim):

                ## check the first line is legal
                ## check upper line is illegal, so this first line is legal
                ## check this first line have no 0
                ## then get max steps
                ## 
                if grid[i][j] != 0 and not check_horizontal_line(i, j, step_size):
                    if i - step_size + 1 < 0 or j - step_size + 1 < 0 or check_vertical_line(i - step_size + 1, j, step_size) or grid[i - step_size + 1][j - step_size + 1:j+1].count(0) != 0:
                        max_step = get_max_steps(i, j, step_size, 0)
                        if max_step != 0:
                            if max_step in steps:
                                steps[max_step] += 1
                            else:
                                steps[max_step] = 1
        ##                                
        for key in sorted(steps):
            step_stairs_list += [(key, steps[key])]

        if len(step_stairs_list) != 0:
            stairs[step_size] = step_stairs_list
        
        step_size += 1
    return stairs


try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
