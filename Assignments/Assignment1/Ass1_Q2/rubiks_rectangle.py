from collections import deque

# Insert your code here
import sys
from collections import defaultdict
def row_exchange(a):
    temp_a = []
    temp_a.append(a[7])
    temp_a.append(a[6])
    temp_a.append(a[5])
    temp_a.append(a[4])
    temp_a.append(a[3])
    temp_a.append(a[2])
    temp_a.append(a[1])
    temp_a.append(a[0])
    #print(temp_a)
    return temp_a
def right_circular_shift(a):
    temp_a = []
    temp_a.append(a[3])
    temp_a.append(a[0])
    temp_a.append(a[1])
    temp_a.append(a[2])
    temp_a.append(a[5])
    temp_a.append(a[6])
    temp_a.append(a[7])
    temp_a.append(a[4])
    #print(temp_a)
    return temp_a
def middle_clockwise_rotation(a):
    temp_a = []
    temp_a.append(a[0])
    temp_a.append(a[6])
    temp_a.append(a[1])
    temp_a.append(a[3])
    temp_a.append(a[4])
    temp_a.append(a[2])
    temp_a.append(a[5])
    temp_a.append(a[7])
    #print(temp_a)
    return temp_a
def check_list(initial_list,need_list):
    for i in range(8):
        if initial_list[i] != need_list[i]:
            return False
            break
        else:
            return True
library = defaultdict(list)
main_library = set()
main_library.add(str([1,2,3,4,5,6,7,8]))
str_list = input("Input final configuration: ")
str_list = str_list.replace(' ','')
try:
    int_list = []
    for i in str_list:
            int_list.append(int(i))
except ValueError:
    print('Incorrect configuration, giving up...')
    sys.exit()
if len(int_list) !=8:
    print('Incorrect configuration, giving up...')
    sys.exit()   
if (1 in int_list and 2 in int_list and 3 in int_list and 4 in int_list\
            and 5 in int_list and 6 in int_list\
                        and 7 in int_list and 8 in int_list) == False:
    print('Incorrect configuration, giving up...')
    sys.exit()
initial_int_list =[1,2,3,4,5,6,7,8]
library[0] = [1,2,3,4,5,6,7,8]
count_step = 0
if str(int_list) in main_library:
    print("0 step is needed to reach the final configuration.")
    sys.exit()
library[count_step +1].append(row_exchange(initial_int_list))
main_library.add(str(row_exchange(initial_int_list)))
library[count_step +1].append(right_circular_shift(initial_int_list))
main_library.add(str(right_circular_shift(initial_int_list)))
library[count_step +1].append(middle_clockwise_rotation(initial_int_list))
main_library.add(str(middle_clockwise_rotation(initial_int_list)))
count_step = count_step +1
if str(int_list) in main_library:
    print("1 step is needed to reach the final configuration.")
    sys.exit()
while 1:
    if str(int_list) in main_library:
        print(f'{count_step} steps are needed to reach the final configuration.')
        break
    for item in library[count_step]:
        if str(row_exchange(item)) not in main_library:
            library[count_step +1].append(row_exchange(item))
            main_library.add(str(row_exchange(item)))
        if str(right_circular_shift(item)) not in main_library:
            library[count_step +1].append(right_circular_shift(item))
            main_library.add(str(right_circular_shift(item)))
        if str(middle_clockwise_rotation(item)) not in main_library:
            library[count_step +1].append(middle_clockwise_rotation(item))
            main_library.add(str(middle_clockwise_rotation(item)))
    count_step = count_step +1


