import streamlit as st

st.title("Daily Qualifier (API Build)")

# -----------------------------
# SIMPLE TEST DATA
# -----------------------------
races = [
    {
        "race_name": "Test Race 1",
        "runners": [
            {"horse": "Horse A", "weight": 11, "last_win": True, "bet_rank": 1},
            {"horse": "Horse B", "weight": 10, "last_win": False, "bet_rank": 3},
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
