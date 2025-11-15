# jednoduchy_scraper_python
Jednoduchy web scpraper napisany v pythone 3.10

Jednoduchy script fungujuci ako webscraper ktory zbiera data na prvej strane z webovej adresy: Hacker News (https://news.ycombinator.com/). Kde v konzole vypise clanok s najviac bodovym ohodnotenim.

Ako to funguje:

Import knižníc:

requests: Umožňuje stiahnuť HTML kód webovej stránky.
BeautifulSoup (z bs4): Umožňuje jednoducho prehľadávať a extrahovať informácie z HTML kódu.

Stiahnutie stránky:
requests.get(URL) pošle požiadavku na server Hacker News a stiahne obsah hlavnej stránky.
response.text obsahuje kompletný HTML kód stránky ako text.

Spracovanie HTML (Parsovanie):
BeautifulSoup(website_html, 'html.parser') vytvorí objekt, ktorý reprezentuje HTML štruktúru stránky. Tento objekt umožňuje jednoduché vyhľadávanie konkrétnych HTML elementov.

Extrakcia dát:
soup.find_all(name="span", class_="titleline"): Nájde všetky HTML značky <span>, ktoré majú CSS triedu titleline. V týchto značkách sa nachádzajú názvy článkov a odkazy na ne.
soup.find_all(name="span", class_="score"): Nájde všetky značky <span> s triedou score, kde je uložené bodové hodnotenie.

Spracovanie a uloženie dát:
Skript prechádza cez nájdené elementy a z každého extrahuje potrebné informácie:
.getText(): Získa textový obsah elementu (názov článku, text skóre).
.get("href"): Získa hodnotu atribútu href zo značky <a> (samotný odkaz).
Získané dáta sa ukladajú do zoznamov article_texts, article_links a article_points.

Vyhodnotenie a zobrazenie výsledkov:
Skript nájde článok s najvyšším bodovým hodnotením pomocou funkcie max() na zozname article_points.
Následne zistí jeho index a pomocou neho dohľadá príslušný názov a odkaz.
Na záver vypíše informácie o najlepšie hodnotenom článku na konzolu.

Ako spustiť skript:
Uistite sa, že máte nainštalované potrebné knižnice: pip install requests beautifulsoup4
Spustite skript z príkazového riadku: python main.py
