from game_mechanics import Game, Player
from strategies import strat1
import random

# In this simple example, both Alice and Bob play the same strategy.
# However, since Alice gets the first turn of the game, she has the advantage.

# Set random seed if desired
seed = None

# Set the number of games to simulate
repeats = 1000

# No need to modify below here
random.seed(seed)
results = {}
for i in range(repeats):
    alice = Player("Alice", strat1)
    bob = Player("Bob", strat1)
    players = [alice, bob]
    game = Game(players)
    winners, scores = game.play()

    if len(winners) == 1:
        winner = winners[0]
    else:
        winner = "Draw"

    results.setdefault(winner, 0)
    results[winner] += 1

print("Win Percentage")
for name, wins in sorted(results.items()):
    print(f"{name} = {100 * wins / repeats}%")
