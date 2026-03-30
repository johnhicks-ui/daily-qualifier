import streamlit as st
import requests
from bs4 import BeautifulSoup
def get_racecards():
    try:
        url = "https://www.racingpost.com/racecards/"
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        races = []

        for link in soup.select("a.RC-meetingItem__link"):
            href = link.get("href")
            if href:
                races.append("https://www.racingpost.com" + href)

        return races

    except Exception:
        return []


# ----------------------------
# GET RACECARDS (Sporting Life)
# ----------------------------
def check_race(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text().lower()

        # Rule 1: handicap only
        if "handicap" not in text:
            return None

        # TEMP: skip runner count

        return f"Possible Qualifier: {url}"

    except Exception:
        return None
    except Exception:
        return None


# ----------------------------
# CHECK RACE
# ----------------------------
def check_race(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text().lower()

        # Rule 1: handicap only
        if "handicap" not in text:
            return None

        # TEMP: skip runner count (fix later)

        return f"Possible Qualifier: {url}"

    except Exception:
        return None

      


# ----------------------------
# STREAMLIT APP
# ----------------------------
if st.button("Scan Today’s Races"):

    with st.spinner("Scanning races..."):
        races = get_racecards()[:15]

        results = []

        for r in races:
            res = check_race(r)
            if res:
                results.append(res)

    if results:
        st.success(f"{len(results)} Qualifiers Found")
        for r in results:
            st.write("👉 " + r)
    else:
        st.warning("No qualifiers today")

        if res:
            results.append(res)

    status.empty()

    if results:
        st.success(f"{len(results)} Races Found")

        for r in results:
            st.write("👉 " + r)

    else:
        st.warning("No qualifiers today")
