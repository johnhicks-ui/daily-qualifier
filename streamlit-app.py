import streamlit as st
import requests

st.title("Daily Qualifier")

def test_connection():
    url = "https://www.racingpost.com/racecards/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    return r.status_code

st.write("Status code:", test_connection())
