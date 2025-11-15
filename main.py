# Kniznice
import requests
from bs4 import BeautifulSoup

# URL pre scrapovanie
URL = "https://news.ycombinator.com/"

# Ziskanie HTML obsahu pomocou GET
# Týmto krokom stiahneme HTML obsah stránky
print("ziskavanie obsahu ...")
response = requests.get(URL)
response.raise_for_status()  # overenie uspesnosti (status kod 200)

# Ziskanie texotveho obsahu (HTML kod stranky)
website_html = response.text

# Vytvorenie objektu BeautyfulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Ziskavanie dat

# 1. zoznam vsetkych clankov
# Nazvy clankov su v HTML znacke <a> s triedov 'titleline'
article_tags = soup.find_all(name="span", class_="titleline")

# 2. zistenie hodnotenia clankov
# Skore je v HTML značke <span> s triedou 'score'
article_scores = soup.find_all(name="span", class_="score")

# Zioznam pre data
article_texts = []
article_links = []
article_points = []

# Prechadzanie nazvov clankov
for article_tag in article_tags:
    # Zistenie nazvu clanku
    text = article_tag.getText()
    article_texts.append(text)

    # Ziskanie url clanku
    link = article_tag.find('a').get("href")
    article_links.append(link)

# Prechadzanie cez vsetky bodove hodnotenia
for score in article_scores:
    # Ziskanie hodnotenia ktore obsahuje body a nasledne vybrat len cast ktore je ciselna
    points = int(score.getText().split()[0])
    article_points.append(points)

# Zobrazenie vysledkov

# Cyklus pre vsetky clanky
# for i in range(len(article_texts)):
#     print(f"Názov: {article_texts[i]}")
#     print(f"Odkaz: {article_links[i]}")
#     # Nie vsetky clanky maju skore a preto moze tento cyklus padnut ak nie pocet skore rovny poctu clankov
#     if i < len(article_points):
#         print(f"Body: {article_points[i]}")
#     print("-" * 20)


# Ziskanie clanku s najvyssim poctom bodov
if article_points:
    highest_score = max(article_points)
    print(f"\nNajvyšší počet bodov: {highest_score}")

    # Najdenie najvysuieho indexu
    highest_score_index = article_points.index(highest_score)

    # Odkaz na clanok
    best_article_title = article_texts[highest_score_index]
    best_article_link = article_links[highest_score_index]

    print("\n--- Najvysie hodnotenie ma clanok: ---")
    print(f"Názov: {best_article_title}")
    print(f"Odkaz: {best_article_link}")
    print(f"Body: {highest_score}")
else:
    print("\nNa stranke nie je clanok s vysokym hodnotenim.")


