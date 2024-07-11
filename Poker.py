from Card import Card

NUM_CARDS_PER_HAND= 2
NUM_PLAYERS = 2

class Poker:
    '''
    Class Poker
        Represents a game of Poker/TexasHoldEm.
    
    Attributes:
        deck -- list of cards in deck
        hand_limit -- number of cards allowed in hand (default is 2)
        num_in_community -- number of cards already revealed in community / table (default is 0)
        num_players -- number of players in game (default is 2)
    
    Methods: 
        __init__ -- constructor
            creates deck object and fills deck with 52 Card objects
        remove_card -- removes specified card from the deck
            raises ValueError if card to remove is not in the deck
        set_num_in_community -- sets the number of cards already in the community/table
        get_num_in_community -- gets input for the number of cards already in the community/table
            raises ValueError for invalid input (only 3 and 4 allowed for downstream probability calculations)
        input_cards -- provides player cards/table cards based on input and removes correspoding cards from deck
            raises ValueErrors whenever input results in a card not in the deck
        count_remaining -- determines how many cards are left in the deck
        display_deck -- displays cards in deck 
    '''

    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                card = Card(value, suit)
                self.deck.append(card)

        self.hand_limit = NUM_CARDS_PER_HAND
        self.num_in_community = 0 
        self.num_players = NUM_PLAYERS
    
    def remove_card(self, card):
        if card in self.deck:
            self.deck.remove(card)
        else:
            raise ValueError('Card to remove not found in deck')

    def set_num_in_community(self):
        num_in_community = self.get_num_in_community()
        self.num_in_community = num_in_community

    def get_num_in_community(self):
        num_in_community = input('Enter number of cards in community: ')
        if num_in_community.isdigit():
            num_in_community = int(num_in_community)
        if num_in_community == 3 or num_in_community == 4:
            return num_in_community
        else: 
            raise ValueError('Invalid number of cards in community - please only enter 3 or 4')
    
    def input_cards(self):
        hands = [[] for _ in range(self.num_players)]
        for i in range(len(hands)):
            print('')
            for j in range(self.hand_limit):
                card_value = input(f'Enter player {i+1} card {j+1} value (2 to 14): ')
                if card_value.isdigit():
                    card_value = int(card_value)
                if card_value < 2 or card_value > 14:
                    card_value = input(f'Please enter valid value (2 to 14): ')
                card_suit = input(f'Enter player {i+1} card {j+1} suit: ')
                card = Card(int(card_value), card_suit)
                if card in self.deck:
                    hands[i].append(card)
                    self.remove_card(card)
                else:
                    raise ValueError('Card specified not in deck')
        
        community = []
        for i in range(self.num_in_community):
            print('')
            card_value = input(f'Enter card {i+1} value on the table: ')
            card_suit = input(f'Enter card {i+1} suit on the table: ')
            card = Card(int(card_value), card_suit)
            if card in self.deck:
                community.append(card)
                self.remove_card(card)
            else:
                raise ValueError('Card specified not in deck')

        return hands, community
    
    def count_remaining(self):
        return len(self.deck)
    
    def display_deck(self):
        for card in self.deck:
            print(card)




    