# Hello Harry Potter World program in Python
import os
os.system('clear')
print('\n'*100)

from random import randint
from time import sleep
from operator import itemgetter
import sys,time,random

print "\nHELLO HARRY POTTER WORLD!"

top_score_list1 = []
top_score_list2 = []
current_standings = [0, 0]    

## I have a class Hemu!!!
class Player(object):
    def __init__(self, house, overall_score):
        self.house = house
        self.overall_score = overall_score

## More classes Hemu!!!!
class Character(object):
    def __init__(self, name, char_num, char_phase):
        self.name = name
        self.char_num = char_num
        self.phrase = phrase
        self.char_phase = char_phase

## Another class and the player's game state!!
class PlayerState(object):
    def __init__(self, desired_game, char, magic_num, guesses, actual_guesses, pointies, points_this_turn, current_phase):
        self.desired_game = desired_game
        self.char = char
        self.magic_num = magic_num
        self.guesses = guesses
        self.actual_guesses = actual_guesses
        self.pointies = pointies
        self.points_this_turn = points_this_turn
        self.current_phase = current_phase

#add in the changing player class: total actual guesses (will help with the dumbledore thing). Also keep a list of all guesses used so far
#add in the character class: "" to be changed everytime you enter a new function. In each function, the current game state is updated, then the character.current_game_state
#will be called. So if harry is activated in the game state of "game," then in game, the game state is changed to "game." Then the function character.game is called.
#if the current game state ("game") == the game state of harry ("game"), then the following function will be applied. If not, then no function happens and the game continues 
#on its way. This needs to be done at the beginning of each function


harry_potter = Character("Harry Potter", 1, "You get one initial free guess!")
luna_lovegood = Character("Luna Lovegood", 2, "She is strange. Her wand length is probably odd as well...")
hagrid = Character("Hagrid", 3, "He is very large so anything less than 100mm would not fit in his hand")
draco_malfoy = Character("Draco Malfoy", 4, "This trouble maker just lost you 5 points")
hermione_granger = Character("Hermione Granger", 5, "10 points to your house!")
ron_weasley1 = Character("Ron Weasley", 6, "Eat slugs! (Ron's wand misfired. You lost a guess)")
ron_weasley2 = Character("Ron Weasley", 7, "Eat slugs! (Ron's wand worked! House points you earn this turn will be doubled)")
professor_snape = Character("Professor Snape", 8, "Detention! -20 points to the other team!")
albus_dumbledore = Character("Albus Dumbledore", 9, "His elder wand allows for two guesses each turn!")
professor_trelawney = Character("Professor Trelawney", 10, "Her foresight will show you the first digit!")

player1 = Player("", 0)
player2 = Player("", 0)
gen_player = [player1, player2]
player_state = PlayerState("not again", "", 0, 0, 0, 0, 0, "")


#*#*#*#*#
# The function where all the character modifications on the game happen
def character_mod_func():
    if player_state.char.char_phase == player_state.current_phase:
            print 5
            if current_phase == "game": # Harry Potter and Albus Dumbledore


#*#*#*#*#
# The initial game menu
def game_menu():
    print('\n'*100)
    print "\nWhat game would you like to play? (Enter the value)"
    print "1. Classic Mode"
    print "2. House Points High Score"
    print "3. Play for the House Cup (2-player) "
    desired = str(raw_input("4. Quit "))
    while desired != "1" and desired != "2" and desired != "3" and desired != "4":
        print "\nThat is not a valid option" ; sleep(2)
        os.system('clear')
        print "\nWhat game would you like to play? (Enter the value)"
        print "1. Classic Mode"
        print "2. House Points High Score"
        print "3. Play for the House Cup (2-player) "
        desired = str(raw_input("4. Quit "))
    print "\n"
    player_state.desired_game = int(desired)


#*#*#*#*#
# this is what the sorting hat says
# needs to have at least 3-5 different things with a random generator to pick the right one
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
def pick_houses(player1, player2):
    previous_player = 5
    house_list = ["Gryff", "Slyth", "Raven", "Huffl", ""]
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
            #gryffindor: +5 points per every other gryffindor character you work with
        elif player_house == "2":
            print "\nYou have chosen Slytherin House! Team up with other Slytherins to steal points from your opponent."
            #slytherin: -5 to them and +5 to you everytime you work with another slytherin 
            # also rolling draco steals 5 from the other team to give to you
        elif player_house == "3":
            print "\nYou have chosen Ravenclaw House! They will tell you whether you're getting closer or further from the correct answer."
            #ravenclaw: tells you whether you are getting closer or further from the magic number every turn
        else:
            print "\nYou have chosen Hufflepuff House! Although I don't know why you would do that voluntarily."
            #hufflepuff: much higher chance of rolling dumbledore 
        raw_input("\nPress any key to continue.")
        player1.house = house_list[int(previous_player) - 1]
        player2.house = house_list[int(player_house) - 1]
        previous_player = player_house
    
  
#*#*#*#*#
# Picks the character
def char_picker(desired_game, player_state, player_placeholder):
    print('\n'*100)
    picker = randint(1, 110)
    print "\n"
    if desired_game == 3 and player_placeholder.house == "Huffl": # Hufflepuff House ability
        k = 1
        for i in str(picker):
            if k == len(str(picker)): # if the last digit = 1, 2, or 3 then Dumbledore is chosen
                if int(i) in range(1, 4):
                    player_state.char = albus_dumbledore
                    print "The Hufflepuffs called for a fair overseer." ; sleep(1)
                    print "You're working with ... " + player_state.char.name ; sleep(1)
                    print player_state.char.phrase
                    return
            k += 1
    if picker >= 1 and picker <= 15: # Harry Potter (common)
        player_state.char = harry_potter
    elif picker >= 16 and picker <= 30: # Luna Lovegood (common)
        player_state.char = luna_lovegood
    elif picker >= 31 and picker <= 45: # Hagrid (common)
        player_state.char = hagrid
    elif picker >= 46 and picker <= 60: # Draco Malfoy (common)
        player_state.char = draco_malfoy
    elif picker >= 61 and picker <= 70: # Hermione Granger (uncommon)
        player_state.char = hermione_granger
    elif picker >= 71 and picker <= 75: # Ron Weasley (uncommon)
        player_state.char = ron_weasley1
    elif picker >= 76 and picker <= 80: # Ron Weasley (uncommon)
        player_state.char = ron_weasley2
    elif picker >= 81 and picker <= 90: # Professor Snape (rare)
        player_state.char = professor_snape
    elif picker >= 91 and picker <= 100: # Albus Dumbledore (rare)
        player_state.char = albus_dumbledore
    else: # Professor Trelawney (rare)
        player_state.char = professor_trelawney
    print "You're working with ... " + player_state.char.name ; sleep(1)
    if desired_game == 3:
        print player_state.char.phrase


#*#*#*#*#
# Generates the magic number (calls on the character function to get character too; returns both)
def magic_num_gen(desired_game, player_state):
    current_phase = "magic_num_gen"
    player_state.magic_num = randint(1,250)
    if desired_game == 3:
        current_player.character_mod_func()
    print "\n"
    # else:
    #     if player_state.char.char_num == 2: # Luna is odd
    #         player_state.magic_num = (randint(1,125) * 2) - 1
    #     elif player_state.char.char_num == 3: # Hagrid is big (100-250)
    #         player_state.magic_num = randint(100,250)
    #     else:
    #         player_state.magic_num = randint(1,250)
    #print player_state.magic_num


#*#*#*#*#
# Game3: playing for the house cup
def game_1_2_3(desired_game, player_state, player_placeholder, cpt):
    if desired_game == 3:
        print "Player " + str(cpt + 1) + "'s turn:"
    ravencloser = 1000
    dumby_counter = 0
    player_state.guesses = 0
    player_state.pointies = 0
    if desired_game == 3 and player_state.char.char_num == 1: # Harry's special ability
        player_state.guesses = -1 
    elif desired_game == 3 and player_state.char.char_num == 6: # Ron's mishap ability
        player_state.guesses = 1
    while True:
        if player_state.guesses == 1:
            print "You've made 1 guess."
        elif player_state.guesses == 0 or player_state.guesses > 1:
            print "You've made " + str(player_state.guesses) + " guesses."
        if desired_game == 3 and player_state.char.name == "Hagrid":
            guess = raw_input("Guess " + player_state.char.name + "'s wand length (from 100mm to 250mm): ")
        elif desired_game == 3 and player_state.char.name == "Luna Lovegood":
            guess = raw_input("Guess " + player_state.char.name + "'s ODD wand length (from 1mm to 250mm): ")
        elif desired_game == 3 and player_state.char.name == "Professor Trelawney":
            numstring = str(player_state.magic_num)
            k = 0
            for i in numstring:
                if k == 0:
                    print "the first digit is " + i
                k += 1
            guess = raw_input("Guess " + player_state.char.name + "'s wand length (from 1mm to 250mm): ")
        else:
            guess = raw_input("Guess " + player_state.char.name + "'s wand length (from 1mm to 250mm): ")
        player_state.guesses += 1
        dumby_counter += 1
        if desired_game == 3 and player_state.char.name == "Albus Dumbledore":
            if dumby_counter % 2 != 0:
                player_state.guesses -= 1
        if guess in str(range(1,251)):
            guess = int(guess)
            if desired_game == 2 or desired_game == 3:
                player_state.pointies += abs(guess - player_state.magic_num)
            if guess == player_state.magic_num:
                print('\n'*100)
                if player_state.guesses >= 6:
                    print "\n\nGood job! You got the magic number!"
                else:
                    print "\n\nWow! You're even better than Mr. Ollivander!"
                print "\n" ; sleep(1)
                print "that took " + str(player_state.guesses) + " guesses."
                break
            elif guess > player_state.magic_num:
                print "\n\n" + player_state.char.name + "'s wand length is LESS THAN " + str(guess) + "."
            else:
                print "\n\n" + player_state.char.name + "'s wand length is GREATER THAN " + str(guess) + "."
            if desired_game == 3 and player_placeholder.house == "Raven": # Ravenclaw House ability
                if ravencloser >= abs(guess - player_state.magic_num):
                    print "Ravenclaw says you're getting CLOSER"
                else:
                    print "Ravenclaw says you're getting FURTHER"
                ravencloser = abs(guess - player_state.magic_num)
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
def high_score1(player_state, top_score_list1):
    num_top_scores = 10 # max number of top scores the game will show
    if len(top_score_list1) >= num_top_scores:
        if player_state.guesses <= int(top_score_list1[num_top_scores - 1][0]):
            initials = raw_input("Enter your initials\n" + str(player_state.guesses) + "   ")
            top_score_list1.remove([top_score_list1[num_top_scores - 1][0],top_score_list1[num_top_scores - 1][1]])
            top_score_list1.append([str(player_state.guesses), str(initials)])
    else:
        initials = raw_input("Enter your initials\n" + str(player_state.guesses) + "   ")
        top_score_list1.append([str(player_state.guesses), str(initials)])
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
def high_score2(player_state, top_score_list2):
    num_top_scores2 = 10 # max number of top scores the game will show
    if len(top_score_list2) >= num_top_scores2:
        if player_state.points_this_turn >= int(top_score_list2[num_top_scores2 - 1][0]):
            initials = raw_input("Enter your house\n" + str(player_state.points_this_turn) + "   ")
            top_score_list2.remove([top_score_list2[num_top_scores2 - 1][0],top_score_list2[num_top_scores2 - 1][1]])
            top_score_list2.append([str(player_state.points_this_turn), str(initials)])
    else:
        initials = raw_input("Enter your house\n" + str(player_state.points_this_turn) + "   ")
        top_score_list2.append([str(player_state.points_this_turn), str(initials)])
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
def pointcalculator(player_state):
    if player_state.pointies < 1:
        player_state.pointies = 1
    if player_state.guesses < 1:
        player_state.guesses = 1
    if player_state.char.char_num == 1: # Harry Potter's special ability
        player_state.pointies /= 1.25 #changing pointies because of first guess not counting
    if player_state.char.char_num == 9: # Albus Dumbledore's special ability
        player_state.pointies /= 2.5 #changing pointies because of getting double guesses per turn
    player_state.points_this_turn = int(25000 / (player_state.guesses * (player_state.pointies + 100)))
    if player_state.points_this_turn > 50:
        player_state.points_this_turn = 50
    print "You earned " + str(player_state.points_this_turn) + " points!\n"


#*#*#*#*#
# calculates changes in the house cup points: points = points the person just scored;
# char_num = a number that identifies the char (HP, dumby, Ron, etc.); current_standings = a list 
# for the current amount of points each player has [player1, player2]; players_turn = which player's turn
# current_player_house = house of the current player
def house_cup_calc(player_state, gen_player, cpt):
    # Gryffindor House ability
    if gen_player[cpt].house == "Gryff" and (player_state.char.char_num in [1, 3, 5, 6, 7, 9]):
        gen_player[cpt].overall_score += 5
    # Slytherin ability (Snape)
    elif gen_player[cpt].house == "Slyth" and (player_state.char.char_num == 8):
        gen_player[cpt].overall_score += 5
        if cpt == 0:
            gen_player[cpt + 1].overall_score -= 5
        else:
            gen_player[cpt - 1].overall_score -= 5        
    if player_state.char.char_num == 4: # Draco's special ability and Slytherin ability
        if gen_player[cpt].house == "Slyth":
            gen_player[cpt].overall_score += 5
            if player == 0:
                gen_player[cpt + 1].overall_score -= 10
            else:
                gen_player[cpt - 1].overall_score -= 10
        else:
            gen_player[cpt].overall_score -= 5
    if player_state.char.char_num == 5: # Hermione's special ability
        gen_player[cpt].overall_score += 10
    if player_state.char.char_num == 7: # Ron's second special ability
        gen_player[cpt].points_this_turn *= 2
    if player_state.char.char_num == 8: # Snape's special ability
        if cpt == 0:
            gen_player[cpt + 1].overall_score -= 20
        else:
            gen_player[cpt - 1].overall_score -= 20    
    gen_player[cpt].overall_score += player_state.points_this_turn
    if gen_player[0].overall_score < 0: # you can't have negative house points
        gen_player[0].overall_score = 0
    if gen_player[1].overall_score < 0:
        gen_player[1].overall_score = 0


#*#*#*#*#
# print the house cup standings
def house_cup_printer(gen_player, cpt, total_rounds, hc_print_list):
    if cpt == 1: # only print after player 2's (cpt = 1) turn
        hc_print_list.append([str(gen_player[0].overall_score), str(gen_player[1].overall_score)])
        print "\n\nHouse Cup Standings:"
        print "round(of " + str(total_rounds) + ")   " + gen_player[0].house + "   " + gen_player[1].house
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
                print str(gen_player[0].house) + " is beating " + str(gen_player[1].house) + " by " + str(difference) + " points!"
            elif int(hc_print_list[i - 1][0]) < int(hc_print_list[i - 1][1]):
                difference = int(hc_print_list[i - 1][1]) - int(hc_print_list[i - 1][0])
                print str(gen_player[1].house) + " is beating " + str(gen_player[0].house) + " by " + str(difference) + " points!"
            else:
                print str(gen_player[0].house) + " and " + str(gen_player[1].house) + " are tied!"
        else:
            if int(hc_print_list[i - 1][0]) > int(hc_print_list[i - 1][1]):
                print str(gen_player[0].house) + " won the House Cup!!"
            elif int(hc_print_list[i - 1][0]) < int(hc_print_list[i - 1][1]):
                print str(gen_player[1].house) + " won the House Cup!!"
            else:
                print str(gen_player[0].house) + " and " + str(gen_player[1].house) + " tied for the House Cup!"    
    raw_input("\n\nPress any key to continue.")


#*#*#*#*#
# calculate the current player's turn
def current_player_turn(players_turn):
    if players_turn % 2 != 0: # player 1
        return 0
    else: #player 2
        return 1
    

#*#*#*#*#
# overall game running function
def overall_game():
    hc_print_list = []
    total_rounds = 5
    while player_state.desired_game == "not again":
        game_menu()
        if player_state.desired_game == 4:
            break
        players_turn = 1
        while player_state.desired_game != "not again":
            if player_state.desired_game == 3 and (players_turn == 1 or players_turn >= (2 * total_rounds + 1)):
                pick_houses(player1, player2)
                players_turn = 1
            cpt = current_player_turn(players_turn)
            char_picker(player_state.desired_game, player_state, gen_player[cpt])
            magic_num_gen(player_state.desired_game, player_state)            
            game_1_2_3(player_state.desired_game, player_state, gen_player[cpt], cpt)
            if player_state.desired_game == 1:
                high_score1(player_state, top_score_list1)
                print_scores(top_score_list1)
            elif player_state.desired_game == 2:
                pointcalculator(player_state)
                high_score2(player_state, top_score_list2)
                print_scores(top_score_list2)
            else:
                pointcalculator(player_state)
                house_cup_calc(player_state, gen_player, cpt)
                house_cup_printer(gen_player, cpt, total_rounds, hc_print_list)
                players_turn += 1 # if odd then player1 turn, if even then player2 turn
            if player_state.desired_game == 1 or player_state.desired_game == 2 or players_turn >= (2 * total_rounds + 1):
                hc_print_list = []
                player1.overall_score = 0
                player2.overall_score = 0
                replay = play_again()
                if replay == False:
                    player_state.desired_game = "not again"
            

overall_game()


#print out what you got points for on the turn (on the page with the house cup standings)
#add background music
#add pictures and a display
