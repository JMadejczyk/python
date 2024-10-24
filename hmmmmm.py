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

# print(players_tab)

# sorted(players_tab, key=)