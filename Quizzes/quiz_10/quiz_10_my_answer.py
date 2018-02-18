# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample

from priority_queue_adt import *


# Possibly define some functions
def get_sorted_list(priority_queue):
    sorted_list = []
    for i in priority_queue:
        if i == None:
            continue
        else:
            sorted_list.append(i)
            
    sorted_list = sorted(sorted_list, reverse = True)
    return sorted_list
            
def get_number_place(number):
    for i in range(len(pq._data)):
        if number == pq._data[i]:
            return i
        
    return None

def get_road(road):
    if road[-1] == 1:
        return road
    elif road[-1] % 2 == 0:
        return get_road(road + [int((road[-1]/2))])
    elif road[-1] % 2 == 1:
        return get_road(road + [int(((road[-1] - 1)/2))])
    
def preferred_sequence():
    def find_father(father_place):
        if father_place[-1] <= get_number_place(test_number):
            father_place.pop()
            return father_place
        elif father_place[-1] % 2 == 0:
            return find_father(father_place + [int((father_place[-1]/2))])
        elif father_place[-1] % 2 == 1:
            return find_father(father_place + [int(((father_place[-1] - 1)/2))])
    sorted_list = get_sorted_list(pq._data)
    new_list = []
    put_place = len(sorted_list)
    break_point = False
    while break_point == False:
        #print('*'*20)
        for test_number in sorted_list:
            #print('-'*20)
            #put_place = len(sorted_list) - len(new_list)
            check_point = True
            test_road = get_road([get_number_place(test_number)])
            road = get_road([put_place])
            a = find_father([put_place])
            #print(f'test_number:{test_number}\nput_place:{put_place}\nnew_list:{new_list}\ntest_road:{test_road}\nroad:{road}\na:{a}')
            #print()
            if len(get_road([get_number_place(test_number)])) == 1:
                for i in a:
                    if i % 2 == 0:
                        try:
                            if pq._data[i] > pq._data[i + 1]:
                                continue
                            else:
                                #print('Violate!')
                                check_point = False
                                break
                        except TypeError:
                            #check_point = False
                            continue
                    else:
                        try:        
                            if pq._data[i] > pq._data[i - 1]:
                                continue
                            else:
                                #print('Violate!')
                                check_point = False
                                break
                        except TypeError:
                            #check_point = False
                            continue

            elif get_road([get_number_place(test_number)])[-2] != get_road([put_place])[-2]:
                #print('Violate!')
                check_point = False  
            else:
                for e in test_road:
                    if e not in road:
                        #print('Violate!')
                        check_point = False
                        break
                if len(a) == 1:
                    pass#print('OK2')
                else:
                    for i in a:
                        if i % 2 == 0:
                            try:
                                if pq._data[i] > pq._data[i + 1]:
                                    continue
                                else:
                                    #print('Violate!')
                                    check_point = False
                                    break
                            except TypeError:
                                #check_point = False
                                continue
                        else:
                            try:        
                                if pq._data[i] > pq._data[i - 1]:
                                    continue
                                else:
                                    #print('Violate!')
                                    check_point = False
                                    break
                            except TypeError:
                                #check_point = False
                                continue
            #print(f'check_point:{check_point}\npq._data:{pq._data}')
            if check_point:
                #print(f'ok, number is {test_number}')
                new_list.append(test_number)
                sorted_list.remove(test_number)
                road.reverse()
                #print(f'reversed_road:{road}')
                delete_place = get_number_place(test_number)
                for path in range(len(road)):
                    #print(f'path:{road[path]}')
                    if road[path] < delete_place:
                        #print('1')
                        continue
                    else:
                        if road[path] == put_place:
                            pq._data[road[path]] = None
                            #print('2')
                        if pq._data[road[path]] == None or pq._data[road[path + 1]] == None:
                            #print('Wrong!')
                            break
                        else:
                            #print('3')
                            pq._data[road[path]] = pq._data[road[path + 1]]

                #print(f'change_pq._data:{pq._data}')
                put_place -= 1
                break

        if put_place == 1:
            break_point = True
    one, two, three = pq._data[1],pq._data[2], pq._data[3] 
    if one != None and two != None and three != None:
        if two > three:
            new_list.append(three)
            new_list.append(one)
            new_list.append(two)
        elif two < three:
            new_list.append(one)
            new_list.append(three)
            new_list.append(two)
        else:
            new_list.append(two)
            new_list.append(three)
            new_list.append(one)
    if len(sorted_list) == 1:
        new_list += sorted_list
    new_list.reverse()
    return new_list
    pass
    # Replace pass above with your code (altogether, aim for around 24 lines of code)


try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())


