# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

NewList = []
L = sorted(set(L))
for i in range(len(L)):
    for j in range(i, len(L)):
        if L[j] == 0:
            NewList.append([0.0, [L[i], 0]])
            continue
        NewList.append([L[i] / L[j], [L[i], L[j]]])

NewList = sorted(NewList)
if NewList[0][1][1] == 0:
    NewList.pop(0)
for temp in NewList:
    common = gcd(temp[1][0],temp[1][1])
    fractions.append(str(round(temp[1][0]/common))+'/'+str(round(temp[1][1]/common)))
for temp in range(len(L)):
    fractions.pop()
fractions.insert(len(fractions),"1")
if NewList[0][1][0]==0 or NewList[0][1][1]==0:
    fractions.insert(0,str(0))

NewList_2 = []
for temp in NewList:
    NewList_2.append([abs(temp[0]-0.5),[temp[1][0],temp[1][1]]])
NewList_2.sort()
common_NewList_2 = []
for temp in NewList_2:
    common = gcd(temp[1][0],temp[1][1])
    if temp[1][1]==0:
        common_NewList_2.append(str(0))
        continue
    if temp[1][0]/common and temp[1][1]/common == 1:
        common_NewList_2.append(str(1))
        continue
    if temp[1][0]/common == 0 and temp[1][1]/common == 1:
        common_NewList_2.append(str(0))
        continue
    common_NewList_2.append(str(round(temp[1][0]/common))+'/'+str(round(temp[1][1]/common)))
#if len(NewList_2) == 1:

else:
    first_number = NewList_2[0][0]
    if len(NewList_2) > 1:
        second_number = NewList_2[1][0]
    else:
        second_number = NewList_2[0][0]
if '1/2' in common_NewList_2[0]:
    spot_on = True
elif first_number == second_number:
    if len(NewList_2) > 1:
        closest_1 = common_NewList_2[0]
        closest_2 = common_NewList_2[1]
    else:
        closest_1 = round(NewList[0][0])
    spot_on = False
else:
    if len(NewList_2) > 1:
        closest_1 = common_NewList_2[0]
    else:
        spot_on = False
print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')

