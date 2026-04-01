

import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier (Stable Build)")

def get_racecards():
    url = "https://www.attheraces.com/racecards"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    links = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and "racecard" in href:
            if href.startswith("/"):
                href = "https://www.attheraces.com" + href
            links.append(href)

    return links[:10]

st.write("Sample race links:")
st.write(get_racecards())
