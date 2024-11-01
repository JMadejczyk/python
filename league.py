n, m, t = 3, 2, 2
teams = ["Kubek", "Szklanka", "Kufel"]
matches = ['Kubek:Kufel:3:2', 'Kubek:Szklanka:1:4']

data = {}
for team in teams:
    data[team] = {"matches_number": 0, "won": 0, "lost": 0} 

for match in matches:
    team1, team2, goals1, goals2 = match.split(":")
    goals1, goals2 = int(goals1), int(goals2)
    data[team1]["matches_number"] += 1
    data[team2]["matches_number"] += 1
    if goals1 > goals2:
        data[team1]["won"] += 1
        data[team2]["lost"] += 1
    elif goals1 < goals2:
        data[team1]["lost"] += 1
        data[team2]["won"] += 1
teams.sort()
for team in teams:
    if n - 1 - data[team]["matches_number"] + data[team]["won"] >= t:
        print(team)
