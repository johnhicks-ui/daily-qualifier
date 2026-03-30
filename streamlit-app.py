import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier")

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

        # RULE 1: handicap race
        if "handicap" not in text:
            return None

        # Get all runner rows (best available method)
        runners = soup.find_all("tr")

        qualifiers = []

        for runner in runners:
            row_text = runner.get_text().lower()

            # crude filters (we refine later)
            if "st" in row_text and "yo" in row_text:

                # RULE: last run winner (very basic)
                if "1st" in row_text:

                    qualifiers.append(row_text.strip()[:60])

        if qualifiers:
            return f"{url} -> {len(qualifiers)} possible"

        return None

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

    

    if results:
        st.success(f"{len(results)} Races Found")

        for r in results:
            st.write("👉 " + r)

    else:
        st.warning("No qualifiers today")
