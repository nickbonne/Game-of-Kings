#! python3

import random
from random import shuffle
import sys

deck = [

    'Ace of Hearts', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 'Five of Hearts',
    'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts',
    'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',

    'Ace of Diamonds', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds', 'Five of Diamonds',
    'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds', 'Ten of Diamonds',
    'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds',

    'Ace of Clubs', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs',
    'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs',
    'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',

    'Ace of Spades', 'Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades',
    'Six of Spades', 'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades',
    'Jack of Spades', 'Queen of Spades', 'King of Spades'

]  ### Deck from which cards are pulled
deck_restore = [

    'Ace of Hearts', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 'Five of Hearts',
    'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts',
    'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',

    'Ace of Diamonds', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds', 'Five of Diamonds',
    'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds', 'Ten of Diamonds',
    'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds',

    'Ace of Clubs', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs',
    'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs',
    'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',

    'Ace of Spades', 'Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades',
    'Six of Spades', 'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades',
    'Jack of Spades', 'Queen of Spades', 'King of Spades'

]  ### Original deck made equal to this to reset game
rules = ['Waterfall',
         'You assign two drinks',
         'You take three drinks',
         'Whores. girls drink',
         'Thumbmaster: Sneak you thumb onto the table. The lsat to follow drinks.',
         'Dicks. Guys drink',
         'Heaven! Last to reach up drinks',
         'Pick a mate, they now drink when you drink',
         'Rhymes: Say a word, and go around the table naming words that rhyme. Drink if you can\'t think',
         'Categories: Pick a catergory and go around the table naming things that belong. Drink if you can\'t think',
         'Make a new rule for the duration of the game. Players drink if they break it.',
         'Question Master: Everyone must reply to you with a question. They drink if they don\'t',
         'Pour some of your drink into a cup. Player who draws last king drinks the contents.'
         ]


def game_reset():
    global deck
    deck = deck_restore


def main_menu():  ###
    main_menu = 1
    while main_menu == 1:
        print('1. Play Game')
        print('2. Quit')
        menu_input = input('What would you like to do? ')
        if menu_input == '1':
            play()
            print('Game Over.', '\n')

        if menu_input == '2':
            sys.exit(0)
        else:
            print()
            print('Try again.', '\n')


def play():
    while len(deck) >= 1:
        print('Press \'enter\' to draw a card')
        enter_input = input()
        if enter_input == '':
            pop_deck()
            print()
    if len(deck) == 0:
        game_reset()



def pop_deck():
    rule_printer = deck.pop(random.randrange(len(deck)))
    print(rule_printer)
    if "Ace" in rule_printer:
        print('Rule: ' + rules[0])
    elif "Two" in rule_printer:
        print('Rule: ' + rules[1])
    elif "Three" in rule_printer:
        print('Rule: ' + rules[2])
    elif "Four" in rule_printer:
        print('Rule: ' + rules[3])
    elif "Five" in rule_printer:
        print('Rule: ' + rules[4])
    elif "Six" in rule_printer:
        print('Rule: ' + rules[5])
    elif "Seven" in rule_printer:
        print('Rule: ' + rules[6])
    elif "Eight" in rule_printer:
        print('Rule: ' + rules[7])
    elif "Nine" in rule_printer:
        print('Rule: ' + rules[8])
    elif "Ten" in rule_printer:
        print('Rule: ' + rules[9])
    elif "Jack" in rule_printer:
        print('Rule: ' + rules[10])
    if "Queen" in rule_printer:
        print('Rule: ' + rules[11])
    if "King" in rule_printer:
        print('Rule: ' + rules[12])
    print()


print('Welcome to a Game of Kings' '\n')
print('Rules are printed after each card is pulled.', '\n' '\n')

while True:
    main_menu()
    play()



