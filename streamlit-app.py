st.write("NEW CODE IS RUNNING")
import streamlit as st
import requests
from bs4 import BeautifulSoup
def get_racecards():
    return [
        "https://www.racingpost.com/racecards/177/clonmel/2026-04-02/916749",
        "https://www.racingpost.com/racecards/205/auteuil/2026-04-02/917017",
        "https://www.racingpost.com/racecards/27/kelso/2026-04-02/914327"
    ]
    
def get_runners(url):
    return "WORKING - READY FOR SCRAPER"



# -----------------------------
# DEBUG LOOP
# -----------------------------


st.title("Daily Qualifier (API Build)")

links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")
if links:
    st.write(get_runners(links[0]))

