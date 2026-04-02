import streamlit as st
import requests
from bs4 import BeautifulSoup
def get_racecards():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.racingpost.com/racecards/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

    if "/racecards/" in href and href.count("/") >= 5:
    if any(x in href for x in ["/kelso/", "/clonmel/", "/aintree/", "/leopardstown/", "/navan/"]):
            if href.startswith("http"):
                links.append(href)
            else:
                links.append("https://www.racingpost.com" + href)

    return list(set(links))

st.title("Daily Qualifier (API Build)")

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
st.write(get_racecards()[:10])
