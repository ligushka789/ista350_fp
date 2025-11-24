import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# путь к твоему локальному HTML
file_path = "ohimsry/2024 Album Releases, Music Releases - Album of The Year.html"

# читаем файл
with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

records = []

albums = soup.select("div.albumBlock")

print("Found albums:", len(albums))

for b in albums:
    # артист
    artist = b.select_one(".artistTitle")
    artist = artist.get_text(strip=True) if artist else None

    # альбом
    title = b.select_one(".albumTitle")
    title = title.get_text(strip=True) if title else None

    # дата + тип
    meta = b.select_one(".type")
    if meta:
        meta_text = meta.get_text(strip=True)
        date_part, _, release_type = meta_text.partition("•")
        release_date = date_part.strip() + " 2024"
        release_type = release_type.strip()
    else:
        release_date = None
        release_type = None

    # рейтинг(и)
    rating_rows = b.select("div.ratingRow")
    critic_score = None
    user_score = None

    if len(rating_rows) == 2:
        critic_score = rating_rows[0].select_one(".rating").get_text(strip=True)
        user_score = rating_rows[1].select_one(".rating").get_text(strip=True)
    elif len(rating_rows) == 1:
        user_score = rating_rows[0].select_one(".rating").get_text(strip=True)

    # ссылка
    link = b.find("a", href=lambda h: h and "/album/" in h)
    url = link["href"] if link else None

    records.append([
        title, artist, release_date, release_type,
        critic_score, user_score, url
    ])

df = pd.DataFrame(records, columns=[
    "Title", "Artist", "ReleaseDate", "ReleaseType",
    "CriticScore", "UserScore", "URL"
])

# Парсим день недели
def parse_weekday(date_str):
    try:
        return datetime.strptime(date_str.strip(), "%b %d %Y").strftime("%A")
    except:
        return None

df["Weekday"] = df["ReleaseDate"].apply(parse_weekday)

# Сохраняем в CSV (теперь с колонкой Weekday)
df.to_csv("csv/releases_2024_detailed.csv", index=False, encoding="utf-8")

print("csv/Saved with Weekday:", df["Weekday"].value_counts())


######################################################

import pandas as pd
import re

# -------------------------------
# PART 1 — Life Expectancy
# -------------------------------

life_html = "ohimsry/List of countries by life expectancy - Wikipedia.html"
tables = pd.read_html(life_html)
life_df = max(tables, key=lambda t: t.shape[0])

# normalize columns
life_df.columns = life_df.columns.map(str).str.strip()

# rename country column
for col in life_df.columns:
    if "Country" in col:
        life_df = life_df.rename(columns={col: "Country"})
        break

# -------------------------------
# PART 2 — Healthcare Index
# -------------------------------

hc_html = "ohimsry/Health Care Index by Country 2025 Mid-Year.html"

with open(hc_html, "r", encoding="utf-8") as f:
    text = f.read()

pattern = r"addRows\(\[(.*?)\]\);"
match = re.search(pattern, text, re.S)

rows_raw = match.group(1)
rows = re.findall(r"\['(.+?)',\s*([0-9]+\.[0-9]+)\]", rows_raw)

health_df = pd.DataFrame(rows, columns=["Country", "Healthcare_Index"])
health_df["Healthcare_Index"] = health_df["Healthcare_Index"].astype(float)

# -------------------------------
# PART 3 — Merge
# -------------------------------

merged = pd.merge(life_df, health_df, on="Country", how="inner")
merged.to_csv("csv/life_expectancy.csv", index=False)

print("Saved: csv/life_expectancy.csv")





































##################################


import requests
import pandas as pd

url = (
    "https://books.google.com/ngrams/json?"
    "content=ecology,environment&year_start=1800&year_end=2019&corpus=26&smoothing=3"
)

response = requests.get(url).json()

years = list(range(1800, 2020))
data = {"year": years}

for entry in response:
    word = entry["ngram"]
    data[word] = entry["timeseries"]

df = pd.DataFrame(data)

df.to_csv("csv/ngram_ecology_environment.csv", index=False)
print("Saved: csv/ngram_ecology_environment.csv")
