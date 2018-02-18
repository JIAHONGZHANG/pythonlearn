# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children,
# - the sum of the nodes along all of T*'s branches is equal to M.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)


def expand_tree(tree):
    Tree = tree
    class StackException(Exception):
        def __init__(self, message):
            self.message = message
        
    class Stack():
        def __init__(self):
            self._data = []
        
        def push(self, value):
            return self._data.append(value)
        
        def pop(self):
            if self._data == None:
                raise StackException('Empty!')
            return self._data.pop()
    
        def is_empty(self):
            return self._data == [] 
        
    def depth_first_search():
        stack = Stack()
        stack.push(([Tree.value],Tree))
    
        while not stack.is_empty():
            path,tree = stack.pop()
            #if None in path:
                #continue
            #print(path)
            library.append(path)
            if tree.left_node or tree.right_node:
                if tree.right_node:
                    stack.push((list(path) + [tree.right_node.value],tree.right_node))
                if tree.left_node:
                    stack.push((list(path) + [tree.left_node.value],tree.left_node))
    
    def get_max_number():
        temp = library
        sum_temp = []
        for i in temp[:]:
            if None in i:
                i.pop()
                sum_temp.append(sum(i))
            else:
                sum_temp.append(sum(i))
        return max(sum_temp)
    
    def add_branch():
        for i in sole_library_2:
            current_node = Tree
            if len(i) == 0 or len(i) == 1:
                break
            if len(i) == 2:
                if current_node.left_node.value == None \
                        and current_node.right_node.value == None:
                    break
                elif current_node.left_node.value == None:
                    current_node.left_node = BinaryTree(sum_number - Tree.value)
                elif current_node.right_node.value == None:
                    current_node.right_node = BinaryTree(sum_number - Tree.value)
            else:
                need_value = sum_number - sum(i[0 : -1])
                for item in i[1 : -1]:
                    if current_node.left_node.value == item:
                        current_node = current_node.left_node
                        continue
                    if current_node.right_node.value == item:
                        current_node = current_node.right_node
                        continue
                if sum(i[0 : -1]) != sum_number:
                    if current_node.left_node.value == None:
                        current_node.left_node = BinaryTree(need_value)
                    if current_node.right_node.value == None:
                        current_node.right_node = BinaryTree(need_value)
                    
    library = []
    sole_library = []
    sole_library_2 = []
    #delete_element = set()

    depth_first_search()
    sum_number = get_max_number()
    depth_first_search()
    for i in library:
        if None in i:
            sole_library.append(i)
                

    for i in sole_library:
        if i in sole_library_2:
            continue
        else:
            sole_library_2.append(i)
        
    #print(sole_library_2)   
    #print(sum_number)   
    add_branch()

                
    pass
    # Replace pass above with your code


# Possibly define other functions


                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()



