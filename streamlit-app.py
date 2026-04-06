import streamlit as st
import requests
from bs4 import BeautifulSoup

st.write("NEW CODE IS RUNNING")


def get_racecards():
import re
import json

def get_runners(url):
    import re
    import json

    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    html = r.text

    matches = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)

    for m in matches:
        if "runner" in m.lower() or "horse" in m.lower():
            try:
                data = json.loads(m)

                if isinstance(data, dict):
                    for key in ["runners", "entries", "horses"]:
                        if key in data:
                            runners = data[key]

                            names = []
                            for r in runners:
                                if isinstance(r, dict):
                                    for k in ["horseName", "name", "runnerName"]:
                                        if k in r:
                                            names.append(r[k])

                            names = list(dict.fromkeys(names))
                            return names[0] if names else None

            except:
                continue

    return None
        "https://www.racingpost.com/racecards/177/clonmel/2026-04-02/916749",
        "https://www.racingpost.com/racecards/205/auteuil/2026-04-02/917017",
        "https://www.racingpost.com/racecards/27/kelso/2026-04-02/914327"
    ]





st.title("Daily Qualifier (API Build)")

links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")
if links:
    st.write(get_runners(links[0]))
