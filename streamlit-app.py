import streamlit as st
import requests

st.title("Daily Qualifier (Betfair Build)")

# -----------------------------
# GET BETFAIR RACES (FREE ENDPOINT VIA PROXY)
# -----------------------------
def get_races():
    url = "https://api.allorigins.win/raw?url=https://www.betfair.com/exchange/plus/en/horse-racing"

    r = requests.get(url)

    if r.status_code != 200:
        return []

    return ["Sample Race 1", "Sample Race 2"]


# -----------------------------
# SIMULATED RUNNERS (TEMP)
# -----------------------------
def get_runners(race):
    return [
        {"horse": "Horse A", "odds": 2.5},
        {"horse": "Horse B", "odds": 3.0},
        {"horse": "Horse C", "odds": 6.0},
        {"horse": "Horse D", "odds": 10.0},
        {"horse": "Horse E", "odds": 12.0},
        {"horse": "Horse F", "odds": 14.0},
        {"horse": "Horse G", "odds": 16.0},
        {"horse": "Horse H", "odds": 20.0},
    ]


# -----------------------------
# QUALIFIER LOGIC (CORE RULES)
# -----------------------------
def find_qualifier(runners):

    if not (8 <= len(runners) <= 14):
        return None

    # sort by odds (favourite first)
    runners = sorted(runners, key=lambda x: x["odds"])

    fav = runners[0]
    second = runners[1]

    # simple rule: pick favourite for now
    return fav["horse"]


# -----------------------------
# MAIN
# -----------------------------
races = get_races()

st.write("Races found:", len(races))

qualifiers = []

for race in races:
    runners = get_runners(race)
    q = find_qualifier(runners)

    if q:
        qualifiers.append(q)

st.write("FINAL QUALIFIERS:")
st.write(qualifiers)
