import streamlit as st

st.write("NEW CODE IS RUNNING")






# -----------------------------
# DEBUG LOOP
# -----------------------------

def get_racecards():
    return [
        "https://www.racingpost.com/racecards/177/clonmel/2026-04-02/916749",
        "https://www.racingpost.com/racecards/205/auteuil/2026-04-02/917017",
        "https://www.racingpost.com/racecards/27/kelso/2026-04-02/914327"
    ]

def get_runners(url):
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    runners = []

    # grab likely runner name links/text
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)

        if not text:
            continue

        # filter obvious junk
        if len(text) < 3:
            continue

        if any(x in text.lower() for x in [
            "racecard", "results", "news", "tips",
            "bet", "casino", "shop"
        ]):
            continue

        # avoid navigation/header noise
        if text[0].isupper():
            runners.append(text)

    # remove duplicates
    runners = list(dict.fromkeys(runners))

    return runners[0] if runners else None
st.title("Daily Qualifier (API Build)")

links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")
if links:
    st.write(get_runners(links[0]))

