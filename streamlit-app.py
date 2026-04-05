import streamlit as st
import requests
from bs4 import BeautifulSoup

st.write("NEW CODE IS RUNNING")


def get_racecards():
    return [
        "https://www.racingpost.com/racecards/177/clonmel/2026-04-02/916749",
        "https://www.racingpost.com/racecards/205/auteuil/2026-04-02/917017",
        "https://www.racingpost.com/racecards/27/kelso/2026-04-02/914327"
    ]


def get_runners(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    runners = []

    for tag in soup.find_all(["h2", "h3", "span", "strong"]):
        text = tag.get_text(strip=True)

        if not text:
            continue

        if len(text) < 3 or len(text) > 30:
            continue

        if any(x in text.lower() for x in ["racecard", "odds", "results", "news"]):
            continue

        if text[0].isupper() and any(c.isalpha() for c in text):
            runners.append(text)

    runners = list(dict.fromkeys(runners))

    return runners[0] if runners else None


st.title("Daily Qualifier (API Build)")

links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")
if links:
    st.write(get_runners(links[0]))
