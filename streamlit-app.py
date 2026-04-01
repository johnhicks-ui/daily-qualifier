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

    if soup.title:
        return soup.title.text
    else:
        return "No title found"

# -----------------------------
# RUN TEST
# -----------------------------
st.write(test_open_race("https://www.racingpost.com/racecards/"))
