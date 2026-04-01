

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

    return r.text[:1000]

st.write("Sample race links:")
st.write(get_racecards())
