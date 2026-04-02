
st.title("Daily Qualifier (API Build)")

# -----------------------------
# SIMPLE TEST DATA
# -----------------------------
races = [
    {
        "race_name": "Test Race",
        "runners": [
            {"horse": "Horse A", "weight": 12, "last_win": True, "bet_rank": 1},
            {"horse": "Horse B", "weight": 11, "last_win": False, "bet_rank": 2},
            {"horse": "Horse C", "weight": 10, "last_win": False, "bet_rank": 3}
        ]
    }
]

st.write("Races loaded:", len(races))

# -----------------------------
# DEBUG LOOP
# -----------------------------
qualifiers = []

for race in races:
    runners = race["runners"]
    race_size = len(runners)

    if not (8 <= race_size <= 14):
        continue

    max_weight = max(r["weight"] for r in runners)

    top_weight_horses = [h for h in runners if h["weight"] == max_weight]

    # 🚨 NEW RULE: must be UNIQUE top weight
    if len(top_weight_horses) != 1:
        continue

    horse = top_weight_horses[0]

    if horse["last_win"] and horse["bet_rank"] <= 2:
        qualifiers.append(horse["horse"])

st.write("FINAL QUALIFIERS:")
st.write(qualifiers)
