# MOBILE LEGENDS MATCH LOGGER

# Player info
ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

# Hero roster (parallel lists)
heroes = ["Layla", "Tigreal", "Gusion", "Kagura", "Chou"]
roles = ["Marksman", "Tank", "Assassin", "Mage", "Fighter"]

# Display hero roster
print("==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

for i in range(len(heroes)):
    print(f" {i+1}. {heroes[i]:<11} [{roles[i]}]")

print("==========================================")

# Storage for match data
match_log = []
wins = 0
losses = 0

# Compute win rate and best match
matches_played = len(match_log)
win_rate = int((wins / matches_played) * 100) if matches_played > 0 else 0

best_match_index = -1
best_kda = -1

for i in range(matches_played):
    if match_log[i]["kda"] > best_kda:
        best_kda = match_log[i]["kda"]
        best_match_index = i

# Output formatted log
print("=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for i in range(matches_played):
    match = match_log[i]
    result_text = "WIN" if match["result"] == "W" else "LOSS"
    print(f"[{i+1}] {match['hero']:<11} | KDA: {match['kda']:.2f} | {result_text:<4} | {match['tag']}")

print("---------------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")

if best_match_index != -1:
    best = match_log[best_match_index]
    print(f"Best Match     : [{best_match_index+1}] {best['hero']}  (KDA: {best['kda']:.2f})")

print("=============================================")
