import streamlit as st
import requests

st.title("Daily Qualifier")

def test_connection():
    try:
        url = "https://www.racingpost.com/racecards/"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers, timeout=10)

        return f"Status code: {r.status_code}"

    except Exception as e:
        return f"Error: {str(e)}"

st.write(test_connection())
