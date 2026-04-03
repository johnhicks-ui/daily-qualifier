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
    return "TEST_FUNCTION_IS_RUNNING"




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

st.title("Daily Qualifier (API Build)")

links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")
if links:
    st.write(get_runners(links[0]))

