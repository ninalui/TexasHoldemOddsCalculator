from Poker import Poker
from probabilities import *

def main():
    try: 
        game = Poker()
        game.set_num_in_community()
        hands, community = game.input_cards()

        player_1 = hands[0]
        player_2 = hands[1]

        if game.num_in_community == 4:
            player_1, tie, player_2 = prob_river_unknown(player_1, player_2, community, game)
        elif game.num_in_community == 3: 
            player_1, tie, player_2 = prob_turn_and_river_unknown(player_1, player_2, community, game)

        display_probs(player_1, tie, player_2)

    except ValueError as ex:
        print(ex)

main()
