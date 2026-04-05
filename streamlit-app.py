import streamlit as st
import requests
from bs4 import BeautifulSoup

st.write("NEW CODE IS RUNNING")


def get_racecards():
    return [
        "https://www.racingpost.com/racecards/177/clonmel/2026-04-02/916749",
        "https://www.racingpost.com/racecards/205/auteuil/2026-04-02/917017",
        "https://www.racingpost.com/racecards/27/kelso/2026-04-02/914327"
 def get_runners(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(" ")

    words = text.split()

    runners = []

    for i in range(len(words) - 1):
        w = words[i].strip()

        # horse names are usually proper nouns, 2–4 words max
        if (
            w[0:1].isupper()
            and 3 <= len(w) <= 25
            and w.lower() not in ["racecard", "results", "news", "tips"]
        ):
            runners.append(w)

    runners = list(dict.fromkeys(runners))

    return runners[0] if runners else None   ]





st.title("Daily Qualifier (API Build)")

links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")
if links:
    st.write(get_runners(links[0]))


