n = int(input())

matches = [input() for _ in range(n)]

players = {}

for match in matches:
    p1_data, p2_data = match.split()
    p1_id, p1_score = p1_data.split(":")
    p2_id, p2_score = p2_data.split(":")

    if p1_id not in players:
        players[p1_id] = {"matches_won": 0, "points_sum": 0}
    if p2_id not in players:
        players[p2_id] = {"matches_won": 0, "points_sum": 0}

    if int(p1_score) > int(p2_score):
        players[p1_id]["matches_won"] += 1
    elif int(p1_score) < int(p2_score):
        players[p2_id]["matches_won"] += 1
        
    players[p1_id]["points_sum"] += int(p1_score)
    players[p2_id]["points_sum"] += int(p2_score)


players_tab = []
for player in players:
    players_tab.append({"p_id": player, "points_sum": players[player]["points_sum"], "matches_won": players[player]["matches_won"]})


def find_player_with_highest_wins_number(players_tab):
    highest_wins_number = 0
    best_players = []
    for player in players_tab:
        if player["matches_won"] > highest_wins_number:
            highest_wins_number = player["matches_won"]
            best_players = [player]

        if player["matches_won"] == highest_wins_number:
            best_players.append(player)
    if len(best_players) == 1:
        return best_players[0]
    else:
        return find_player_with_highest_score(best_players)

def find_player_with_highest_score(players_tab):
    highest_score = 0
    best_players = []
    for player in players_tab:
        if player["points_sum"] > highest_score:
            highest_score = player["points_sum"]
            best_players = [player]
        if player["points_sum"] == highest_score:
            best_players.append(player)
    if len(best_players) == 1:
        return best_players[0]
    else:
        return find_player_with_highest_ascii(best_players)
    
def find_player_with_highest_ascii(players_tab):
    lowest_ascii = 1000
    best_player = ""
    for player in players:
        if ord(player["p_id"]) < lowest_ascii:
            lowest_ascii = ord(player["p_id"])
            best_player = player["p_id"]
    return best_player