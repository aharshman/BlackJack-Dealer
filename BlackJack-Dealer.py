# -*- coding: utf-8 -*-
"""
Alexander Harshman
9/12/21
"""

from Cards import Card
from random import randint
from graphics import time

def main():
    
# Setting Values
    handvalue = 0
    aces = 0
    cardcount = 0
    
# Deck of cards listed out inefficiently
    deck =  [Card(1, 's'), Card(1, 'd'), Card(1, 'h'), Card(1, 'c'),
             Card(2, 's'), Card(2, 'd'), Card(2, 'h'), Card(2, 'c'), 
             Card(3, 's'), Card(3, 'd'), Card(3, 'h'), Card(3, 'c'), 
             Card(4, 's'), Card(4, 'd'), Card(4, 'h'), Card(4, 'c'), 
             Card(5, 's'), Card(5, 'd'), Card(5, 'h'), Card(5, 'c'),
             Card(6, 's'), Card(6, 'd'), Card(6, 'h'), Card(6, 'c'),
             Card(7, 's'), Card(7, 'd'), Card(7, 'h'), Card(7, 'c'),
             Card(8, 's'), Card(8, 'd'), Card(8, 'h'), Card(8, 'c'),
             Card(9, 's'), Card(9, 'd'), Card(9, 'h'), Card(9, 'c'),
             Card(10, 's'), Card(10, 'd'), Card(10, 'h'), Card(10, 'c'),
             Card(11, 's'), Card(11, 'd'), Card(11, 'h'), Card(11, 'c'),
             Card(12, 's'), Card(12, 'd'), Card(12, 'h'), Card(12, 'c'),
             Card(13, 's'), Card(13, 'd'), Card(13, 'h'), Card(13, 'c')]
    
    # This also does the same thing as the list just more efficiently
    """suits = ['s', 'd', 'h', 'c']

    deck = []

    for i in range (1, 14):
        for suit in suits:
            card = (Card(i, suit))
            deck.append(card)"""
                 
    
# loop that draws cards while the deal is under 17
    while handvalue <= 16:
    
    # This picks a random index number in the list
        cardnum = randint(0, len(deck))
    
    # This line picks a card and removes it from the deck
        card = deck.pop(cardnum)
    
        print(card)
    
        # Gets the value of a picked card
        value = card.value()
        
        # Totals the value of the dealers hand
        handvalue = handvalue + value
        
        # Tests to see if the card is an ace
        if card.getRank() == 1:
            aces += 1
        
        # If the dealer busts and they have an ace, it makes the ace valued at one
        if handvalue > 21 and aces > 0:
            handvalue = handvalue - 10
            aces = aces - 1
            
        # Waits a second before the next card is drawn for suspense.
        time.sleep(1)
            
        # Tracks how many cards are dealt        
        cardcount += 1
    
# Sees if the dealer got blackjack
    if handvalue == 21 and cardcount == 2:
        print('BlackJack!!')
    
# Sees if the dealer did not bust
    elif handvalue < 22:
        print('The Dealer has', handvalue)

    else:
        print('The Dealer busts with', handvalue)
    
    
main()

