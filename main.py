import os
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import json

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class Player:
    def __init__(self, name: str, side: str, kills: int, shots: int, role: str, death: int, tk: int):
        self.name = name
        self.side = side
        self.kills = kills
        self.shots = shots
        self.role = role
        self.death = death
        self.tk = tk
    
    def to_dict(self):
        return {
            "name": self.name,
            "side": self.side,
            "kills": self.kills,
            "shots": self.shots,
            "role": self.role,
            "death": self.death,
            "tk": self.tk
        }


class Mission:
    def __init__(self, url: str, name: str, mission_type: str, date: str, mission_map: str, author: str, duration: str, bluefor: int, redfor: int, greenfor: int, total: int, players=None):
        self.url = url
        self.name = name
        self.type = mission_type
        self.date = date
        self.map = mission_map
        self.author = author
        self.duration = duration
        self.bluefor = bluefor
        self.redfor = redfor
        self.greenfor = greenfor
        self.total = total
        self.players = players if players is not None else []

    def add_player(self, player: Player):
        self.players.append(player)

    def to_dict(self):
        return {
            "url": self.url,
            "name": self.name,
            "type": self.type,
            "date": self.date,
            "map": self.map,
            "author": self.author,
            "duration": self.duration,
            "bluefor": self.bluefor,
            "redfor": self.redfor,
            "greenfor": self.greenfor,
            "total": self.total,
            "players": [p.to_dict() for p in self.players]
        }


class Scraper:

    @staticmethod
    def scrape_missions(browser):
        url = "https://aar.ofcra.org/stats/missions.php"
        missions = []

        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("#missions tbody tr")

        rows = page.locator("#missions tbody tr").all()

        for row in rows:
            c = row.locator("td")
            link = c.nth(0).locator("a")

            mission = Mission(
                url=urljoin(page.url, link.get_attribute("href")),
                name=link.inner_text(),
                mission_type=c.nth(1).inner_text(),
                date=c.nth(2).inner_text(),
                mission_map=c.nth(3).inner_text(),
                author=c.nth(4).inner_text(),
                duration=c.nth(5).inner_text(),
                bluefor=int(c.nth(6).inner_text() or 0),
                redfor=int(c.nth(7).inner_text() or 0),
                greenfor=int(c.nth(8).inner_text() or 0),
                total=int(c.nth(9).inner_text() or 0),
            )

            missions.append(mission)

        page.close()
        return missions

    @staticmethod
    def scrape_players(browser, url: str):
        players = []

        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("h3:has-text('Players')")

        rows = page.locator("h3:has-text('Players') + table tbody tr").all()

        for row in rows:
            c = row.locator("td")
            link = c.nth(0).locator("a")

            player = Player(
                name=link.inner_text(),
                side=c.nth(1).inner_text(),
                kills=int(c.nth(2).inner_text() or 0),
                shots=int(c.nth(3).inner_text() or 0),
                role=c.nth(4).inner_text(),
                death=int(c.nth(5).inner_text() or 0),
                tk=int(c.nth(6).inner_text() or 0),
            )

            players.append(player)

        page.close()
        return players

    @staticmethod
    def scrape_all():
        cls()
        print("scraping missions + players...\n")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            missions = Scraper.scrape_missions(browser)

            for i, mission in enumerate(missions, 1):
                print(f"[{i}/{len(missions)}] Scraping players for: {mission.name}")

                mission.players = Scraper.scrape_players(browser, mission.url)

            browser.close()

        input("\nPress any key to continue...")
        return missions


class Menu:
    def show_ascii():
        print("""
                &&&$XXXX$&&&                
           &$Xx+ .;: +.+   :xxX$&           
         &X; x +  ;; + ;   ++  x+X&         
       $x+++ +: ;+xXXXXXX+:.;  x+++x$       
     $x++++++;x+:          :+++++++++x$     
   &$x+++++xx            ..    xx+++++x$&   
  &X+++++xx  ;.        :++x:    .xx+++++X&  
  $x++++x;   :++.     .+xx++      ;x++++x$  
 &+++++x:            .++xx+xx      :x+++++& 
&X+++x+x            :x+++.++.       +++;x+X&
$x+  +x:        ;x. .;;+x.;++       :x+  ;x$
$x;. +$       ;x+x.  ;x+:.:x;        $+ ::x$
$x+  +X       ..;++.+++x++++        .$+  ;x$
$x+  xx;        ;+X$Xx++++++.::     :x+  +x$
&X+++++x.       :X$$$Xxx++++++x:    ++++++X&
 &+++++x;   .++;+$$$Xx++:+++++x:   :x+++++& 
  $x++++x+ .;+++xx;. ;:;+;.+x+:   ;x++++x$  
  &X+++++xX.;+xx+..  :. .;..++...xx+++++X&  
   &$x++.x+xx.          ..   .;Xx+.:x+x$&   
     $x+: .++xx+;.        .;xxx;..: ;x$     
       $x+.:  ;+++xxXXXXxx+::.+. xxx$       
        &$Xxx;.+:+. : ::.. :..++xx$&        
           &$Xx+x+++;:++;+xxxxX$&           
                &&&$XXXX$$&&                
""")

    def main_menu():
        print("\t\tOFCRA SCRAPER")
        print("\t============================")
        Menu.show_ascii()
        print("\t============================\n")
        print("1. Scrape a page")
        print("2. Scrape a specific number of missions", "[WIP]")
        print("3. Export to JSON")
        print("4. Help")
        print("5. Exit")

        return input("\nEnter the desired option: ")
    
    def help():
        cls()
        print("1. Scrape all missions in the first page of https://aar.ofcra.org/stats/missions.php (10 missions)")
        print("2. Specify a number of missions to scrape, e.g. 1 for the latest mission")
        print("3. Export all scraped missions to JSON")
        print("4. Show help about the options")
        print("5. Exit the program")
        input()


def export_missions(missions: list[Mission]):
    data = []
    for m in missions:
        data.append(m.to_dict())

        with open("missions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("\nExported successfully.")
    input()


if __name__ == "__main__":
    missions = []

    while True:
        cls()
        option = Menu.main_menu()

        match option:
            case "1":
                missions = Scraper.scrape_all()
            case "2":
                print("\nThis is still work in progress...")
                input()
            case "3":
                export_missions(missions)
            case "4":
                Menu.help()
            case _:
                print("\nExiting the program...")
                break