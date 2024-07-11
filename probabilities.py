from hand_functions import * 
from itertools import combinations

def prob_river_unknown(player_1, player_2, community, game):
    '''
    function -- prob river unknown
        determine the probability of win/tie for 2 players during a game where the river (5th card) has not been revealed
    parameters: player_1 -- list of player 1's cards
                player_2 -- list of player 2's cards
                community -- list of cards on the table
                game -- Poker game object
    returns the probability player 1 wins, the probability the players tie, and the probability player 2 wins
    raises ValueError if at any point, a winner cannot be found for a certain river 
    '''
    num_remaining = game.count_remaining()

    player_1_wins = 0
    player_2_wins = 0 
    player_ties = 0 

    for river in game.deck:
        community.append(river)

        player_1_hands = get_hand_combinations(player_1, community)
        best_rank_player_1 = -1

        for hand in player_1_hands:
            rank_1 = get_best_hand_rank(hand)

            if rank_1 > best_rank_player_1:
                best_rank_player_1 = rank_1
                best_hand_1 = hand

            elif rank_1 == best_rank_player_1:
                best_high_card = get_high_card(best_hand_1, best_rank_player_1)
                high_card_1 = get_high_card(hand, rank_1)

                if high_card_1 > best_high_card:
                    best_hand_1 = hand
        
        player_2_hands = get_hand_combinations(player_2, community)
        best_rank_player_2 = -1

        for hand in player_2_hands:
            rank_2 = get_best_hand_rank(hand)

            if rank_2 > best_rank_player_2:
                best_rank_player_2 = rank_2
                best_hand_2 = hand
                
            elif rank_2 == best_rank_player_2:
                best_hand_high_card = get_high_card(best_hand_2, best_rank_player_2)
                high_card_2 = get_high_card(hand, rank_2)

                if high_card_2 > best_hand_high_card:
                    best_hand_2 = hand

        community.remove(river)

        if best_rank_player_1 > best_rank_player_2:
            player_1_wins += 1

        elif best_rank_player_2 > best_rank_player_1:
            player_2_wins += 1
        
        elif best_rank_player_1 == best_rank_player_2:
            winner = break_tie(best_hand_1, best_hand_2, best_rank_player_1)
            if winner == 1: 
                player_1_wins += 1
            elif winner == 2: 
                player_2_wins += 1
            elif winner == 0:
                player_ties += 1
            else:
                raise ValueError(f'No winner was found for this tie: {best_hand_1} vs {best_hand_2}')
        
        else:
            raise ValueError(f'No winner was found for this river, {river}')

    player_1_prob = player_1_wins / num_remaining
    player_tie_prob = player_ties / num_remaining
    player_2_prob = player_2_wins / num_remaining

    return player_1_prob, player_tie_prob, player_2_prob

def prob_turn_and_river_unknown(player_1, player_2, community, game):
    '''
    function -- prob turn and river unknown
        determine the probability of win/tie for 2 players during a game where the turn (4th card) and the river (5th card) have not yet been revealed
    parameters: player_1 -- list of player 1's cards
                player_2 -- list of player 2's cards
                community -- list of cards on the table
                game -- Poker game object
    returns the probability player 1 wins, the probability the players tie, and the probability player 2 wins
    raises ValueError if at any point, a winner cannot be found for a certain turn-river pair
    '''
    turn_river_pairs = list(combinations(game.deck, 2))
    total = len(turn_river_pairs)

    player_1_wins = 0
    player_2_wins = 0
    player_ties = 0 

    for pair in turn_river_pairs:
        community.extend(pair)

        player_1_hands = get_hand_combinations(player_1, community)
        best_rank_player_1 = -1

        for hand in player_1_hands:
            rank_1 = get_best_hand_rank(hand)

            if rank_1 > best_rank_player_1:
                best_rank_player_1 = rank_1
                best_hand_1 = hand

            elif rank_1 == best_rank_player_1:
                best_high_card = get_high_card(best_hand_1, best_rank_player_1)
                high_card_1 = get_high_card(hand, rank_1)

                if high_card_1 > best_high_card:
                    best_hand_1 = hand
        
        player_2_hands = get_hand_combinations(player_2, community)
        best_rank_player_2 = -1

        for hand in player_2_hands:
            rank_2 = get_best_hand_rank(hand)
            
            if rank_2 > best_rank_player_2:
                best_rank_player_2 = rank_2
                best_hand_2 = hand
                
            elif rank_2 == best_rank_player_2:
                best_hand_high_card = get_high_card(best_hand_2, best_rank_player_2)
                high_card_2 = get_high_card(hand, rank_2)

                if high_card_2 > best_hand_high_card:
                    best_hand_2 = hand

        turn = pair[0]
        river = pair[1]
        community.remove(turn)
        community.remove(river)

        if best_rank_player_1 > best_rank_player_2:
            player_1_wins += 1

        elif best_rank_player_2 > best_rank_player_1:
            player_2_wins += 1
        
        elif best_rank_player_1 == best_rank_player_2:
            winner = break_tie(best_hand_1, best_hand_2, best_rank_player_1)
            if winner == 1: 
                player_1_wins += 1
            elif winner == 2: 
                player_2_wins += 1
            elif winner == 0:
                player_ties += 1
            else:
                raise ValueError(f'No winner was found for this tie: {best_hand_1} vs {best_hand_2}')

        else:
            raise ValueError(f'No winner was found for this turn-river pair, {turn}{river}')

    player_1_prob = player_1_wins / total
    player_tie_prob = player_ties / total
    player_2_prob = player_2_wins / total

    return player_1_prob, player_tie_prob, player_2_prob
    
def display_probs(player_1, tie, player_2):
    '''
    function -- display probs
        displays the probabilities of player 1 winning, the players ending in a tie, and player 2 winning in percent format
    paramaters: player_1 -- probability of player 1 winning
                tie -- probability of a tie
                player_2 -- probability of player 2 winning
    returns nothing 
    '''
    print(f'\nProbability of Player 1 winning: {player_1:.2%}')
    print(f'Probability of Tie: {tie:.2%}')
    print(f'Probability of Player 2 winning: {player_2:.2%}')