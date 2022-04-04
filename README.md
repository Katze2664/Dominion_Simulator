# Dominion Simulator

Simulates a simplified version of Dominion.

## Description

Dominion is a deck-building card game. Each player begins with a small deck of cards, 
which they improve by purchasing cards from a common supply that varies from game to 
game. Cards can help the player's deck function, impede their opponents, or provide 
victory points. Timing is an important component to a successful strategy in Dominion.
Buying victory cards gives you victory points which are necessary to win the game,
however buying victory cards too early in the game before you have built up enough
power will lead to your hand becoming clogged with victory cards, and your opponent
is likely to overtake you and win.

In this project I have created a simulation of a simplified version of Dominion in
which the only cards available for purchase are: Copper, Silver, Gold, Estates,
Duchies, and Provinces. The simulation allows for different strategies to tested
over a large number of games to see how often they win in expectation. This could
be used to explore questions of timing, such as when is the right time to start
buying Duchies.

Currently only a single strategy has been implemented, which is used by both players.
By running the simulation over many games this allows the first-player advantage to 
be quantified.

## Executing program

Run main.py

## Authors

Ethan Watkins

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details

## Acknowledgements

Dominion, created by Donald X. Vaccarino and published by Rio Grande Games.