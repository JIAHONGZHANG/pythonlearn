# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by *** and Eric Martin for COMP9021

class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
    def __init__(self, *args, length = None):
        self.list = []
        self.cycles = []
        self.nb_of_cycles = 0

        ## build the list
        if len(args) == 0 and length == None:
            self.list = []
        elif len(args) == 0 and length != None and length >= 0:
            for i in range(1, length+1):
                self.list += [i]
        elif len(args) > 0:
            check_set = set()
            for i in range(len(args)):
                check_set.add(i+1)
                if type(args[i]) != int:
                    raise PermutationError("Cannot generate permutation from these arguments")
                    return
            if set(args) != check_set:
                raise PermutationError("Cannot generate permutation from these arguments")
                return
            if length != None and length != len(args):
                raise PermutationError("Cannot generate permutation from these arguments")
                return
            for arg in args:
                self.list += [arg]
        else:
            raise PermutationError("Cannot generate permutation from these arguments")
            return

        self.check_and_build_cycles()


    def __len__(self):
        return len(self.list)


    def __repr__(self):
        return 'Permutation({})'.format(', '.join(str(i) for i in self.list))


    def __str__(self):
        result = []
        for cycle in self.cycles:
            result += [' '.join(str(c) for c in cycle)]
        return '({})'.format(')('.join(i for i in result))
        

    def __mul__(self, permutation):
        if len(self) != len(permutation):
            raise PermutationError("Cannot compose permutations of different lengths")
            return
        temp = []
        for index in self.list:
            temp += [permutation.list[index - 1]]
        new = Permutation(length = len(self))
        new.list = temp[:]
        new.check_and_build_cycles()
        return new
            

    def __imul__(self, permutation):
        return self * permutation

    def inverse(self):
        temp = self.list[:]
        for index in range(len(self)):
            temp[self.list[index] - 1] = index + 1
        new = Permutation(length = len(self))
        new.list = temp[:]
        new.check_and_build_cycles()
        return new
        
    # Insert your code for helper functions, if needed
    def check_and_build_cycles(self):
        self.cycles = []
        self.nb_of_cycles = 0
        ## check and build the cycles
        for i in range(len(self.list)):
            value = self.list[i]
            temp_list = []
            temp_list += [value]
            while value != i + 1:
                value = self.list[value - 1]
                temp_list += [value]
            if temp_list[0] == max(temp_list):
                self.cycles += [temp_list]
                self.nb_of_cycles += 1
                
        ## sorted by the first number of cycles.
        self.cycles.sort(key=lambda l:(l[0]))


                
        




                
        
