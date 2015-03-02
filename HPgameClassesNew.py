# Hello Harry Potter World program in Python
import os
os.system('cls')

from random import randint
from time import sleep
from operator import itemgetter
import sys, time, random

print "\nHELLO HARRY POTTER WORLD!"

top_score_list1 = []
top_score_list2 = []
current_standings = [0, 0] 


#                               view of the classes (two main ones with two smaller ones accessed through the main ones):
#                                  gen_player  <-- a list containing the player class: player 1 and player 2 (gen_player[0] = player1)
#                                    /      \
#        gen_player[0] = player1 <---        ---> gen_player[1] = player2  <-- each player is a class which includes house and the overall score
#             /        \                                /           \
# player1.house  and  player1.overall_score    player2.house  and  player2.overall_score      ## overall score is just a number but the house leads into the house class
#           |
#           |
# player1.house  <--- accesses the house class
#           ^
#           |--- (house_name, house_id, etc.)
#           | 
# player1.house.house_name  <-- gives the house name
# player1.house.house_id  <--- gives the house id
#
#
#
#                                                   the class that holds the state of all things happening to the current player;
#                                player_state  <---  has a bunch of different things but also accesses the character class
#                              /    |           |      \       \
#                             /     |           |       \       \
#     player_state.desired_game   .magic_num  .guesses  ...    player_state.char  <--- accesses the character class
#                                                                            ^
#                                                                            |--- (name, char_id, etc.)
#                                                                            |
#                                                              player_state.char.name  <--- gives the character name
#                                                              player_state.char.char_id
#                                                              player_state.char.phrase
# 
#
#to be done still:
#print out what you got points for on the turn (on the page with the house cup standings)
#add background music
# add a voldemort character (if slyth then +15, otherwise you can have a normal turn or you can duel him)


## I have a class Hemu!!!
class Player(object):
    def __init__(self, house, overall_score):
        self.house = house # the house. This is the access point to the house class
        self.overall_score = overall_score # keeps track of the overall score of each player

## class for the different houses (to be used in the player class)
class House(object):
    def __init__(self, house_name, house_id, phrase, house_phase, house_number):
        self.house_name = house_name # the name of the house (appears in the house cup standings)
        self.house_id = house_id # the id number of the house
        self.phrase = phrase # the phrase that is said when the house is picked
        self.house_phase = house_phase # the phase of the game that the house ability is activated (may have multiple times)
        self.house_number = house_number # for huffl:nothing / raven:closer or further / gryff:point mod amt / slyth:point mod amt

## More classes Hemu!!!!
class Character(object):
    def __init__(self, name, char_id, phrase, char_phase):
        self.name = name # name of the character
        self.char_id = char_id # the number that identifies the character
        self.phrase = phrase # the phrase that is said when the character is picked
        self.char_phase = char_phase # the time of the game when the character can activate its ability (may have multiple times)

## Another class and the player's game state!!
class PlayerState(object):
    def __init__(self, desired_game, char, magic_num, guesses, actual_guesses, guesses_list, pointies, points_this_turn, current_phase, cpt):
        self.desired_game = desired_game # either game 1, 2, or 3
        self.char = char # this accesses the character class
        self.magic_num = magic_num
        self.guesses = guesses # the possibly modified number of guesses this turn
        self.actual_guesses = actual_guesses # the real number of guesses used this turn (unmodified)
        self.guesses_list = guesses_list # the list of all guesses made
        self.pointies = pointies # the cumulative difference between the magic_num and the guess
        self.points_this_turn = points_this_turn # the points that the current player has racked up on this current turn only
        self.current_phase = current_phase #the function of the game that is currently running
        self.cpt = cpt #current player's turn



#for use in house id
dummy = 0
gryff = 1
slyth = 2
raven = 3
huffl = 4

#house initiation
#gryffindor: +5 points per every other gryffindor character you work with
#slytherin: -5 to them and +5 to you everytime you work with another slytherin also rolling draco steals 5 from the other team to give to you
#ravenclaw: tells you whether you are getting closer or further from the magic number every turn
#hufflepuff: much higher chance of rolling dumbledore
gryffindor = House("Gryff", gryff, "You have chosen Gryffindor House! Team up with other Gryffindors for bonus points.", ["hc_calc"], 5)
slytherin = House("Slyth", slyth, "You have chosen Slytherin House! Team up with other Slytherins to steal points from your opponent.", ["char_picker", "hc_calc"], 5)
ravenclaw = House("Raven", raven, "You have chosen Ravenclaw House! They will tell you whether you're getting closer or further from the correct answer.", ["game"], 1000)
hufflepuff = House("Huffl", huffl, "You have chosen Hufflepuff House! Although I don't know why you would do that voluntarily.", ["char_picker"], 0)
house_dummy = House("", dummy, "", [], 0)



#for use in character id
har = 1
lun = 2
hag = 3
dra = 4
her = 5
ron1 = 6
ron2 = 7
sna = 8
dum = 9
tre = 10
            
#character initiation
harry_potter = Character("Harry Potter", har, "You get one initial free guess!", ["game", "point_calculator"])
luna_lovegood = Character("Luna Lovegood", lun, "She is strange. Her wand length is probably odd as well...", ["magic_num_gen", "game_later"])
hagrid = Character("Hagrid", hag, "He is very large so anything less than 100mm would not fit in his hand", ["magic_num_gen", "game_later"])
draco_malfoy = Character("Draco Malfoy", dra, "This trouble maker just lost you 5 points", ["hc_calc"])
hermione_granger = Character("Hermione Granger", her, "10 points to your house!", ["hc_calc"])
ron_weasley1 = Character("Ron Weasley", ron1, "Eat slugs! (Ron's wand misfired. You lost a guess)", ["game"])
ron_weasley2 = Character("Ron Weasley", ron2, "Eat slugs! (Ron's wand worked! House points you earn this turn will be doubled)", ["hc_calc"])
professor_snape = Character("Professor Snape", sna, "Detention! -20 points to the other team!", ["hc_calc"])
albus_dumbledore = Character("Albus Dumbledore", dum, "His elder wand allows for two guesses each turn!", ["game", "point_calculator"])
professor_trelawney = Character("Professor Trelawney", tre, "Her foresight will show you the first digit!", ["game"])
character_dummy = Character("", dummy, "", [])

#score mods for the few characters who affect the score
hermione_score_mod = 10 #hermione gives +10 points to your house
ron_score_mod = 2 #ron's x2 score mod
draco_score_mod = 5 #draco gives -5 points to either your house or the opponents (depends on whether you're slytherin or not)
snape_score_mod = 20 #snape gives -20 points to the opponent's house



#player and game state initiation
player1 = Player(house_dummy, 0)
player2 = Player(house_dummy, 0)
gen_player = [player1, player2]
player_state = PlayerState("not again", character_dummy, 0, 0, 0, [], 0, 0, [], 0)



#*#*#*#*#
# The function where all the character modifications on the game happen
def character_mod_func(gen_player, player_state):
    #determine if in the proper game and phase of game
    if player_state.desired_game == 3 and player_state.current_phase in player_state.char.char_phase:
        if player_state.current_phase == "char_picker":
            #nothing for now
            pass

        elif player_state.current_phase == "magic_num_gen": # Luna Lovegood and Hagrid
            if player_state.char.char_id == lun: # Luna is odd
                player_state.magic_num = (randint(1,125) * 2) - 1
            elif player_state.char.char_id == hag: # Hagrid is big (100-250)
                player_state.magic_num = randint(100,250)
        
        elif player_state.current_phase == "game": # Harry Potter, Ron's mishap, Albus Dumbledore, and Professor Trelawney
            if player_state.char.char_id == har and player_state.actual_guesses == 0: # Harry's special ability (one free guess)
                player_state.guesses = -1 
            elif player_state.char.char_id == ron1 and player_state.actual_guesses == 0: # Ron's mishap ability (lose a guess)
                player_state.guesses = 1
            elif player_state.char.char_id == dum and player_state.actual_guesses % 2 != 0: # Dumbledore's special ability (every other guess is free)
                player_state.guesses -= 1
            elif player_state.char.char_id == tre: # Trelawney's special ability of foresight
                numstring = str(player_state.magic_num)
                k = 0
                for i in numstring:
                    if k == 0:
                        print "the first digit is " + i
                    k += 1
        
        elif player_state.current_phase == "game_later": # Hagrid's and Luna's special message for guessing
            if player_state.char.char_id == lun:
                character_dummy.phrase = "Guess " + player_state.char.name + "'s ODD wand length (from 1mm to 250mm): "
            elif player_state.char.char_id == hag:
                character_dummy.phrase = "Guess " + player_state.char.name + "'s wand length (from 100mm to 250mm): "

        elif player_state.current_phase == "point_calculator":
            player_state.pointies = 0
            if player_state.char.char_id == har: # Harry changes calculations because he gives first guess free
                for i in range(0,len(player_state.guesses_list)):
                    if i > 0:
                        player_state.pointies += abs(player_state.guesses_list[i] - player_state.magic_num)
            if player_state.char.char_id == dum: # Dumbledore changes calculations because he gives double guesses per turn
                for i in range(0,len(player_state.guesses_list)):
                    if i % 2 != 0:
                        player_state.pointies += abs(player_state.guesses_list[i] - player_state.magic_num)

        elif player_state.current_phase == "hc_calc": # Hermione Granger, Ron's other ability (the 2x points one), Draco Malfoy, and Professor Snape
            if player_state.char.char_id == her: # Hermione
                gen_player[player_state.cpt].overall_score += hermione_score_mod # Hermione gives +10 points to your house
            if player_state.char.char_id == ron2: # Ron's (good) ability
                player_state.points_this_turn *= ron_score_mod # Ron grants x2 points for this turn  
            if player_state.char.char_id == dra: # Draco
                if gen_player[player_state.cpt].house.house_id == slyth:
                    gen_player[player_state.cpt].overall_score += draco_score_mod # if you're in slytherin then draco gives +5 to you
                    if player == 0:
                        gen_player[player_state.cpt + 1].overall_score -= draco_score_mod # and draco will take 5 points from the other team
                    else:
                        gen_player[player_state.cpt - 1].overall_score -= draco_score_mod
                else:
                    gen_player[player_state.cpt].overall_score -= draco_score_mod 
            if player_state.char.char_id == 8: # Snape
                if player_state.cpt == 0:
                    gen_player[player_state.cpt + 1].overall_score -= snape_score_mod # snape makes the other team lose 20 points
                else:
                    gen_player[player_state.cpt - 1].overall_score -= snape_score_mod                                   


#*#*#*#*#
# The function where all the house modifications on the game happen
def house_mod_func(gen_player, player_state):
    if player_state.desired_game == 3 and player_state.current_phase in gen_player[player_state.cpt].house.house_phase:
        if player_state.current_phase == "char_picker":
            if gen_player[player_state.cpt].house.house_id == huffl: # Hufflepuff House ability
                huffl_picker = randint(1,8)
                if huffl_picker in range(1, 3):
                    player_state.char = albus_dumbledore # dumbledore
                    print "The Hufflepuffs called for a fair overseer." ; sleep(1)        
            if gen_player[player_state.cpt].house.house_id == slyth and player_state.char.char_id == dra: # in slytherin and char is draco
                player_state.char.phrase = "This trouble maker just stole 5 points for you, his fellow Slytherin."

        elif player_state.current_phase == "magic_num_gen":
            # nothing for now
            pass

        elif player_state.current_phase == "game":
            # nothing for now
            pass

        elif player_state.current_phase == "game_later":
                if gen_player[player_state.cpt].house.house_id == raven: # Ravenclaw House ability
                    if gen_player[player_state.cpt].house.house_number >= abs(player_state.guess_list[len(guess_list) - 1] - player_state.magic_num):
                        print "Ravenclaw says you're getting CLOSER"
                    else:
                        print "Ravenclaw says you're getting FURTHER"
                    gen_player[player_state.cpt].house.house_number = abs(player_state.guess_list[len(guess_list) - 1] - player_state.magic_num)

        elif player_state.current_phase == "point_calculator":
            # nothing for now
            pass

        elif player_state.current_phase == "hc_calc":
            # Gryffindor House ability
            if gen_player[player_state.cpt].house.house_id == gryff and (player_state.char.char_id in [har, hag, her, ron1, ron2, dum]): # Harry, Hagrid, Hermione, both Rons, and Dumbledore
                gen_player[player_state.cpt].overall_score += gen_player[player_state.cpt].house.house_number # +5 points for teaming up with fellow gryffs
            # Slytherin House ability
            elif gen_player[player_state.cpt].house.house_id == slyth and (player_state.char.char_id in [dra, sna]): # Slytherin with Draco or Snape
                gen_player[player_state.cpt].overall_score += gen_player[player_state.cpt].house.house_number # +5 points for teaming up with fellow slyths
                if player_state.cpt == 0:
                    gen_player[player_state.cpt + 1].overall_score -= gen_player[player_state.cpt].house.house_number # -5 points to other team
                else:
                    gen_player[player_state.cpt - 1].overall_score -= gen_player[player_state.cpt].house.house_number     
 


#*#*#*#*#
# The initial game menu
def game_menu():
    desired = "5"
    while desired not in str([1, 2, 3, 4]):
        os.system('cls')
        print "\nWhat game would you like to play? (Enter the value)"
        print "1. Classic Mode"
        print "2. House Points High Score"
        print "3. Play for the House Cup (2-player) "
        desired = raw_input("4. Quit ")
        if desired not in str(range(0,5)):
            print "\nThat is not a valid option" ; sleep(2)
        else:
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
def pick_houses(gen_player, player_state):
    previous_player = "5"
    house_list = [gryffindor, slytherin, ravenclaw, hufflepuff] 
    for i in range(0,2):
        player_house = "5" #needs to be in here to allow proper iteration through the while loop for player2
        os.system('cls')
        print "PLAYER " + str(i + 1) + ":" ; sleep(1)
        print "So you want to play for the House Cup. But first you need to be sorted into the proper house..."
        print "\n"
        sorting_hat()
        while player_house not in str(range(0,5)) or player_house == previous_player:
            print "\n\n"
            print "1. Gryffindors who work together exude courage. Teaming up with them is bound to gain you some extra points."
            print "2. Slytherin's underhandedness is unmatched. They may be able to do something sneaky to your opponent for you."
            print "3. Ravenclaws are renowned for their intelligence. I'm sure they can help you solve the problem even faster."
            print "4. Hufflepuff: nobody actually knows what they are good at. However, they do believe in fairness, whatever that means..."
            player_house = raw_input("\nWhat house are you destined to be in (enter the number)? ")
            if player_house not in str(range(0,5)) or player_house == previous_player:
                print "\nThat is not a valid option" ; sleep(1) 
                os.system('cls')
        gen_player[i].house = house_list[int(player_house) - 1]
        print "\n" + gen_player[i].house.phrase
        previous_player = player_house
        raw_input("\nPress any key to continue.")
    
  
#*#*#*#*#
# Picks the character
def char_picker(gen_player, player_state):
    player_state.current_phase = "char_picker"
    os.system('cls')
    picker = randint(1, 110)
    print "\n"
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
    ##
    house_mod_func(gen_player, player_state) # Hufflepuff House ability
    ##
    print "You're working with ... " + player_state.char.name ; sleep(1)
    if player_state.desired_game == 3:
        print player_state.char.phrase


#*#*#*#*#
# Generates the magic number
def magic_num_gen(gen_player, player_state):
    player_state.magic_num = randint(1,250)
    ##
    player_state.current_phase = "magic_num_gen"
    character_mod_func(gen_player, player_state)
    ##
    print "\n"
    #print player_state.magic_num


#*#*#*#*#
# All 3 games use this function
def game_1_2_3(gen_player, player_state):
    if player_state.desired_game == 3:
        print "Player " + str(player_state.cpt + 1) + "'s turn:"
    ravencloser = 1000
    player_state.guesses = 0
    player_state.guesses_list = []
    while True:
        ##
        player_state.current_phase = "game"
        character_mod_func(gen_player, player_state)
        ##
        if player_state.guesses == 1:
            print "You've made 1 guess."
        elif player_state.guesses == 0 or player_state.guesses > 1:
            print "You've made " + str(player_state.guesses) + " guesses."
        character_dummy.phrase = "Guess " + player_state.char.name + "'s wand length (from 1mm to 250mm): "
        ##
        player_state.current_phase = "game_later"
        character_mod_func(gen_player, player_state)
        ##
        print character_dummy.phrase, # normally is: "guess the wand length (from 1mm to 250mm)"
        guess = raw_input()
        player_state.guesses += 1
        player_state.actual_guesses += 1
        if guess in str(range(1,251)):
            guess = int(guess)
            player_state.guesses_list.append(guess)
            if guess == player_state.magic_num:
                os.system('cls')
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
            ##
            house_mod_func(gen_player, player_state) # ravenclaw
            ##
        else:    
            print "\nThat is not a valid guess."        


#*#*#*#*#
# This is how we do it (print the scores)
def print_scores(top_scores):
    os.system('cls')
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
def pointcalculator(gen_player, player_state):
    player_state.pointies = 0
    for each_guess in player_state.guesses_list:
        player_state.pointies += abs(each_guess - player_state.magic_num)
    ##
    player_state.current_state = "point_calculator"
    character_mod_func(gen_player, player_state)
    ##
    if player_state.pointies < 1:
        player_state.pointies = 1
    if player_state.guesses < 1:
        player_state.guesses = 1
    player_state.points_this_turn = int(25000 / (player_state.guesses * (player_state.pointies + 100)))
    if player_state.points_this_turn > 50:
        player_state.points_this_turn = 50
    print "You earned " + str(player_state.points_this_turn) + " points!\n"


#*#*#*#*#
# calculates changes in the house cup points
def house_cup_calc(gen_player, player_state):
    ##
    player_state.current_phase = "hc_calc"
    character_mod_func(gen_player, player_state)
    house_mod_func(gen_player, player_state)
    ##
    gen_player[player_state.cpt].overall_score += player_state.points_this_turn
    if gen_player[0].overall_score < 0: # you can't have negative house points
        gen_player[0].overall_score = 0
    if gen_player[1].overall_score < 0:
        gen_player[1].overall_score = 0


#*#*#*#*#
# print the house cup standings
def house_cup_printer(gen_player, player_state, total_rounds, hc_print_list):
    if player_state.cpt == 1: # only print after player 2's (cpt = 1) turn
        hc_print_list.append([str(gen_player[0].overall_score), str(gen_player[1].overall_score)])
        print "\n\nHouse Cup Standings:"
        print "round(of " + str(total_rounds) + ")   " + gen_player[0].house.house_name + "   " + gen_player[1].house.house_name
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
                print str(gen_player[0].house.house_name) + " is beating " + str(gen_player[1].house.house_name) + " by " + str(difference) + " points!"
            elif int(hc_print_list[i - 1][0]) < int(hc_print_list[i - 1][1]):
                difference = int(hc_print_list[i - 1][1]) - int(hc_print_list[i - 1][0])
                print str(gen_player[1].house.house_name) + " is beating " + str(gen_player[0].house.house_name) + " by " + str(difference) + " points!"
            else:
                print str(gen_player[0].house.house_name) + " and " + str(gen_player[1].house.house_name) + " are tied!"
        else:
            if int(hc_print_list[i - 1][0]) > int(hc_print_list[i - 1][1]):
                print str(gen_player[0].house.house_name) + " won the House Cup!!"
            elif int(hc_print_list[i - 1][0]) < int(hc_print_list[i - 1][1]):
                print str(gen_player[1].house.house_name) + " won the House Cup!!"
            else:
                print str(gen_player[0].house.house_name) + " and " + str(gen_player[1].house.house_name) + " tied for the House Cup!"    
    raw_input("\n\nPress any key to continue.")


#*#*#*#*#
# calculate the current player's turn
def current_player_turn(players_turn):
    if players_turn % 2 != 0: # player 1
        player_state.cpt = 0
    else: #player 2
        player_state.cpt = 1
    

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
                pick_houses(gen_player, player_state)
                players_turn = 1
            current_player_turn(players_turn)
            char_picker(gen_player, player_state)
            magic_num_gen(gen_player, player_state)            
            game_1_2_3(gen_player, player_state)
            if player_state.desired_game == 1:
                high_score1(player_state, top_score_list1)
                print_scores(top_score_list1)
            elif player_state.desired_game == 2:
                pointcalculator(gen_player, player_state)
                high_score2(player_state, top_score_list2)
                print_scores(top_score_list2)
            else:
                pointcalculator(gen_player, player_state)
                house_cup_calc(gen_player, player_state)
                house_cup_printer(gen_player, player_state, total_rounds, hc_print_list)
                players_turn += 1 # if odd then player1 turn, if even then player2 turn
            if player_state.desired_game == 1 or player_state.desired_game == 2 or players_turn >= (2 * total_rounds + 1):
                hc_print_list = []
                player1.overall_score = 0
                player2.overall_score = 0
                replay = play_again()
                if replay == False:
                    player_state.desired_game = "not again"
            

overall_game()


