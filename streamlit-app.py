import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier - Test Build")

# -----------------------------
# TEST FUNCTION ONLY
# -----------------------------
def test_open_race(url):
    import requests
    from bs4 import BeautifulSoup

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    base = "https://www.racingpost.com"

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.find_all("a")

    race_links = []

    for link in links:
        href = link.get("href")

        if href:
            # only keep real racecards (not navigation junk)
            if "/racecards/" in href and len(href.split("/")) > 3:
                full_url = base + href
                race_links.append(full_url)

    return race_links[:10]
# -----------------------------
# RUN TEST
# -----------------------------
st.write(test_open_race("https://www.racingpost.com/racecards/"))
