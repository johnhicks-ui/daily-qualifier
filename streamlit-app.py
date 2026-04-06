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
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import time

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(3)

        runners = []

        elements = driver.find_elements(By.CSS_SELECTOR, "[data-test-selector='participant-name']")

        for el in elements:
            name = el.text.strip()
            if name:
                runners.append(name)

        driver.quit()

        return runners[0] if runners else None

    except:
        driver.quit()
        return None
links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")

if links:
    st.write(get_runners(links[0]))
