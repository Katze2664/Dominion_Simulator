
# Buys cards in order of priority: Province > Gold > Duchy > Silver > None,
# subject to availability and sufficient coins.
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
