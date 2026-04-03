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
    import re

    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    page_text = soup.get_text(" ").lower()

    # RULE 1: handicap only
    if "handicap" not in page_text:
        return None

    rows = []

    for td in soup.find_all("td"):
        text = td.get_text(" ", strip=True)

        if not text:
            continue

        # try to capture weight (numbers like 11-2, 10-13 etc)
        weight_match = re.search(r"\b(\d{1,2}-\d{1,2})\b", text)

        # horse pattern (basic)
        if "." in text and text[0].isdigit():
            parts = text.split(".")
            if len(parts) > 1:
                name = parts[1].split("(")[0].strip()

                if len(name) > 2:
                    weight = weight_match.group(1) if weight_match else "0-0"

                    rows.append((name, weight))

    if not rows:
        return None

    # convert weight like 12-0 → numeric
    def weight_value(w):
        try:
            stones, pounds = w.split("-")
            return int(stones) * 14 + int(pounds)
        except:
            return 0

    # pick TOP WEIGHT
    top = sorted(rows, key=lambda x: weight_value(x[1]), reverse=True)[0]

    return top[0]
st.title("Daily Qualifier (API Build)")
links = get_racecards()
st.write("Race Links:")
st.write(links)
st.write("Qualifier from first race:")
st.write(get_runners(links[0]))


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

