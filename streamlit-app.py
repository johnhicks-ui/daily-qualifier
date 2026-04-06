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
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    # extract race ID from URL
    race_id = url.split("/")[-1]

    api_url = f"https://www.racingpost.com/api/racecards/{race_id}"

    try:
        r = requests.get(api_url, headers=headers)

        if r.status_code != 200:
            return None

        data = r.json()

        runners = data.get("runners", [])

        names = []
        for r in runners:
            name = r.get("horseName") or r.get("name")
            if name:
                names.append(name)

        return names[0] if names else None

    except:
        return None
links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")

if links:
    st.write(get_runners(links[0]))
