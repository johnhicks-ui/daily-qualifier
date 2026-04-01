import streamlit as st
import requests
from bs4 import BeautifulSoup

def test_open_race(url):
    import requests
    from bs4 import BeautifulSoup

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # show us raw page text so we can find horses next
    return soup.get_text()[:1000]
