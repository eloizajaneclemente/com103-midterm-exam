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

# Loop for 4 matches
for i in range(1, 5):
    print(f"--- MATCH {i} ---")
    hero_num = int(input("Hero number (0 to skip): "))

    if hero_num == 0:
        continue

    if 1 <= hero_num <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()

        
        denominator = deaths if deaths != 0 else 1
        kda = (kills + assists) / denominator

        
        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

       
        if result == "W":
            wins += 1
        else:
            losses += 1

        
        match_log.append({
            "hero": heroes[hero_num - 1],
            "kda": kda,
            "result": result,
            "tag": tag
        })

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
