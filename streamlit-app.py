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
        return f"Race found: {url}"
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
