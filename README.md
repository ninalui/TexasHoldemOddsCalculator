# Texas Hold'em Odds Calculator

## Overview

This program calculates the odds of winning a game of Texas Hold'em for two players using a standard 52-card deck. It evaluates the probabilities during the flop (3 community cards face-up) or turn (4 community cards face-up) phases of the game. The user inputs the hands of the two players and the community cards, and the program calculates the probabilities of each player winning or the game ending in a tie. 

## How to Use
1. Clone the repository:
```sh
git clone https://github.com/ninalui/TexasHoldemOddsCalculator.git
```
2. Make sure you are in the right directory then run:
```sh
python driver.py
```
3. You will be prompted to enter the card values and suits for each player's hand and the community cards. The program will then display the probabilities of each player winning and the probability of a tie. 

### Card Values
- Input 2 to 14
- Numeric values: 2 - 10
- Face cards: 10 - J (Jack), 11 - Q (Queen), 12 -  K (King), 13 - A (Ace)

### Suits

- C: Clubs
- S: Spades
- H: Hearts
- D: Diamonds

## Disclaimer
Please ensure to input valid card values and suits as specified above. Due to time constraints, handling incorrect input was not implemented. Please provide valid inputs to avoid any issues. 

## Files
- Card.py: Defines the Card class representing a playing card.
- Poker.py: Defines the Poker class representing the game logic.
- hand_functions.py: Contains functions to evaluate poker hands.
- probabilities.py: Contains functions to calculate the probabilities of winning.
- driver.py: The main driver script to run the program.
