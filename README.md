# OFCRA SCRAPER
CLI tool written in Python that scrapes the latest missions from the [official OFCRA stats page](https://aar.ofcra.org/stats/missions.php) and exports structured data (missions + players) to JSON for further analysis.<br>

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
This script uses playwright to scrape everything and it scrapes every mission one by one, so it can be a bit slow, but you'll only need to do it once and then you can save a JSON with all missions and players.<br>
The workflow is the following: scrape missions -> save in an array of missions -> for each mission scrape players -> save in each mission's specific player array -> export to JSON.

## Why I made this
I've been learning web scraping with Python lately, I've done some programs using ScrapeGraphAI and Scrapy. I wanted to try something as simple and popular as Playwright too, but also wanted to create something useful out of it that everyone can use! Not only is this a learning project, but also a useful tool for you to use whenever you want!
