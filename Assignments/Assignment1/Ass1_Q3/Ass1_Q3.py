import sys
import os
#from collections import defaultdict

wordsEn = {}
wordsEn['a'] = 2
wordsEn['b'] = 5
wordsEn['c'] = 4
wordsEn['d'] = 4
wordsEn['e'] = 1
wordsEn['f'] = 6
wordsEn['g'] = 5
wordsEn['h'] = 5
wordsEn['i'] = 1
wordsEn['j'] = 7
wordsEn['k'] = 6
wordsEn['l'] = 3
wordsEn['m'] = 5
wordsEn['n'] = 2
wordsEn['o'] = 3
wordsEn['p'] = 5
wordsEn['q'] = 7
wordsEn['r'] = 2
wordsEn['s'] = 1
wordsEn['t'] = 2
wordsEn['u'] = 4
wordsEn['v'] = 6
wordsEn['w'] = 6
wordsEn['x'] = 7
wordsEn['y'] = 5
wordsEn['z'] = 7

required_dict = []
check_point = True

input_str = input("Enter between 3 and 10 lowercase letters: ")
input_str = input_str.replace(' ','')
input_list = []
for i in input_str:
    if i.isalpha() == False:
        print('Incorrect input, giving up...')
        sys.exit()
    input_list.append(i)
if len(input_list)<3 or len(input_list)>10:
    print('Incorrect input, giving up...')
    sys.exit()
input_list.sort()
#print(input_list)

wordsEn_filename = 'wordsEn.txt'
if not os.path.exists(wordsEn_filename):
    print("Not such file.")
    sys.exit()

voc_library=set()
with open(wordsEn_filename) as main_library:
    voc = main_library.readlines()
    for line in voc:
        voc_library.add(line.split('\n')[0])

for i in voc_library:
    a = input_list[:]
    check_point = True
    for j in i:
        if len(a) == 10:
            if j not in a[0] and j not in a[1] \
               and j not in a[2] and j not in a[3]\
                   and j not in a[4] and j not in a[5] and \
                       j not in a[6] and j not in a[7] and j not in a[8] and j not in a[9]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
        if len(a) == 9:
            if j not in a[0] and j not in a[1] \
               and j not in a[2] and j not in a[3]\
                   and j not in a[4] and j not in a[5] and \
                       j not in a[6] and j not in a[7] and j not in a[8]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
        if len(a) == 8:
            if j not in a[0] and j not in a[1] \
               and j not in a[2] and j not in a[3]\
                   and j not in a[4] and j not in a[5] and j not in a[6] and j not in a[7]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
        if len(a) == 7:
            if j not in a[0] and j not in a[1] \
               and j not in a[2] and j not in a[3] and j not\
                       in a[4] and j not in a[5] and j not in a[6]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
        if len(a) == 6:
            if j not in a[0] and j not in a[1] \
               and j not in a[2] and j not in a[3] and j not\
                       in a[4] and j not in a[5]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
        if len(a) == 5:
            if j not in a[0] and j not in a[1] \
               and j not in a[2] and j not in a[3] and j not\
                       in a[4]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
        if len(a) == 4:
            if j not in a[0] and j not in a[1] \
               and j not in a[2] and j not in a[3]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
        if len(a) == 3:
            if j not in a[0] and j not in a[1] \
               and j not in a[2]:
                check_point = False
                #print('False',end = ' ')
                break
            else:
                a[a.index(j)] = '*'
                
    if check_point == True:
        number = 0
        for j in i:
           number = number + wordsEn[j]         
        required_dict.append((i,number))
required_dict_2 = []
#print(len(required_dict))
required_dict.append(('NULL',0))
required_dict.sort(key = lambda d: d[1],reverse = True)
#print(required_dict)
if required_dict[0][1] == 0:
    print('No word is built from some of those letters.')
    sys.exit()
else:
    print(f'The highest score is {required_dict[0][1]}.')
    for i in range(len(required_dict)):
        if required_dict[i][1] != required_dict[0][1]:
            continue
        else:
            required_dict_2.append(required_dict[i][0])
required_dict_2.sort()
if len(required_dict_2) == 1:
    print(f'The highest scoring word is {required_dict_2[0]}')
else:
    print('The highest scoring words are, in alphabetical order:')
    for i in required_dict_2:
        print(f'    {i}')
#print(f'{required_dict[1][1]}')
            
##    i = 0
##    while required_dict[i][0] == required_dict[i+1][0] :
##        print(f'   {required_dict[i+1][0]}')
##        i = i+1
##    
