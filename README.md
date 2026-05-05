# OFCRA SCRAPER
CLI tool written in Python that scrapes the latest missions from the [official OFCRA stats page](https://aar.ofcra.org/stats/missions.php) and exports structured data (missions + players) to JSON for further analysis.<br>

![demo](assets/demo.gif)

For those who might not know: OFCRA is an ARMA 3 community that makes TVT missions almost every week, they upload their statistics to their official website.<br>

<img src="https://game.ofcra.org/img/logo.png" width="200"><br>

## Features
- Extracts all mission details (name, map, date...)
- Extracts all players for each mission along their stats (kills, shots, role...)
- Lets you export retrieved data to JSON

## Features to come
- Extract only specific players: currently it scrapes everything, but being able to scrape specific players will be faster and more useful for ARMA squads to analyze the JSON more easily
- Extract a specific number of missions: maybe you don't want to scrape the latest 10 missions, what if you just want to scrape one? it becomes unnecessarily slow.
- Extract more than 1 page: instead of scraping just 1 page (10 latest missions), why not scrape everything since 2017?! (or maybe just a few pages)

## Architecture
1. Scrape missions list
2. Store missions in array
3. Scrape players for each mission
4. Export final dataset to JSON

## Installation
Clone or download the repo and run the following command to install external libraries from the project directory: <br>
```cmd
pip install -r requirements.txt
```
Then run this command for the scraping library: <br>
```cmd
playwright install
```
Run the script with: <br>
```cmd
python main.py
```

## Why I made this
I've been learning web scraping with Python lately, I've done some programs using ScrapeGraphAI and Scrapy. I wanted to try something as simple and popular as Playwright too, but also wanted to create something useful out of it that everyone can use! Not only is this a learning project, but also a useful tool for you to use whenever you want!
