import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier - Test Build")

# -----------------------------
# TEST FUNCTION ONLY
# -----------------------------
def test_open_race(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.find_all("a")

    race_links = []

    for link in links:
        href = link.get("href")
        if href and "racecards" in href:
            race_links.append(href)

    return race_links[:10]

# -----------------------------
# RUN TEST
# -----------------------------
st.write(test_open_race("https://www.racingpost.com/racecards/"))
