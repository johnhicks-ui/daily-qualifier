import streamlit as st

st.title("Daily Qualifier (API Build)")

# -----------------------------
# SAMPLE STRUCTURED DATA
# -----------------------------
races = [
    {
        "race_name": "Wincanton Handicap",
        "runners": [
            {"horse": "Horse A", "weight": 11, "last_win": True, "bet_rank": 1},
            {"horse": "Horse B", "weight": 10, "last_win": False, "bet_rank": 3},
        ]
    },
    {
        "race_name": "Southwell Maiden",
        "runners": [
            {"horse": "Horse C", "weight": 12, "last_win": True, "bet_rank": 2},
            {"horse": "Horse D", "weight": 9, "last_win": True, "bet_rank": 1},
        ]
    }
]

# -----------------------------
# YOUR 5 RULES FILTER
# -----------------------------
def check_horse(horse, race_size):
    return (
        horse["weight"] == max_race_weight and
        horse["last_win"] == True and
        8 <= race_size <= 14 and
        horse["bet_rank"] <= 2
    )

# -----------------------------
# SIMPLE PROCESSING
# -----------------------------
qualifiers = []

for race in races:
    runners = race["runners"]
    race_size = len(runners)

    # rule 4: runners 8–14
    if not (8 <= race_size <= 14):
        continue

    max_weight = max(r["weight"] for r in runners)

    for horse in runners:
        if (
            horse["weight"] == max_weight and
            horse["last_win"] == True and
            horse["bet_rank"] <= 2
        ):
            qualifiers.append({
                "race": race["race_name"],
                "horse": horse["horse"]
            })
