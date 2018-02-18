from random import randint

# Insert your code here

from random import seed,randint
from collections import defaultdict
dice_library = {}
dice_library['Ace'] = 0
dice_library['King'] = 1
dice_library['Queen'] = 2
dice_library['Jack'] = 3
dice_library['10'] = 4
dice_library['9'] = 5

count_dice_library = {}
count_dice_library["Five of a kind"] = 0
count_dice_library["Four of a kind"] = 0
count_dice_library["Full house"] = 0
count_dice_library["Straight"] = 0
count_dice_library["Three of a kind"] = 0
count_dice_library["Two pair"] = 0
count_dice_library["One pair"] = 0

def play():

    def get_dice():
        if len(hand_dice) == 0:
            for _ in range(5):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 1:
            for _ in range(4):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 2:
            for _ in range(3):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 3:
            for _ in range(2):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 4:
                hand_dice.append(randint(0,5))
        hand_dice.sort()

    def search_dice_delete(choosen_dice):
        if choosen_dice in hand_dice:
            hand_dice.pop(hand_dice(choosen_dice))
        else:
            print("That is not possible, try again!")

    def display_rule_dice():
        global five_of_a_kind,four_of_a_kind,full_house,straight,three_of_a_kind,two_pair,one_pair,bust
        print()
        print("It is a",end =' ')
        if five_of_a_kind == True:
            print("Five of a kind")
        elif four_of_a_kind == True:
            print("Four of a kind")
        elif full_house == True:
            print("Full house")
        elif straight == True:
            print("Straight")
        elif three_of_a_kind == True:
            print("Three of a kind")
        elif two_pair == True:
            print("Two pair")
        elif one_pair == True:
            print("One pair")
        elif bust == True:
            print("Bust")

    def display_hand_dice():
        print("The roll is:",end = ' ')
        #print(hand_dice)
        for i in range(4):
            if hand_dice[i] == 0:
                print("Ace",end = ' ')
            if hand_dice[i] == 1:
                print("King",end = ' ') 
            if hand_dice[i] == 2:
                print("Queen",end = ' ')
            if hand_dice[i] == 3:
                print("Jack",end = ' ')
            if hand_dice[i] == 4:
                print("10",end = ' ')
            if hand_dice[i] == 5:
                print("9",end = ' ')
        if hand_dice[4] == 0:
            print("Ace",end = '')
        elif hand_dice[4] == 1:
            print("King",end = '') 
        elif hand_dice[4] == 2:
            print("Queen",end = '')
        elif hand_dice[4] == 3:
            print("Jack",end = '')
        elif hand_dice[4] == 4:
            print("10",end = '')
        elif hand_dice[4] == 5:
            print("9",end = '')

    def count_hand_dice():
        global nb_hand_dice
        nb_hand_dice = defaultdict(list)
        if 0 in hand_dice:
            nb_hand_dice[0] = [hand_dice.count(0)]
        if 1 in hand_dice:
            nb_hand_dice[1] = [hand_dice.count(1)]
        if 2 in hand_dice:
            nb_hand_dice[2] = [hand_dice.count(2)]
        if 3 in hand_dice:
            nb_hand_dice[3] = [hand_dice.count(3)]
        if 4 in hand_dice:
            nb_hand_dice[4] = [hand_dice.count(4)]
        if 5 in hand_dice:
            nb_hand_dice[5] = [hand_dice.count(5)]

    def rule_dice():
        global five_of_a_kind,four_of_a_kind,full_house,straight,three_of_a_kind,two_pair,one_pair,bust
        five_of_a_kind = False
        four_of_a_kind = False
        full_house = False
        straight = False
        three_of_a_kind = False
        two_pair = False
        one_pair =False
        bust = False
        if len(nb_hand_dice) == 5 :
            if 0 in nb_hand_dice and 5 in nb_hand_dice:
                bust = True
            else:
                straight = True
        if len(nb_hand_dice) == 4:
            one_pair = True
        if len(nb_hand_dice) == 3:
            for i in nb_hand_dice:
                if nb_hand_dice[i] == [3]:
                   three_of_a_kind = True
                   break
                if nb_hand_dice[i] == [2]:
                    two_pair = True
                    break
        if len(nb_hand_dice) == 2:
             for i in nb_hand_dice:
                if nb_hand_dice[i] == [4]:
                       four_of_a_kind = True
                elif nb_hand_dice[i] == [2]:
                       full_house = True
        if len(nb_hand_dice) == 1:
            five_of_a_kind = True

    def input_output_1():
        global check_wrong,temp_hand_dice,hand_dice
        input_massage = input("Which dice do you want to keep for the second roll? ")
#        input_massage = input_massage.upper()
        input_massage = input_massage.split(" ")
        temp_hand_dice = []
        if input_massage[0] == 'All' or input_massage[0] == 'all':
            check_wrong = False
            temp_hand_dice = hand_dice
        elif input_massage == ['']:
            hand_dice = []
            check_wrong = False
        else:
            for i in input_massage:
                if i in dice_library:
                    if dice_library[i] in hand_dice:
                        temp_hand_dice.append(dice_library[i])
                        if temp_hand_dice.count(dice_library[i]) > hand_dice.count(dice_library[i]):
                            check_wrong = True
                            print("That is not possible, try again!")
                            break
                        else:
                            check_wrong = False
                    else: 
                        check_wrong = True
                        print("That is not possible, try again!")
                        break
                else:
                    check_wrong = True
                    print("That is not possible, try again!")
                    break

    def input_output_2():
        global check_wrong,temp_hand_dice,hand_dice
        input_massage = input("Which dice do you want to keep for the third roll? ")
 #       input_massage = input_massage.upper()
        input_massage = input_massage.split(" ")
        temp_hand_dice = []
        if input_massage[0] == 'All' or input_massage[0] == 'all':
            check_wrong = False
            temp_hand_dice = hand_dice
        elif input_massage == ['']:
            hand_dice = []
            check_wrong = False
        else:
            for i in input_massage:
                if i in dice_library:
                    if dice_library[i] in hand_dice:
                        temp_hand_dice.append(dice_library[i])
                        if temp_hand_dice.count(dice_library[i]) > hand_dice.count(dice_library[i]):
                            check_wrong = True
                            print("That is not possible, try again!")
                            break
                        else:
                            check_wrong = False
                    else: 
                        check_wrong = True
                        print("That is not possible, try again!")
                        break
                else:
                    check_wrong = True
                    print("That is not possible, try again!")
                    break
        
                    
    global check_wrong,temp_hand_dice,hand_dice
    hand_dice = []
    temp_hand_dice = []

    get_dice()
    count_hand_dice()
    rule_dice()
    display_hand_dice()
    display_rule_dice()
    #dice_library
    check_wrong = bool
    check_wrong = True
    while check_wrong == True :
        input_output_1()
    #temp_hand_dice.sort   
    temp_hand_dice.sort()
    hand_dice.sort()
    if temp_hand_dice == hand_dice and hand_dice != []:
        print("Ok, done.")
    else:
        hand_dice = temp_hand_dice
        get_dice()
        count_hand_dice()
        rule_dice()
        display_hand_dice()
        display_rule_dice()
        
        check_wrong = bool
        check_wrong = True
        while check_wrong == True :
            input_output_2()
        temp_hand_dice.sort   
        #print(temp_hand_dice)
        if temp_hand_dice == hand_dice and hand_dice != []:
            print("Ok, done.")
        else:
            hand_dice = temp_hand_dice

            get_dice()
            count_hand_dice()
            rule_dice()
            display_hand_dice()
            display_rule_dice()

def simulate(times):
    def simulate_count():
        global five_of_a_kind_count,four_of_a_kind_count,full_house_count,straight_count,three_of_a_kind_count,\
                        two_pair_count,one_pair_count,bust_count
        if five_of_a_kind == True:
            five_of_a_kind_count = five_of_a_kind_count + 1 
        elif four_of_a_kind == True:
            four_of_a_kind_count = four_of_a_kind_count + 1
        elif full_house == True:
            full_house_count = full_house_count + 1
        elif straight == True:
            straight_count = straight_count + 1
        elif three_of_a_kind == True:
            three_of_a_kind_count = three_of_a_kind_count + 1
        elif two_pair == True:
            two_pair_count = two_pair_count + 1
        elif one_pair == True:
            one_pair_count = one_pair_count + 1
        elif bust == True:
            bust_count = bust_count + 1
    def get_dice():
        if len(hand_dice) == 0:
            for _ in range(5):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 1:
            for _ in range(4):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 2:
            for _ in range(3):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 3:
            for _ in range(2):
                hand_dice.append(randint(0,5))
        elif len(hand_dice) == 4:
                hand_dice.append(randint(0,5))
        hand_dice.sort()
    def count_hand_dice():
        global nb_hand_dice
        nb_hand_dice = defaultdict(list)
        if 0 in hand_dice:
            nb_hand_dice[0] = [hand_dice.count(0)]
        if 1 in hand_dice:
            nb_hand_dice[1] = [hand_dice.count(1)]
        if 2 in hand_dice:
            nb_hand_dice[2] = [hand_dice.count(2)]
        if 3 in hand_dice:
            nb_hand_dice[3] = [hand_dice.count(3)]
        if 4 in hand_dice:
            nb_hand_dice[4] = [hand_dice.count(4)]
        if 5 in hand_dice:
            nb_hand_dice[5] = [hand_dice.count(5)]  
        
    def rule_dice():
        global five_of_a_kind,four_of_a_kind,full_house,straight,three_of_a_kind,two_pair,one_pair,bust
        five_of_a_kind = False
        four_of_a_kind = False
        full_house = False
        straight = False
        three_of_a_kind = False
        two_pair = False
        one_pair =False
        bust = False
        if len(nb_hand_dice) == 5 :
            if 0 in nb_hand_dice and 5 in nb_hand_dice:
                bust = True
            else:
                straight = True
        if len(nb_hand_dice) == 4:
            one_pair = True
        if len(nb_hand_dice) == 3:
            for i in nb_hand_dice:
                if nb_hand_dice[i] == [3]:
                   three_of_a_kind = True
                   break
                if nb_hand_dice[i] == [2]:
                    two_pair = True
                    break
        if len(nb_hand_dice) == 2:
             for i in nb_hand_dice:
                if nb_hand_dice[i] == [4]:
                       four_of_a_kind = True
                elif nb_hand_dice[i] == [2]:
                       full_house = True
        if len(nb_hand_dice) == 1:
            five_of_a_kind = True    
        
    global five_of_a_kind_count,four_of_a_kind_count,full_house_count,\
                    straight_count,three_of_a_kind_count,two_pair_count,one_pair_count,bust_count
    five_of_a_kind_count = 0
    four_of_a_kind_count = 0
    full_house_count = 0
    straight_count = 0
    three_of_a_kind_count = 0
    two_pair_count = 0
    one_pair_count = 0
    bust_count = 0
    for _ in range(times):
        hand_dice = []
        temp_hand_dice = []

        get_dice()
        count_hand_dice()
        rule_dice()
        simulate_count()
    print("Five of a kind : {:.2f}%".format(five_of_a_kind_count/times*100))
    print("Four of a kind : {:.2f}%".format(four_of_a_kind_count/times*100))
    print("Full house     : {:.2f}%".format(full_house_count/times*100))
    print("Straight       : {:.2f}%".format(straight_count/times*100))
    print("Three of a kind: {:.2f}%".format(three_of_a_kind_count/times*100))
    print("Two pair       : {:.2f}%".format(two_pair_count/times*100))
    print("One pair       : {:.2f}%".format(one_pair_count/times*100))
