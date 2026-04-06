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
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    html = r.text

    # STEP 1: find script blocks
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)

    for s in scripts:

        # look for big state objects
        if "__INITIAL_STATE__" in s or "racecard" in s.lower():

            # try to isolate JSON-like content
            start = s.find("{")
            end = s.rfind("}")

            if start != -1 and end != -1:
                chunk = s[start:end+1]

                try:
                    data = json.loads(chunk)

                    # try common structures
                    def find_horses(obj):
                        if isinstance(obj, dict):
                            for k, v in obj.items():
                                if k in ["runners", "entries", "horses"]:
                                    return v
                                res = find_horses(v)
                                if res:
                                    return res
                        elif isinstance(obj, list):
                            for item in obj:
                                res = find_horses(item)
                                if res:
                                    return res
                        return None

                    runners = find_horses(data)

                    if runners:
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
links = get_racecards()

st.write("Race Links:")
st.write(links)

st.write("Qualifier from first race:")

if links:
    st.write(get_runners(links[0]))
