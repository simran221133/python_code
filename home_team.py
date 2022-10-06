teams = ["lakers", "golden-state", "boston", "lebron", "raptors"]

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print("[" + str(home_team) + " vs " + str(away_team) + "]" , end=" ")
print()