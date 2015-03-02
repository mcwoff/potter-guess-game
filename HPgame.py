# Hello Harry Potter World program in Python
#import os
#os.system('clear')
print('\n'*100)

from random import randint
from time import sleep
from operator import itemgetter
import sys,time,random

print "\nHELLO HARRY POTTER WORLD!"

top_score_list1 = []
top_score_list2 = []
current_standings = [0, 0]


#*#*#*#*#
# The initial game menu
def game_menu():
    print('\n'*100)
    print "\nWhat game would you like to play? (Enter the value)"
    print "1. Classic Mode"
    print "2. House Points High Score"
    print "3. Play for the House Cup (2-player) "
    desired_game = str(raw_input("4. Quit "))
    while desired_game != "1" and desired_game != "2" and desired_game != "3" and desired_game != "4":
        print "\nThat is not a valid option" ; sleep(2)
        os.system('clear')
        print "\nWhat game would you like to play? (Enter the value)"
        print "1. Classic Mode"
        print "2. House Points High Score"
        print "3. Play for the House Cup (2-player) "
        desired_game = str(raw_input("4. Quit "))
    print "\n"
    return int(desired_game)


#*#*#*#*#
# this is what the sorting hat says
# needs to have at least 3-5 different things with a random generator to pick the right one
# also needs to have slow typing
def sorting_hat():
    sorting_hat_speech1 = "Oh you may not think I'm pretty,\nBut don't judge on what you see,\nI'll eat myself if you can find\nA smarter hat than me." 
    sorting_hat_speech2 = "\n\nYou can keep your bowlers black,\nYour top hats sleek and tall,\nFor I'm the Hogwarts Sorting Hat\nAnd I can cap them all." 
    sorting_hat_speech3 = "\n\nThere's nothing hidden in your head\nThe Sorting Hat can't see,\nSo try me on and I will tell you\nWhere you ought to be."
    sorting_hat_speech = [sorting_hat_speech1, sorting_hat_speech2, sorting_hat_speech3]
    for speech in sorting_hat_speech:
        for letter in speech:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(.03)
    

#*#*#*#*#
# Pick your house (if playing game 3)
def pick_houses():
    players_houses = []
    for i in range(0,2):
        print('\n'*100)
        print "PLAYER " + str(i + 1) + ":" ; sleep(1)
        print "So you want to play for the House Cup. But first you need to be sorted into the proper house..."
        print "\n"
        sorting_hat()
        print "\n\n"
        print "1. Gryffindors who work together exude courage. Teaming up with them is bound to gain you some extra points."
        print "2. Slytherin's underhandedness is unmatched. They may be able to do something sneaky to your opponent for you."
        print "3. Ravenclaws are renowned for their intelligence. I'm sure they can help you solve the problem even faster."
        print "4. Hufflepuff: nobody actually knows what they are good at. However, they do believe in fairness, whatever that means..."
        player_house = raw_input("\nWhat house are you destined to be in (enter the number)? ")
        while player_house != "1" and player_house != "2" and player_house != "3" and player_house != "4" or player_house == previous_player:
            print "\nThat is not a valid option" ; sleep(1) 
            os.system('clear')
            print "1. Gryffindors who work together exude courage. Teaming up with them is bound to gain you some extra points."
            print "2. Slytherin's underhandedness is unmatched. They may be able to do something sneaky to your opponent for you."
            print "3. Ravenclaws are renowned for their intelligence. I'm sure they can help you solve the problem even faster."
            print "4. Hufflepuff: nobody actually knows what they are good at. However, they do believe in fairness, whatever that means..."
            player_house = raw_input("\nWhat house are you destined to be in (enter the number)? ")
        if player_house == "1":
            print "\nYou have chosen Gryffindor House! Team up with other Gryffindors for bonus points."
            players_houses[i] = "Gryff"
            #gryffindor: +5 points per every other gryffindor character you work with
        elif player_house == "2":
            print "\nYou have chosen Slytherin House! Team up with other Slytherins to steal points from your opponent."
            players_houses[i] = "Slyth"
            #slytherin: -5 to them and +5 to you everytime you work with another slytherin 
            # also rolling draco steals 5 from the other team to give to you
        elif player_house == "3":
            print "\nYou have chosen Ravenclaw House! They will tell you whether you're getting closer or further from the correct answer."
            players_houses[i] = "Raven"
            #ravenclaw: tells you whether you are getting closer or further from the magic number every turn
        else:
            print "\nYou have chosen Hufflepuff House! Although I don't know why you would do that voluntarily."
            players_houses[i] = "Huffl"
            #hufflepuff: much higher chance of rolling dumbledore 
        raw_input("\nPress any key to continue.")
        previous_player = player_house
    return players_houses
    
  
#*#*#*#*#
# Picks the character
def char_picker(desired_game, current_player_house):
    print('\n'*100)
    picker = randint(1, 110)
    print "\n"
    if desired_game == 3 and current_player_house == "Huffl": # Hufflepuff House ability
        k = 1
        for i in str(picker):
            if k == len(str(picker)): # if the last digit = 1, 2, or 3 then Dumbledore is chosen
                if i == 1 or i == 2 or i == 3:
                    print "The Hufflepuffs called for a fair overseer." ; sleep(1)
                    print "You're working with... Albus Dumbledore!" ; sleep(1)
                    print "His elder wand allows for two guesses each turn!"
                    return [9, "Albus Dumbledore"]    
            k += 1
    if picker >= 1 and picker <= 15: # Harry Potter (common)
        print "You're working with... Harry Potter" ; sleep(1)
        if desired_game == 3: 
            print "You get one initial free guess!"
        return [1, "Harry Potter"]
    elif picker >= 16 and picker <= 30: # Luna Lovegood (common)
        print "You're working with... Luna Lovegood" ; sleep(1)
        if desired_game == 3: 
            print "She is strange. Her wand length is probably odd as well..."
        return [2, "Luna Lovegood"]
    elif picker >= 31 and picker <= 45: # Hagrid (common)
        print "You're working with... Hagrid" ; sleep(1)
        if desired_game == 3: 
            print "He is very large so anything less than 100mm woud not fit in his hand"
        return [3, "Hagrid"]
    elif picker >= 46 and picker <= 60: # Draco Malfoy (common)
        print "You're working with... Draco Malfoy" ; sleep(1)
        if desired_game == 3: 
            print "This trouble maker just lost you 5 points"
        return [4, "Draco Malfoy"]
    elif picker >= 61 and picker <= 70: # Hermione Granger (uncommon)
        print "You're working with... Hermione Granger" ; sleep(1)
        if desired_game == 3: 
            print "10 points to your house!"
        return [5, "Hermione Granger"]
    elif picker >= 71 and picker <= 75: # Ron Weasley (uncommon)
        print "You're working with... Ron Weasley" ; sleep(1)
        if desired_game == 3: 
            print "Eat slugs! (Ron's wand misfired. You lost a guess)"
        return [6, "Ron Weasley"]
    elif picker >= 76 and picker <= 80: # Ron Weasley (uncommon)
        print "You're working with... Ron Weasley" ; sleep(1)
        if desired_game == 3: 
            print "Eat slugs! (Ron's wand worked! House points you earn this turn will be doubled)"
        return [7, "Ron Weasley"]
    elif picker >= 81 and picker <= 90: # Professor Snape (rare)
        print "You're working with... Professor Snape" ; sleep(1)
        if desired_game == 3: 
            print "Detention! -20 points to the other team!"
        return [8, "Professor Snape"]
    elif picker >= 91 and picker <= 99: # Albus Dumbledore (rare)
        print "You're working with... Albus Dumbledore" ; sleep(1)
        if desired_game == 3: 
            print "His elder wand allows for two guesses each turn!"
        return [9, "Albus Dumbledore"]
    else: # Professor Trelawney (rare)
        print "You're working with... Professor Trelawney" ; sleep(1)
        if desired_game == 3: 
            print "Her foresight will show you the first digit!"
        return [10, "Professor Trelawney"]


#*#*#*#*#
# Generates the magic number (calls on the character function to get character too; returns both)
def magic_num_gen(desired_game, char):
    if desired_game == 1 or desired_game == 2:
        magic_num = randint(1,250)
    else:
        if char == 2: # Luna is odd
            magic_num = (randint(1,125) * 2) - 1
        elif char == 3: # Hagrid is big (100-250)
            magic_num = randint(100,250)
        else:
            magic_num = randint(1,250)
    print "\n"
    #print magic_num
    return magic_num


#*#*#*#*#
# Game3: playing for the house cup
def game_1_2_3(chosen_char, magic_num, desired_game, char_num, current_player_house, current_player_turn):
    if desired_game == 3:
        print "Player " + str(current_player_turn + 1) + "'s turn:"
    guesses_used = 0
    pointies = 0
    ravencloser = 1000
    dumby_counter = 0
    if desired_game == 3 and char_num == 1: # Harry's special ability
        guesses_used = -1 
    elif desired_game == 3 and char_num == 6: # Ron's mishap ability
        guesses_used = 1
    while True:
        if guesses_used == 1:
            print "You've made 1 guess."
        elif guesses_used == 0 or guesses_used > 1:
            print "You've made " + str(guesses_used) + " guesses."
        if desired_game == 3 and chosen_char == "Hagrid":
            guess = raw_input("Guess " + chosen_char + "'s wand length (from 100mm to 250mm): ")
        elif desired_game == 3 and chosen_char == "Luna Lovegood":
            guess = raw_input("Guess " + chosen_char + "'s ODD wand length (from 1mm to 250mm): ")
        elif desired_game == 3 and chosen_char == "Professor Trelawney":
            numstring = str(magic_num)
            k = 0
            for i in numstring:
                if k == 0:
                    print "the first digit is " + i
                k += 1
            guess = raw_input("Guess " + chosen_char + "'s wand length (from 1mm to 250mm): ")
        else:
            guess = raw_input("Guess " + chosen_char + "'s wand length (from 1mm to 250mm): ")
        guesses_used += 1
        dumby_counter += 1
        if desired_game == 3 and chosen_char == "Albus Dumbledore":
            if dumby_counter % 2 != 0:
                guesses_used -= 1
        if guess in str(range(1,250)):
            guess = int(guess)
            if desired_game == 2 or desired_game == 3:
                pointies += abs(guess - magic_num)
            if guess == magic_num:
                print('\n'*100)
                if guesses_used >= 6:
                    print "\n\nGood job! You got the magic number!"
                else:
                    print "\n\nWow! You're even better than Mr. Ollivander!"
                print "\n" ; sleep(1)
                print "that took " + str(guesses_used) + " guesses."
                return [guesses_used, pointies]
            elif guess > magic_num:
                print "\n\n" + chosen_char + "'s wand length is LESS THAN " + str(guess) + "."
            else:
                print "\n\n" + chosen_char + "'s wand length is GREATER THAN " + str(guess) + "."
            if desired_game == 3 and current_player_house == "Raven": # Ravenclaw House ability
                if ravencloser >= abs(guess - magic_num):
                    print "Ravenclaw says you're getting CLOSER"
                else:
                    print "Ravenclaw says you're getting FURTHER"
                ravencloser = abs(guess - magic_num)
        else:    
            print "\nThat is not a valid guess."        


#*#*#*#*#
# This is how we do it (print the scores)
def print_scores(top_scores):
    print('\n'*100)
    print "\nTop Scores:"
    i = 0
    for row in top_scores:
        i +=1
        print str(i) + ". " + "  ".join(row)


#*#*#*#*#
# convert the game scores to ints
def maker1(x):
    top_score_list1[x][0] = int(top_score_list1[x][0])


#*#*#*#*#
#convert the game scores to str
def shaker1(x):
    top_score_list1[x][0] = str(top_score_list1[x][0])


#*#*#*#*#
def high_score1(game_score, top_score_list1):
    num_top_scores = 10 # max number of top scores the game will show
    if len(top_score_list1) >= num_top_scores:
        if game_score <= int(top_score_list1[num_top_scores - 1][0]):
            initials = raw_input("Enter your initials\n" + str(game_score) + "   ")
            top_score_list1.remove([top_score_list1[num_top_scores - 1][0],top_score_list1[num_top_scores - 1][1]])
            top_score_list1.append([str(game_score), str(initials)])
    else:
        initials = raw_input("Enter your initials\n" + str(game_score) + "   ")
        top_score_list1.append([str(game_score), str(initials)])
    map(maker1, range(0,len(top_score_list1)))
    top_score_list1 = sorted(top_score_list1, key=itemgetter(0))    
    map(shaker1, range(0,len(top_score_list1)))
    return top_score_list1


#*#*#*#*#
# convert the game scores to ints
def maker2(x):
    top_score_list2[x][0] = int(top_score_list2[x][0])


#*#*#*#*#
#convert the game scores to str
def shaker2(x):
    top_score_list2[x][0] = str(top_score_list2[x][0])
    

#*#*#*#*#
def high_score2(points, top_score_list2):
    num_top_scores2 = 10 # max number of top scores the game will show
    if len(top_score_list2) >= num_top_scores2:
        if points >= int(top_score_list2[num_top_scores2 - 1][0]):
            initials = raw_input("Enter your house\n" + str(points) + "   ")
            top_score_list2.remove([top_score_list2[num_top_scores2 - 1][0],top_score_list2[num_top_scores2 - 1][1]])
            top_score_list2.append([str(points), str(initials)])
    else:
        initials = raw_input("Enter your house\n" + str(points) + "   ")
        top_score_list2.append([str(points), str(initials)])
    map(maker2, range(0,len(top_score_list2)))
    top_score_list2 = sorted(top_score_list2, reverse=True, key=itemgetter(0))    
    map(shaker2, range(0,len(top_score_list2)))
    return top_score_list2

#*#*#*#*#
# play again function
def play_again():
    replayer = "p"
    while replayer != "y" and replayer != "n":
        replayer = raw_input("Do you want to play again? (y/n) ")
        if replayer != "y" and replayer != "Y" and replayer != "n" and replayer != "N":
            print "Invalid response."
        elif replayer == "y" or replayer == "Y":
            return True
        else:
            return False


#*#*#*#*#
# points calculator (game_score is a list: [guesses_used, pointies])
def pointcalculator(game_score, char_num):
    if game_score[1] < 1:
        game_score[1] = 1
    if game_score[0] < 1:
        game_score[0] = 1
    if char_num == 1: # Harry Potter's special ability
        game_score[1] /= 1.25 #changing pointies because of first guess not counting
    if char_num == 9: # Albus Dumbledore's special ability
        game_score[1] /= 2.5 #changing pointies because of getting double guesses per turn
    calc = int(12500 / (game_score[0] * game_score[1]))
    if calc > 50:
        calc = 50
    print "You earned " + str(calc) + " points!\n"
    return calc


#*#*#*#*#
# calculates changes in the house cup points: points = points the person just scored;
# char_num = a number that identifies the char (HP, dumby, Ron, etc.); current_standings = a list 
# for the current amount of points each player has [player1, player2]; players_turn = which player's turn
# current_player_house = house of the current player
def house_cup_calc(points, char_num, current_standings, players_turn, current_player_house):
    if players_turn % 2 != 0:
        player = 0 #player1 on odd
    else:
        player = 1 #player2 on even
    var_points = points
    # Gryffindor House ability
    if current_player_house == "Gryff" and (char_num == 1 or char_num == 2 or char_num == 3 or char_num == 5 or char_num == 6 or char_num == 7 or char_num == 9):
        current_standings[player] += 5
    # Slytherin ability (Snape)
    elif current_player_house == "Slyth" and (char_num == 8):
        current_standings[player] += 5
        if player == 0:
            current_standings[player + 1] -= 5
        else:
            current_standings[player - 1] -= 5        
    if char_num == 4: # Draco's special ability and Slytherin ability
        if current_player_house == "Slyth":
            current_standings[player] += 5
            if player == 0:
                current_standings[player + 1] -= 10
            else:
                current_standings[player - 1] -= 10
        else:
            var_points -= 5
    if char_num == 5: # Hermione's special ability
        var_points += 10
    if char_num == 7: # Ron's second special ability
        var_points *= 2
    if char_num == 8: # Snape's special ability
        if player == 0:
            current_standings[player + 1] -= 20
        else:
            current_standings[player - 1] -= 20    
    current_standings[player] += var_points
    if current_standings[0] < 0: # you can't have negative house points
        current_standings[0] = 0
    if current_standings[1] < 0:
        current_standings[1] = 0


#*#*#*#*#
# print the house cup standings
def house_cup_printer(current_standings, players_turn, players_houses, total_rounds):
    if players_turn % 2 == 0: # only print after each player takes a turn
        hc_print_list.append([str(current_standings[0]), str(current_standings[1])])
        print "\n\nHouse Cup Standings:"
        print "round(of " + str(total_rounds) + ")   " + players_houses[0] + "   " + players_houses[1]
        i = 0
        for row in hc_print_list:
            if len(str(row[0])) < 3:
                i += 1
                print "   " + str(i) + ".          " + "      ".join(row)
            else:
                i += 1
                print "   " + str(i) + ".          " + "     ".join(row)
        if i < total_rounds:
            if int(hc_print_list[i - 1][0]) > int(hc_print_list[i - 1][1]):
                difference = int(hc_print_list[i - 1][0]) - int(hc_print_list[i - 1][1])
                print str(players_houses[0]) + " is beating " + str(players_houses[1]) + " by " + str(difference) + " points!"
            elif int(hc_print_list[i - 1][0]) < int(hc_print_list[i - 1][1]):
                difference = int(hc_print_list[i - 1][1]) - int(hc_print_list[i - 1][0])
                print str(players_houses[1]) + " is beating " + str(players_houses[0]) + " by " + str(difference) + " points!"
            else:
                print str(players_houses[0]) + " and " + str(players_houses[1]) + " are tied!"
        else:
            if int(hc_print_list[i - 1][0]) > int(hc_print_list[i - 1][1]):
                print str(players_houses[0]) + " won the House Cup!!"
            elif int(hc_print_list[i - 1][0]) < int(hc_print_list[i - 1][1]):
                print str(players_houses[1]) + " won the House Cup!!"
            else:
                print str(players_houses[0]) + " and " + str(players_house[1]) + " are tied for the House Cup!"    
    raw_input("\n\nPress any key to continue.")


#*#*#*#*#
# calculate the current player's turn
def cpt(players_turn):
    if players_turn % 2 != 0: # player 1
        return 0
    else: #player 2
        return 1
    

#*#*#*#*#
# overall game running function
def overall_game():
    hc_print_list = []
    desired_game = "not again"
    total_rounds = 5
    while desired_game == "not again":
        desired_game = game_menu()
        if desired_game == 4:
            break
        players_turn = 1
        while desired_game != "not again":
            if desired_game == 3 and (players_turn == 1 or players_turn >= (2 * total_rounds + 1)):
                players_houses = pick_houses()
                players_turn = 1
            current_player_turn = cpt(players_turn)
            char = char_picker(desired_game, players_houses[current_player_turn])
            magic_num = magic_num_gen(desired_game, char[0])            
            game_score = game_1_2_3(char[1], magic_num, desired_game, char[0], players_houses[current_player_turn], current_player_turn)
            if desired_game == 1:
                top_scores = high_score1(game_score[0], top_score_list1)
                print_scores(top_scores)
            elif desired_game == 2:
                points = pointcalculator(game_score, char[0])
                top_scores = high_score2(points, top_score_list2)
                print_scores(top_scores)
            else:
                points = pointcalculator(game_score, char[0])
                house_cup_calc(points, char[0], current_standings, players_turn, players_houses[current_player_turn])
                house_cup_printer(current_standings, players_turn, players_houses, total_rounds)
                players_turn += 1 # if odd then player1 turn, if even then player2 turn
            if desired_game == 1 or desired_game == 2 or players_turn >= (2 * total_rounds + 1):
                replay = play_again()
                if replay == False:
                    desired_game = "not again"
            

overall_game()


