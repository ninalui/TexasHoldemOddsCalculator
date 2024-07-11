class Card:
    '''
    Class Card
        Represents standard playing card with its value and suit
        
    Attributes: 
        value -- value of card
        suit -- suit of card
    
    Methods:
        __init__ -- constructor
        __eq__ -- determines if 2 cards are of equal value and suit
        __str__ -- provides user-friendly string representation of card
        __repr__ -- provides developer-friendly string representation of card
    '''
    VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    SUITS = ['D', 'C', 'H', 'S']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __str__(self):
        if self.value == 14:
            value = 'A'
        elif self.value == 13:
            value = 'K'
        elif self.value == 12:
            value = 'Q'
        elif self.value == 11:
            value = 'J'
        else: 
            value = str(self.value)
        return value + self.suit
    
    def __repr__(self):
        return str(self.value) + self.suit
