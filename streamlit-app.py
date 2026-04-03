import streamlit as st
import requests
from bs4 import BeautifulSoup
def get_racecards():
    return [
        "https://www.racingpost.com/racecards/177/clonmel/2026-04-02/916749",
        "https://www.racingpost.com/racecards/205/auteuil/2026-04-02/917017",
        "https://www.racingpost.com/racecards/27/kelso/2026-04-02/914327"
    ]
    
def get_runners(url):
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    horses = []

    for td in soup.find_all("td"):
        text = td.get_text(strip=True)

        if text and text[0].isdigit() and "." in text:
            parts = text.split(".")
            if len(parts) > 1:
                name = parts[1].split("(")[0].strip()
                if len(name) > 2:
                    horses.append(name)

    horses = list(set(horses))

    # RULE 1: runner count
    if len(horses) < 8 or len(horses) > 14:
        return None

    # TEMP: return first horse (we improve next)
    return horses[0]
st.title("Daily Qualifier (API Build)")
links = get_racecards()
st.write("Race Links:")
st.write(links)
st.write("Sample runners from first race:")
st.write(get_runners(links[0]))
# -----------------------------
# SIMPLE TEST DATA
# -----------------------------
races = [
    {
        "race_name": "Valid Test Race",
        "runners": [
            {"horse": "Horse A", "weight": 12, "last_win": True, "bet_rank": 1},
            {"horse": "Horse B", "weight": 11, "last_win": False, "bet_rank": 2},
            {"horse": "Horse C", "weight": 10, "last_win": False, "bet_rank": 3},
            {"horse": "Horse D", "weight": 9, "last_win": False, "bet_rank": 4},
            {"horse": "Horse E", "weight": 8, "last_win": False, "bet_rank": 5},
            {"horse": "Horse F", "weight": 7, "last_win": False, "bet_rank": 6},
            {"horse": "Horse G", "weight": 6, "last_win": False, "bet_rank": 7},
            {"horse": "Horse H", "weight": 5, "last_win": False, "bet_rank": 8}
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
st.write("Race Links:")

