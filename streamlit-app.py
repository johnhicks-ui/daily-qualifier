import streamlit as st

st.title("Daily Qualifier (API Build)")

# -----------------------------
# SIMPLE TEST DATA
# -----------------------------
races = [
    {
        "race_name": "Handicap Race Example",
        "runners": [
            {"horse": "Horse A", "weight": 12, "last_win": True, "bet_rank": 1},
            {"horse": "Horse B", "weight": 11, "last_win": False, "bet_rank": 2},
            {"horse": "Horse C", "weight": 12, "last_win": True, "bet_rank": 3},
            {"horse": "Horse D", "weight": 10, "last_win": True, "bet_rank": 2},
            {"horse": "Horse E", "weight": 9, "last_win": False, "bet_rank": 1},
            {"horse": "Horse F", "weight": 12, "last_win": True, "bet_rank": 2},
            {"horse": "Horse G", "weight": 8, "last_win": False, "bet_rank": 4},
            {"horse": "Horse H", "weight": 12, "last_win": True, "bet_rank": 1},
        ]
    }
]

st.write("Races loaded:", len(races))

# -----------------------------
# DEBUG LOOP
# -----------------------------
qualifiers = []

for race in races:
    st.write("Processing race:", race["race_name"])

    runners = race["runners"]
    race_size = len(runners)

    st.write("Runner count:", race_size)

    if not (8 <= race_size <= 14):
        st.write("Skipped (runner rule)")
        continue

    max_weight = max(r["weight"] for r in runners)
    st.write("Max weight:", max_weight)

    for horse in runners:
        st.write("Checking horse:", horse["horse"])

        if (
            horse["weight"] == max_weight and
            horse["last_win"] == True and
            horse["bet_rank"] <= 2
        ):
            qualifiers.append(horse["horse"])

st.write("FINAL QUALIFIERS:")
st.write(qualifiers)
