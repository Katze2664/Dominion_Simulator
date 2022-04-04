from random import shuffle
from random import seed

seed()

class Game:
    def __init__(self, players):
        self.players = players
        self.turn_counter = 0
        self.province = 8
        self.duchy = 8
        self.estate = 8

    def game_state(self):
        return self.province, self.duchy, self.estate

    def check_valid(self, action, player):
        coins = sum(player.hand)
        if action == "province" and (self.province == 0 or coins < 8):
            return False
        elif action == "duchy" and (self.duchy == 0 or coins < 5):
            return False
        elif action == "estate" and (self.estate == 0 or coins < 2):
            return False
        elif action == "gold" and coins < 6:
            return False
        elif action == "silver" and coins < 3:
            return False
        else:
            valid_actions = ["none", "copper", "silver", "gold", "estate", "duchy", "province"]
            return action in valid_actions

    def buy(self, action, player):
        if action == "province":
            self.province -= 1
        elif action == "duchy":
            self.duchy -= 1
        elif action == "estate":
            self.estate -= 1
        player.buy(action)

    def winner(self):
        best_score = max([player.vp for player in self.players])
        best_players = [player for player in self.players if player.vp == best_score]
        fewest_turns = min([player.turns for player in best_players])
        winners = [player for player in best_players if player.turns == fewest_turns]
        winner_names = []
        print("Winners:")
        for player in winners:
            winner_names.append(player.name)
            print(player.name)
        return winner_names

    def scores(self):
        result = {}
        for player in self.players:
            result[player.name] = dict(vp=player.vp,
                                       turns=player.turns,
                                       province=player.province,
                                       duchy=player.duchy,
                                       estate=player.estate,
                                       gold=player.gold,
                                       silver=player.silver,
                                       copper=player.copper,
                                       )
            print(f"{player.name} VP: {player.vp}, Turns: {player.turns}, "
                  f"P: {player.province}, D: {player.duchy}, E: {player.estate}, "
                  f"G: {player.gold}, S: {player.silver}, C: {player.copper}")
        return result

    def play(self):
        while self.province != 0:
            self.turn_counter += 1
            # print("Turn", self.turn_counter)
            if self.turn_counter == 100:
                raise Exception("Turn count exceeded")

            for player in self.players:
                player.draw_hand()
                valid_action = False
                attempts = 0
                while not valid_action:
                    attempts += 1
                    action = player.action(self.game_state())
                    valid_action = self.check_valid(action, player)
                    if attempts == 10:
                        raise Exception("Failed to supply valid action")
                self.buy(action, player)
                player.discard_hand()
            # input()
        winner_names = self.winner()
        scores = self.scores()
        return winner_names, scores


class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.turns = 0
        self.vp = 3
        self.total_cards = 10
        self.victory_cards = 10
        self.copper = 7
        self.silver = 0
        self.gold = 0
        self.estate = 3
        self.duchy = 0
        self.province = 0

        self.deck = [0]*3 + [1]*7
        shuffle(self.deck)
        self.hand = []
        self.discard_pile = []

    def action(self, game_state):
        game_province, game_duchy, game_estate = game_state
        player_state = dict(hand=self.hand,
                            game_province=game_province,
                            game_duchy=game_duchy,
                            game_estate=game_estate)
        return self.strategy(player_state)

    def draw_hand(self):
        self.turns += 1
        for i in range(5):
            if len(self.deck) == 0:
                self.reshuffle()
            self.hand.append(self.deck.pop())

    def discard_hand(self):
        while len(self.hand) != 0:
            self.discard_pile.append(self.hand.pop())

    def reshuffle(self):
        assert len(self.deck) == 0
        self.deck = self.discard_pile.copy()
        shuffle(self.deck)
        self.discard_pile = []

    def buy(self, action):
        # print(self.name, action, sum(self.hand), self.hand)
        if action == "province":
            self.discard_pile.append(0)
            self.vp += 6
            self.total_cards += 1
            self.victory_cards += 1
            self.province += 1
        elif action == "duchy":
            self.discard_pile.append(0)
            self.vp += 3
            self.total_cards += 1
            self.victory_cards += 1
            self.duchy += 1
        elif action == "estate":
            self.discard_pile.append(0)
            self.vp += 1
            self.total_cards += 1
            self.victory_cards += 1
            self.estate += 1
        elif action == "gold":
            self.discard_pile.append(3)
            self.total_cards += 1
            self.gold += 1
        elif action == "silver":
            self.discard_pile.append(2)
            self.total_cards += 1
            self.silver += 1
        elif action == "copper":
            self.discard_pile.append(1)
            self.total_cards += 1
            self.copper += 1
        elif action == "none":
            pass
        else:
            raise Exception("No action implemented")

def strat1(player_state):
    # print(player_state)
    coins = sum(player_state["hand"])
    if coins >= 8:
        if player_state["game_province"] > 0:
            return "province"

        else:
            return "gold"
    elif coins >= 6:
        return "gold"
    elif coins >= 5:
        if player_state["game_duchy"] > 0:
            return "duchy"
        else:
            return "silver"
    elif coins >= 3:
        return "silver"
    else:
        return "none"

results = {}
repeats = 10
for i in range(repeats):
    p1 = Player("p1", strat1)
    p2 = Player("p2", strat1)
    players = [p1, p2]
    game = Game(players)
    winners, scores = game.play()

    winners = tuple(winners)
    print("w", winners)
    if winners in results.keys():
        results[winners] += 1
    else:
        results[winners] = 1

print(results)