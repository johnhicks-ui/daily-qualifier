import streamlit as st
import requests
import re
import json
from bs4 import BeautifulSoup

st.title("Daily Qualifier (API Build)")


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

    # ACTUAL runner selector used by Racing Post
    for tag in soup.select("a[data-test-selector='link-listCourseNameLink']"):
        text = tag.get_text(strip=True)

        if text:
            runners.append(text)

    # fallback if above fails
    if not runners:
        for tag in soup.select("span[data-test-selector='participant-name']"):
            text = tag.get_text(strip=True)
            if text:
                runners.append(text)

    runners = list(dict.fromkeys(runners))

    return runners[0] if runners else None
links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")

if links:
    st.write(get_runners(links[0]))
