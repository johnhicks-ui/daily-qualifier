import streamlit as st
import requests

st.title("Daily Qualifier (Betfair Build)")

# -----------------------------
# GET BETFAIR RACES (FREE ENDPOINT VIA PROXY)
# -----------------------------
def get_races():
    url = "https://api.allorigins.win/raw?url=https://www.betfair.com/exchange/plus/en/horse-racing"

    r = requests.get(url)

    if r.status_code != 200:
        return []

    return ["Sample Race 1", "Sample Race 2"]


# -----------------------------
# SIMULATED RUNNERS (TEMP)
# -----------------------------
def get_runners(url):
    return [
        {"horse": "Horse A", "odds": 2.5},
        {"horse": "Horse B", "odds": 3.0},
        {"horse": "Horse C", "odds": 6.0},
        {"horse": "Horse D", "odds": 10.0},
        {"horse": "Horse E", "odds": 12.0},
        {"horse": "Horse F", "odds": 14.0},
        {"horse": "Horse G", "odds": 16.0},
        {"horse": "Horse H", "odds": 20.0},
    ]

st.write("FINAL QUALIFIERS:")
st.write(qualifiers)
