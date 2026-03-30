import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier")


# ----------------------------
# GET RACECARDS (Sporting Life)
# ----------------------------
def get_racecards():
    url = "https://www.sportinglife.com/racing/racecards"
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    races = []

    for link in soup.select("a[href*='/racing/racecards/']"):
        href = link.get("href")

        if href and "/racecards/" in href:
            full_url = "https://www.sportinglife.com" + href
            races.append(full_url)

    return list(set(races))


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

# TEMP: skip runner count filter (data unreliable right now)

return f"Possible Qualifier: {url}"
        return f"Possible Qualifier: {url}"

    except Exception:
        return None


# ----------------------------
# STREAMLIT APP
# ----------------------------
if st.button("Scan Today’s Races"):

    status = st.empty()
    status.write("Scanning...")

    races = get_racecards()[:15]
    results = []

    for r in races:
        res = check_race(r)

        if res:
            results.append(res)

    status.empty()

    if results:
        st.success(f"{len(results)} Races Found")

        for r in results:
            st.write("👉 " + r)

    else:
        st.warning("No qualifiers today")
