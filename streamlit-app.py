import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Daily Qualifier")

def get_racecards():
    url = "https://www.racingpost.com/racecards/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    races = []
    for link in soup.select("a.RC-meetingItem__link"):
        href = link.get("href")
        if href:
            races.append("https://www.racingpost.com" + href)
    return races

def check_race(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        race_type = soup.select_one(".RC-header__raceClass")
        if not race_type or "handicap" not in race_type.text.lower():
            return None

        runners = soup.select(".RC-runnerRow")
        if not (8 <= len(runners) <= 14):
            return None

        horses = []

        for r in runners:
            name = r.select_one(".RC-runnerName").text.strip()
            weight = r.select_one(".RC-runnerWgt").text.strip()

            st_, lb_ = map(int, weight.split("-"))
            total = st_ * 14 + lb_

            horses.append((name, total))

        top_weight = max(h[1] for h in horses)
        top = [h for h in horses if h[1] == top_weight]

        if len(top) != 1:
            return None

        horse_name = top[0][0]

        

       

        if not any(horse_name in p for p in parts):
            return None

        header = soup.select_one(".RC-header__timeCourse").text.strip()

        return f"{header} — {horse_name}"

    except:
        return None


if st.button("Scan Today’s Races"):
    st.write("Scanning...")

    races = get_racecards()
    results = []

    for r in races:
        res = check_race(r)
        if res:
            results.append(res)

    if results:
    st.success(f"{len(results)} Qualifiers Found")
    for r in results:
        st.write("👉 " + r)
else:
    st.warning("No qualifiers today")
