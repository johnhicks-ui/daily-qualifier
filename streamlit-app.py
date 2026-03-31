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

        text = soup.get_text(" ").lower()

        # safer detection (less strict)
        if "race" not in text:
            return None

        if "handicap" in text:
            return f"Handicap race: {url}"

        return None

    except Exception:
        return None

# ----------------------------
# STREAMLIT APP
# ----------------------------
def check_race(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text(" ").lower()

        # safer detection (less strict)
        if "race" not in text:
            return None

        if "handicap" in text:
            return f"Handicap race: {url}"

        return None

    except Exception:
        return None
