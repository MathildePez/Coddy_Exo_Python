# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
commun_players = sorted(list(match1 & match2 & match3))

print(f"Players in all matches: {commun_players}")

# 2. Find players who participated in exactly two matches
listmatch1 = sorted(list(match1))
listmatch2 = sorted(list(match2))
listmatch3 = sorted(list(match3))

liste_total = listmatch1 + listmatch2 + listmatch3

only_1_list = []
only_2_list = []

for player in liste_total:
    if liste_total.count(player) == 2:
        only_2_list.append(player)

only_2_list_1 = sorted(list(set(only_2_list)))

print(f"Players in exactly two matches: {only_2_list_1}")

# 3. Find players who participated in only one match
for player in liste_total:
    if liste_total.count(player) == 1:
        only_1_list.append(player)

only_1_list_1 = sorted(list(set(only_1_list)))

print(f"Players in only one match: {only_1_list_1}")

# 4. Count total unique players
unique_list = list(set(liste_total))
count_tot = len(unique_list)

print(f"Total unique players: {count_tot}")

# 5. Find players in Match 1 only
only_match_1 = sorted(list(match1 - match2 - match3))

print(f"Players in Match 1 only: {only_match_1}")
