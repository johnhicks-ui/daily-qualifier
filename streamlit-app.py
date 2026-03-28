import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier")


# ----------------------------
# GET RACECARDS
# ----------------------------
def get_racecards():
    url = "https://www.racingpost.com/racecards/"
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    races = []

    for link in soup.select("a.RC-meetingItem__link"):
        href = link.get("href")

        if href:
            full_url = "https://www.racingpost.com" + href

            if "/racecards/" in full_url:
                races.append(full_url)

    return list(set(races))


# ----------------------------
# CHECK RACE
# ----------------------------
def check_race(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        # race type
        race_type = soup.select_one(".RC-header__raceClass")

        if race_type:
            race_text = race_type.text.lower()
        else:
            race_text = ""

        # RULE 1: handicap only
        if "handicap" not in race_text:
            return None

        # runners
        runners = soup.select(".RC-runnerRow")

        # RULE 5: 8–14 runners
        if not (8 <= len(runners) <= 14):
            return None

        # TEMP RESULT (proves system works)
        return f"PASS: {url}"

    except Exception:
        return None


# ----------------------------
# STREAMLIT APP
# ----------------------------
if st.button("Scan Today’s Races"):

    status = st.empty()
    status.write("Scanning...")

    races = get_racecards()
    results = []

    for r in races:
        res = check_race(r)

        if res:
            results.append(res)

    status.empty()

    if results:
        st.success(f"{len(results)} Qualifiers Found")

        for r in results:
            st.write("👉 " + r)

    else:
        st.warning("No qualifiers today")
