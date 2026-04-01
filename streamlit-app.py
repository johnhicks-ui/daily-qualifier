import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier - Test Build")

# -----------------------------
# TEST FUNCTION ONLY
# -----------------------------
def test_open_race(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    return soup.get_text()[:300]

# -----------------------------
# RUN TEST
# -----------------------------
st.write(test_open_race("https://www.racingpost.com/racecards/"))
