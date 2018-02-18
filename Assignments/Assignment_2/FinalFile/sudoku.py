# coding: utf-8

# In[19]:

import sys
import os
from collections import defaultdict

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message


# In[20]:

class Sudoku:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as file:
            self.item_list = []
            for line in file:
                for item in line:
                    if item.isdigit():
                        self.item_list.append(int(item))
            if len(self.item_list) != 81:
                raise SudokuError('Incorrect input')
                sys.exit()
  
    def preassess(self):
        each_row_library, each_column_library,each_box_library = self.get_each_library()
        for i in range(9):
            for j in range(1, 9):
                if each_row_library[i].count(j) > 1:
                    print('There is clearly no solution.')
                    sys.exit()
                if each_column_library[i].count(j) > 1:
                    print('There is clearly no solution.')
                    sys.exit()
                if each_box_library[i].count(j) > 1:
                    print('There is clearly no solution.')
                    sys.exit()
        print('There might be a solution.')
        
                
    def get_each_library(self):
        item_list = self.item_list
        each_row_library = defaultdict(list)
        each_column_library = defaultdict(list)
        each_box_library = defaultdict(list)

        each_row_library.clear()
        each_column_library.clear()
        each_box_library.clear()


        for i in range(9):
            for j in range(i * 9, (i + 1) * 9):
                each_row_library[i].append(item_list[j])

        for i in range(9):
            for j in range(9):
                each_column_library[i].append(item_list[j * 9 + i])

        for i in range(3):
            for j in range(3):
                each_box_library[0].append(each_row_library[i][j])
        for i in range(3):
            for j in range(3, 6):
                each_box_library[1].append(each_row_library[i][j])
        for i in range(3):
            for j in range(6, 9):
                each_box_library[2].append(each_row_library[i][j])
        for i in range(3, 6):
            for j in range(3):
                each_box_library[3].append(each_row_library[i][j])
        for i in range(3, 6):
            for j in range(3, 6):
                each_box_library[4].append(each_row_library[i][j])
        for i in range(3, 6):
            for j in range(6, 9):
                each_box_library[5].append(each_row_library[i][j])
        for i in range(6, 9):
            for j in range(3):
                each_box_library[6].append(each_row_library[i][j])
        for i in range(6, 9):
            for j in range(3, 6):
                each_box_library[7].append(each_row_library[i][j])
        for i in range(6, 9):
            for j in range(6, 9):
                each_box_library[8].append(each_row_library[i][j])

        return each_row_library,each_column_library,each_box_library
    
    def get_display(self, have_in_box):
        string = ''
        if 1 in have_in_box and 2 in have_in_box:
            string += '\\N{1 2}'
        if 1 in have_in_box and 2 not in have_in_box:
            string += '\\N{1}'
        if 1 not in have_in_box and 2 in have_in_box:
            string += '\\N{2}'
        if 1 not in have_in_box and 2 not in have_in_box:
            string += '\\N{}'

        if 3 in have_in_box and 4 in have_in_box:
            string += '{3 4}'
        if 3 in have_in_box and 4 not in have_in_box:
            string += '{3}'
        if 3 not in have_in_box and 4 in have_in_box:
            string += '{4}'
        if 3 not in have_in_box and 4 not in have_in_box:
            string += '{}'

        if 5 in have_in_box and 6 in have_in_box:
            string += '{5 6}'
        if 5 in have_in_box and 6 not in have_in_box:
            string += '{5}'
        if 5 not in have_in_box and 6 in have_in_box:
            string += '{6}'
        if 5 not in have_in_box and 6 not in have_in_box:
            string += '{}'
            
        if 7 in have_in_box and 8 not in have_in_box and 9 not in have_in_box:
            string += '{7}'
        if 7 not in have_in_box and 8 in have_in_box and 9 not in have_in_box:
            string += '{8}'
        if 7 not in have_in_box and 8 not in have_in_box and 9 in have_in_box:
            string += '{9}'
        if 7 in have_in_box and 8 in have_in_box and 9 not in have_in_box:
            string += '{7 8}'
        if 7 in have_in_box and 8 not in have_in_box and 9 in have_in_box:
            string += '{7 9}'
        if 7 not in have_in_box and 8 in have_in_box and 9 in have_in_box:
            string += '{8 9}'
        if 7 in have_in_box and 8 in have_in_box and 9 in have_in_box:
            string += '{7 8 9}'
        if 7 not in have_in_box and 8 not in have_in_box and 9 not in have_in_box:
            string += '{}'

        string += '{}'
        return string

    def bare_tex_output(self):
        file_name = self.file_name
        each_row_library,each_column_library,each_box_library = self.get_each_library()
        item_list = self.item_list
        trim_file_name = ''
        for each_str in file_name:
            if each_str is '.':
                break
            trim_file_name = trim_file_name + each_str
        with open(trim_file_name + '_bare.tex', 'w') as tex_file_name:
            print('\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}', file = tex_file_name)
            print('\\usepackage{cancel}\n\\pagestyle{empty}', file = tex_file_name)
            print('\n', file = tex_file_name, end = '')
            print('\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},', file = tex_file_name)
            print('                               label=above right:{\\tiny #2},', file = tex_file_name)
            print('                               label=below left:{\\tiny #3},', file = tex_file_name)
            print('                               label=below right:{\\tiny #4}]{#5};}}', file = tex_file_name)
            print('\n', file = tex_file_name, end = '')
            print('\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}', file = tex_file_name)
            print('\n', file = tex_file_name, end ='')
            print('\\begin{center}', file = tex_file_name)
            print('\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = tex_file_name)
            #print('\n', file = tex_file_name)
            for i in range(81):
                if i == 0:
                    print('% Line 1', file = tex_file_name)
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        print('\\N{}{}{}{}{} & ', file = tex_file_name, end = '')

                elif i in (2, 5, 11, 14, 20, 23, 29, 32, 38, 41, 47, 50, 56, 59, 65, 68, 74, 77):
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} &', file = tex_file_name)
                    else:
                        print('\\N{}{}{}{}{} &', file = tex_file_name)

                elif i in (8, 17, 35, 44, 62, 71):
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\n', file = tex_file_name)
                    else:
                        print('\\N{}{}{}{}{} \\\\ \\hline\n', file = tex_file_name)

                elif i in (26, 53, 80):
                    if i == 80:
                        if item_list[i]  != 0:
                            print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\\hline', file = tex_file_name)
                        else:
                            print('\\N{}{}{}{}{} \\\\ \\hline\\hline', file = tex_file_name)
                    else:
                        if item_list[i]  != 0:
                            print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\\hline\n', file = tex_file_name)
                        else:
                            print('\\N{}{}{}{}{} \\\\ \\hline\\hline\n', file = tex_file_name)
                        

                elif i in (9, 18, 27, 36, 45, 54, 63, 72):
                    print(f'% Line {i//9 + 1}', file = tex_file_name)
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        print('\\N{}{}{}{}{} & ', file = tex_file_name, end = '')

                else:
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        print('\\N{}{}{}{}{} & ', file = tex_file_name, end = '')  

    
            print('\\end{tabular}\n\\end{center}\n\n\\end{document}', file = tex_file_name)
        
    def get_reflect_library(self):
        reflect_library = defaultdict(set)
        reflect_library[0] = (0,0,0)
        reflect_library[1] = (0,1,0)
        reflect_library[2] = (0,2,0)
        reflect_library[3] = (0,3,1)
        reflect_library[4] = (0,4,1)
        reflect_library[5] = (0,5,1)
        reflect_library[6] = (0,6,2)
        reflect_library[7] = (0,7,2)
        reflect_library[8] = (0,8,2)
        reflect_library[9] = (1,0,0)
        reflect_library[10] = (1,1,0)
        reflect_library[11] = (1,2,0)
        reflect_library[12] = (1,3,1)
        reflect_library[13] = (1,4,1)
        reflect_library[14] = (1,5,1)
        reflect_library[15] = (1,6,2)
        reflect_library[16] = (1,7,2)
        reflect_library[17] = (1,8,2)
        reflect_library[18] = (2,0,0)
        reflect_library[19] = (2,1,0)
        reflect_library[20] = (2,2,0)
        reflect_library[21] = (2,3,1)
        reflect_library[22] = (2,4,1)
        reflect_library[23] = (2,5,1)
        reflect_library[24] = (2,6,2)
        reflect_library[25] = (2,7,2)
        reflect_library[26] = (2,8,2)
        reflect_library[27] = (3,0,3)
        reflect_library[28] = (3,1,3)
        reflect_library[29] = (3,2,3)
        reflect_library[30] = (3,3,4)
        reflect_library[31] = (3,4,4)
        reflect_library[32] = (3,5,4)
        reflect_library[33] = (3,6,5)
        reflect_library[34] = (3,7,5)
        reflect_library[35] = (3,8,5)
        reflect_library[36] = (4,0,3)
        reflect_library[37] = (4,1,3)
        reflect_library[38] = (4,2,3)
        reflect_library[39] = (4,3,4)
        reflect_library[40] = (4,4,4)
        reflect_library[41] = (4,5,4)
        reflect_library[42] = (4,6,5)
        reflect_library[43] = (4,7,5)
        reflect_library[44] = (4,8,5)
        reflect_library[45] = (5,0,3)
        reflect_library[46] = (5,1,3)
        reflect_library[47] = (5,2,3)
        reflect_library[48] = (5,3,4)
        reflect_library[49] = (5,4,4)
        reflect_library[50] = (5,5,4)
        reflect_library[51] = (5,6,5)
        reflect_library[52] = (5,7,5)
        reflect_library[53] = (5,8,5)
        reflect_library[54] = (6,0,6)
        reflect_library[55] = (6,1,6)
        reflect_library[56] = (6,2,6)
        reflect_library[57] = (6,3,7)
        reflect_library[58] = (6,4,7)
        reflect_library[59] = (6,5,7)
        reflect_library[60] = (6,6,8)
        reflect_library[61] = (6,7,8)
        reflect_library[62] = (6,8,8)
        reflect_library[63] = (7,0,6)
        reflect_library[64] = (7,1,6)
        reflect_library[65] = (7,2,6)
        reflect_library[66] = (7,3,7)
        reflect_library[67] = (7,4,7)
        reflect_library[68] = (7,5,7)
        reflect_library[69] = (7,6,8)
        reflect_library[70] = (7,7,8)
        reflect_library[71] = (7,8,8)
        reflect_library[72] = (8,0,6)
        reflect_library[73] = (8,1,6)
        reflect_library[74] = (8,2,6)
        reflect_library[75] = (8,3,7)
        reflect_library[76] = (8,4,7)
        reflect_library[77] = (8,5,7)
        reflect_library[78] = (8,6,8)
        reflect_library[79] = (8,7,8)
        reflect_library[80] = (8,8,8)
        
        return reflect_library
    
    def forced_tex_output(self):
        reflect_library = self.get_reflect_library()
        #item_list = self.item_list
        #each_row_library,each_column_library,each_box_library = self.each_row_library, self.each_column_library, self.each_box_library
    
        box_number = 0
        while box_number < 9 :
            item_list = self.item_list
            each_row_library,each_column_library,each_box_library = self.get_each_library()
            zero_item_in_box = []
            for i in reflect_library:
                row, colume, box = reflect_library[i]
                if box == box_number:
                    if item_list[i] == 0:
                        #print(i, end = ' ')
                        zero_item_in_box.append(i)

            have_in_box = defaultdict(list)
            for i in range(81):
                have_in_box[i] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in zero_item_in_box:
                row, colume, box = reflect_library[i]
                for j in each_row_library[row]:
                    if j in have_in_box[i]:
                        have_in_box[i].remove(j)
                for j in each_column_library[colume]:
                    if j in have_in_box[i]:
                        have_in_box[i].remove(j)
                for j in each_box_library[box]:
                    if j in have_in_box[i]:
                        have_in_box[i].remove(j)

            all_have_in_box = []
            for i in zero_item_in_box:
                all_have_in_box += have_in_box[i]

            forced_number = []
            for i in all_have_in_box:
                if all_have_in_box.count(i) == 1:
                    for key in zero_item_in_box:
                        if i in have_in_box[key]:
                            forced_number.append((i,key))


            if forced_number != []:
                for number,place in forced_number:
                    item_list[place] = number
                each_row_library, each_column_library, each_box_library = self.get_each_library()
                box_number = 0
                continue

            box_number += 1

        file_name = self.file_name
        item_list = self.item_list
        trim_file_name = ''
        for each_str in file_name:
            if each_str is '.':
                break
            trim_file_name = trim_file_name + each_str
        with open(trim_file_name + '_forced.tex', 'w') as tex_file_name:
            print('\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}', file = tex_file_name)
            print('\\usepackage{cancel}\n\\pagestyle{empty}', file = tex_file_name)
            print('\n', file = tex_file_name, end = '')
            print('\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},', file = tex_file_name)
            print('                               label=above right:{\\tiny #2},', file = tex_file_name)
            print('                               label=below left:{\\tiny #3},', file = tex_file_name)
            print('                               label=below right:{\\tiny #4}]{#5};}}', file = tex_file_name)
            print('\n', file = tex_file_name, end = '')
            print('\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}', file = tex_file_name)
            print('\n', file = tex_file_name, end ='')
            print('\\begin{center}', file = tex_file_name)
            print('\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = tex_file_name)
            #print('\n', file = tex_file_name)
            for i in range(81):
                if i == 0:
                    print('% Line 1', file = tex_file_name)
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        print('\\N{}{}{}{}{} & ', file = tex_file_name, end = '')

                elif i in (2, 5, 11, 14, 20, 23, 29, 32, 38, 41, 47, 50, 56, 59, 65, 68, 74, 77):
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} &', file = tex_file_name)
                    else:
                        print('\\N{}{}{}{}{} &', file = tex_file_name)

                elif i in (8, 17, 35, 44, 62, 71):
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\n', file = tex_file_name)
                    else:
                        print('\\N{}{}{}{}{} \\\\ \\hline\n', file = tex_file_name)

                elif i in (26, 53, 80):
                    if i == 80:
                        if item_list[i]  != 0:
                            print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\\hline', file = tex_file_name)
                        else:
                            print('\\N{}{}{}{}{} \\\\ \\hline\\hline', file = tex_file_name)
                    else:
                        if item_list[i]  != 0:
                            print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\\hline\n', file = tex_file_name)
                        else:
                            print('\\N{}{}{}{}{} \\\\ \\hline\\hline\n', file = tex_file_name)
                        

                elif i in (9, 18, 27, 36, 45, 54, 63, 72):
                    print(f'% Line {i//9 + 1}', file = tex_file_name)
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        print('\\N{}{}{}{}{} & ', file = tex_file_name, end = '')

                else:
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        print('\\N{}{}{}{}{} & ', file = tex_file_name, end = '')  

    
            print('\\end{tabular}\n\\end{center}\n\n\\end{document}', file = tex_file_name)
        
        #return have_in_box
        
    def marked_tex_output(self):
        
        self.forced_tex_output()
        file_name = self.file_name
        each_row_library,each_column_library,each_box_library = self.get_each_library()
        item_list = self.item_list
        reflect_library = self.get_reflect_library()
        have_in_box = defaultdict(list)
        
        for i in range(81):
            have_in_box[i] = [1,2,3,4,5,6,7,8,9]
        for i in range(81):
            if item_list[i] == 0:
                row,colume,box = reflect_library[i]
                for number in each_row_library[row]:
                    if number in have_in_box[i]:
                        have_in_box[i].remove(number)
                for number in each_column_library[colume]:
                    if number in have_in_box[i]:
                        have_in_box[i].remove(number)
                for number in each_box_library[box]:
                    if number in have_in_box[i]:
                        have_in_box[i].remove(number)

        trim_file_name = ''
        for each_str in file_name:
            if each_str is '.':
                break
            trim_file_name = trim_file_name + each_str
        with open(trim_file_name + '_marked.tex', 'w') as tex_file_name:
            print('\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}', file = tex_file_name)
            print('\\usepackage{cancel}\n\\pagestyle{empty}', file = tex_file_name)
            print('\n', file = tex_file_name, end = '')
            print('\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},', file = tex_file_name)
            print('                               label=above right:{\\tiny #2},', file = tex_file_name)
            print('                               label=below left:{\\tiny #3},', file = tex_file_name)
            print('                               label=below right:{\\tiny #4}]{#5};}}', file = tex_file_name)
            print('\n', file = tex_file_name, end = '')
            print('\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}', file = tex_file_name)
            print('\n', file = tex_file_name, end ='')
            print('\\begin{center}', file = tex_file_name)
            print('\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = tex_file_name)
            #print('\n', file = tex_file_name)
            for i in range(81):
                if i == 0:
                    print('% Line 1', file = tex_file_name)
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        regular_string = self.get_display(have_in_box[i])
                        print(regular_string + ' & ', file = tex_file_name, end = '')

                elif i in (2, 5, 11, 14, 20, 23, 29, 32, 38, 41, 47, 50, 56, 59, 65, 68, 74, 77):
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} &', file = tex_file_name)
                    else:
                        regular_string = self.get_display(have_in_box[i])
                        print(regular_string + ' &', file = tex_file_name)

                elif i in (8, 17, 35, 44, 62, 71):
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\n', file = tex_file_name)
                    else:
                        regular_string = self.get_display(have_in_box[i])
                        print(regular_string + ' \\\\ \\hline\n', file = tex_file_name)

                elif i in (26, 53, 80):
                    if i == 80:
                        if item_list[i]  != 0:
                            print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\\hline', file = tex_file_name)
                        else:
                            regular_string = self.get_display(have_in_box[i])
                            print(regular_string + ' \\\\ \\hline\\hline', file = tex_file_name)
                    else:
                        if item_list[i]  != 0:
                            print('\\N{}{}{}{}{'+ str(item_list[i]) + '} \\\\ \\hline\\hline\n', file = tex_file_name)
                        else:
                            regular_string = self.get_display(have_in_box[i])
                            print(regular_string + ' \\\\ \\hline\\hline\n', file = tex_file_name)
                        

                elif i in (9, 18, 27, 36, 45, 54, 63, 72):
                    print(f'% Line {i//9 + 1}', file = tex_file_name)
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        regular_string = self.get_display(have_in_box[i])
                        print(regular_string + ' & ', file = tex_file_name, end = '')

                else:
                    if item_list[i]  != 0:
                        print('\\N{}{}{}{}{'+ str(item_list[i]) + '} & ', file = tex_file_name, end = '')
                    else:
                        regular_string = self.get_display(have_in_box[i])
                        print(regular_string + ' & ', file = tex_file_name, end = '')  

    
            print('\\end{tabular}\n\\end{center}\n\n\\end{document}', file = tex_file_name)
            #return item_list
            



# In[21]:

#sudoku = Sudoku('sudoku_3.txt')


# In[22]:

#sudoku.marked_tex_output()


# In[ ]:



