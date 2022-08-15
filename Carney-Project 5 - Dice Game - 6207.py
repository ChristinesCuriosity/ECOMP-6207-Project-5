#This is a Dice Game!
import time
#Step 1 - # of dice and game start
number_dice = input('Enter the number of dice:')
number_dice = int(number_dice)
ready = input('Ready to start? \n Press \'any\' key to continue')

#Step 2 - Functions to roll dice
import random
def roll_dice(n):
    dice = [] #empty list of dice
    #add random numbers 1-6 to list
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print('Computer total', computer_total)
    print('User total', user_total)
    if user_total > computer_total:
        print('User wins!')
    elif user_total < computer_total:
        print('Computer wins!')
    else:
        print('It\'s a tie!')
def roll_again(choices, dice_list):
    print('Rolling again...\n')
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1,6)
def computer_strategy(n):
    #create computer choices:roll if <5
    print('Computer is thinking...\n')
    time.sleep(3)
    choices = '' #Starts with an empty list of choices
    for i in range(n):
        if computer_rolls[i] <5:
            choices = choices +'r'
        else:
            choices = choices +'-'
    return choices
            
#User turn to roll
user_rolls = roll_dice(number_dice)
print('User first roll: ', user_rolls,'\n')

#Step 4 - User choices
user_choices = input('Enter - to hold or r to roll again :')
#check length of user input
while len(user_choices) != number_dice:
    print('You must enter ',number_dice, ' choices.')
    user_choices = input('Enter - to hold or r to roll again. ex. ---r-r')

#Step 5 - Roll Again based off of User choices
roll_again(user_choices, user_rolls)
print('Player new Roll: ', user_rolls,'\n')
    

#computer turn to roll
print('Computer\'s turn ')
computer_rolls = roll_dice(number_dice)
print('Computer\'s first roll: ', computer_rolls,'\n')

#Step 6 - Computer strategy
computer_choices = computer_strategy(number_dice)
print('Computer Choice: ', computer_choices)
roll_again(computer_choices, computer_rolls)
print('Computer\'s new Roll: ', computer_rolls,'\n')

#Step 3 - Decide on Winner
find_winner(computer_rolls,user_rolls)




    
