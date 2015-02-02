#!/usr/bin/env python
from itertools import combinations


def team_score(team):
    binary_score = str(bin(int(team[0], 2) | int(team[1], 2))).count("1")
    return binary_score


def predict_teams(teams):
    team_combinations = list(combinations(teams, 2))
    scores = []
    for team in team_combinations:
        scores.append(team_score(team))
    return max(scores), scores.count(max(scores))


# t, str
n, m = raw_input().split(" ")
teams = []
for line in range(0, int(n)):
    team = raw_input()
    teams.append(team)

result = predict_teams(teams)
print result[0]
print result[1]
