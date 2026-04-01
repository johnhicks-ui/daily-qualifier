import streamlit as st
def test_open_race(url):
    import requests
    from bs4 import BeautifulSoup

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    if soup.title:
        return soup.title.text
    else:
        return "No title found (page likely blocked)"


# ----------------------------
# GET RACECARDS (Sporting Life)
# ----------------------------
def check_race(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text(" ").lower()

        # safer detection (less strict)
        if "race" not in text:
            return None

        if "handicap" in text:
            return f"Handicap race: {url}"

        return None

    except Exception:
        return None

# ----------------------------
# STREAMLIT APP
# ----------------------------
def check_race(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text(" ").lower()

        # safer detection (less strict)
        if "race" not in text:
            return None

        if "handicap" in text:
            return f"Handicap race: {url}"  

        return None

    except Exception:
        return None
# if st.button("Scan Today’s Races"):

    # with st.spinner("Scanning races..."):
    # races = get_racecards()[:15]
    # results = []

    # for r in races:
    #     res = check_race(r)
    #  res:
    #   results.append(res)

    if results:
        st.success(f"{len(results)} Races Found")
        for r in results:
            st.write("👉 " + r)
    else:
        st.warning("No races found")
        st.write(test_open_race("https://www.racingpost.com/racecards/"))
        
