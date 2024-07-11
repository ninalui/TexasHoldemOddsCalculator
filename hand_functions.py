from itertools import combinations

# POKER HAND RANKS (high to low)
ROYAL_FLUSH = 9
STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0
POKER_HAND_TOTAL = 5

def has_pair(hand_count):
    '''
    function -- has pair
        determines if a hand has any pairs
    parameters: hand_count -- dict of counts of each value in the hand
    returns how many distinct pairs are in the hand
    '''
    pair_count = sum(1 for val in hand_count.values() if val == 2)
    return pair_count

def three_of_a_kind(hand_count):
    '''
    function -- three of a kind
        determines if a hand has a three of a kind
    parameters: hand_count -- dict of counts of each value in the hand
    returns True if there is a three of a kind in the hand, False otherwise
    '''
    return 3 in hand_count.values()

def four_of_a_kind(hand_count):
    '''
    function -- four of a kind
        determines if a hand has a four of a kind
    parameters: hand_count -- dict of counts of each value in the hand
    returns True if there is a four of a kind in the hand, False otherwise
    '''
    return 4 in hand_count.values()

def flush(hand_suits):
    '''
    function -- flush
        determines if a hand has a flush (all cards are the same suit)
    parameters: hand_suits -- set of all the suits in the hand 
    returns True if there is only one suit in the hand (all cards are the same), False otherwise
    '''
    if len(hand_suits) == 1:
        return True
    else: 
        return False
    
def straight(hand_values):
    '''
    function -- straight
        determines if a hand has a straight -- considers both high ace and low ace
        for a hand to have a straight, the difference between the lowest value card and the highest value card would be 4
        and there would be no duplicates in the hand 
    parameters: hand_values -- list of all the values in the hand
    returns True if there is a straight, False otherwise
    '''
    low_ace_straight = [2, 3, 4, 5, 14]
    value_range = max(hand_values) - min(hand_values) 

    if hand_values == low_ace_straight:
        return True
    elif len(set(hand_values)) == len(hand_values):
        if value_range == 4:
            return True
    else:
        return False
    
def royal_values(hand_value):
    '''
    function -- royal values
        determines if a hand contains only royal values (10, J, Q, K, A)
    parameters: hand_values -- list of all the values in the hand
    returns True if there are only royal values in the hand, False otherwise
    '''
    values = {10, 11, 12, 13, 14}
    if values.issubset(hand_value):
        return True
    else:
        return False
    
def get_best_hand_rank(hand):
    '''
    function -- get best hand
        determines what the highest ranking poker hand is in the current hand 
    parameters: hand -- list of all the cards in the current hand
    returns the rank (int) of the highest ranking poker hand in the hand (the higher the number, the higher the rank)
    '''
    hand_values = sorted([card.value for card in hand])
    hand_count = {value : hand_values.count(value) for value in set(hand_values)}
    hand_suits = set([card.suit for card in hand])

    if flush(hand_suits):
        if royal_values(hand_values):
            return ROYAL_FLUSH
        
        elif straight(hand_values):
            return STRAIGHT_FLUSH
        
        else:
            return FLUSH
    
    elif four_of_a_kind(hand_count):
        return FOUR_OF_A_KIND
    
    elif straight(hand_values):
        return STRAIGHT
    
    else:
        pair_count = has_pair(hand_count)
        
        if three_of_a_kind(hand_count):
            
            if pair_count == 1:
                return FULL_HOUSE
            
            else:
                return THREE_OF_A_KIND
        
        elif pair_count == 2:
            return TWO_PAIR
        
        elif pair_count == 1:
            return ONE_PAIR
    
    return HIGH_CARD

def get_high_card(hand, rank):
    '''
    function -- get high card
        determines what the highest card in the hand is outside of those in combinations
            - to break a tie between hands that are of the same ranking
    parameters: hand -- list of cards in the current hand
                rank -- int poker ranking of the hand
    returns the highest card in the hand outside of those in combinations 
    '''
    hand_values = sorted([card.value for card in hand])
    hand_count = {value : hand_values.count(value) for value in set(hand_values)}

    if rank == FOUR_OF_A_KIND:
        four_value = [value for value, count in hand_count.items() if count == 4][0]
        hand_values.remove(four_value)

    elif rank == THREE_OF_A_KIND:
        three_value = [value for value, count in hand_count.items() if count == 3][0]
        hand_values.remove(three_value)

    elif rank == TWO_PAIR or rank == ONE_PAIR:
        pair_values = [value for value, count in hand_count.items() if count == 3]
        hand_values = set(hand_values).difference(set(pair_values))

    highest_card = max(hand_values)

    return highest_card

def get_hand_combinations(hole_cards, community_cards):
    ''' 
    function -- get hand combinations
        provides all possible combinations of 5 card hands from a list of cards
    parameters: hole_cards -- list of all the cards in the player's hand
                community_cards -- list of all the cards on the table
    returns a list of all possible 5 card hands out of the cards provided
    '''
    all_cards = hole_cards + community_cards
    combos = list(combinations(all_cards, POKER_HAND_TOTAL))
    return combos

def break_tie(player_1_hand, player_2_hand, rank):
    '''
    function -- break tie
        called when the rank of two players are the same, to determine who would win the tie-break
        when two players have the same rank, the one with the higher value card wins 
    parameters: player_1_hand -- list of player 1's best 5 card hand
                player_2_hand -- list of player 2's best 5 card hand 
                rank -- the rank (int) the 2 players share
    returns the winner of the tie break (1 if player 1, 2 if player 2, 0 if still tie)
    '''
    hand_values_1 = sorted([card.value for card in player_1_hand])
    hand_values_2 = sorted([card.value for card in player_2_hand])
    winner = -1

    if hand_values_1 == hand_values_2: 
        winner = 0
    
    if (rank == STRAIGHT 
        or rank == STRAIGHT_FLUSH 
        or rank == FLUSH
        or rank == HIGH_CARD):

        highest_1 = max(hand_values_1)
        highest_2 = max(hand_values_2)
        
    else: 
        # for four-, three-, pairs, the highest value inside the multiple wins   
        count_dict_1 = {value : hand_values_1.count(value) for value in set(hand_values_1)}
        count_dict_2 = {value : hand_values_2.count(value) for value in set(hand_values_2)}
                                                                        
        if rank == FOUR_OF_A_KIND: 
            highest_1 = [card_value for card_value, count in count_dict_1.items() if count == 4][0]
            highest_2 = [card_value for card_value, count in count_dict_2.items() if count == 4][0]

        elif rank == THREE_OF_A_KIND or rank == FULL_HOUSE:
            highest_1 = [card_value for card_value, count in count_dict_1.items() if count == 3][0]
            highest_2 = [card_value for card_value, count in count_dict_2.items() if count == 3][0]
            
            if rank == FULL_HOUSE: 
                if highest_1 == highest_2:
                    rank = ONE_PAIR
        
        elif rank == TWO_PAIR: 
            pair_values_1 = [card_value for card_value, count in count_dict_1.items() if count == 2]
            highest_1 = max(pair_values_1)
            
            pair_values_2 = [card_value for card_value, count in count_dict_2.items() if count == 2]
            highest_2 = max(pair_values_2)
            
            if highest_1 == highest_2: # get the other (smaller) value if high pairs are same value 
                highest_1 = min(pair_values_1)
                highest_2 = min(pair_values_2)            

        elif rank == ONE_PAIR:
            highest_1 = [card_value for card_value, count in count_dict_1.items() if count == 2][0]
            highest_2 = [card_value for card_value, count in count_dict_2.items() if count == 2][0]
        
    # if no winner found/highest values were the same for both hands
    while winner == -1:
        if highest_1 > highest_2: 
            winner = 1
        
        elif highest_2 > highest_1:
            winner = 2
        
        elif highest_1 == highest_2: # move on to the next highest value if tie
            winner = -1
            hand_values_1.remove(highest_1)
            highest_1 = max(hand_values_1)
            hand_values_2.remove(highest_2)
            highest_2 = max(hand_values_2)

    return winner