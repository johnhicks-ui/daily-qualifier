import streamlit as st

st.write("NEW CODE IS RUNNING")

def get_runners(url):
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    horses = []

    for td in soup.find_all("td"):
        text = td.get_text(strip=True)

        if text and text[0].isdigit() and "." in text:
            parts = text.split(".")
            if len(parts) > 1:
                name = parts[1].split("(")[0].strip()

                if len(name) > 2:
                    horses.append(name)

    horses = list(set(horses))

    if not horses:
        return None

    return horses[0]




# -----------------------------
# DEBUG LOOP
# -----------------------------

def get_racecards():
    return [
        "https://www.racingpost.com/racecards/177/clonmel/2026-04-02/916749",
        "https://www.racingpost.com/racecards/205/auteuil/2026-04-02/917017",
        "https://www.racingpost.com/racecards/27/kelso/2026-04-02/914327"
st.title("Daily Qualifier (API Build)")

links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")
if links:
    st.write(get_runners(links[0]))

