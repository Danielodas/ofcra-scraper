import os

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


class Mission:
    def __init__(self, mission_type: str, date: str, mission_map: str, author: str, duration: str, bluefor: int, redfor: int, greenfor: int, total: int, players=None):
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


class Scraper:
    pass


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
        print("1. Scrape a page", "[WIP]")
        print("2. Scrape a specific number of missions", "[WIP]")
        print("3. Export to JSON", "[WIP]")
        print("4. Help")
        print("5. Exit")

        return input("\nEnter the desired option: ")
    
    def help():
        cls()
        print("1. Scrape all missions in the first page of https://aar.ofcra.org/stats/missions.php")
        print("2. Specify a number of missions to scrape, e.g. 1 for the latest mission")
        print("3. Export all scraped missions to JSON")
        print("4. Show help about the options")
        print("5. Exit the program")
        input()


if __name__ == "__main__":
    missions = []

    while True:
        cls()
        option = Menu.main_menu()

        match int(option):
            case 1:
                continue
            case 2:
                continue
            case 3:
                continue
            case 4:
                Menu.help()
            case _:
                print("\nExiting the program...")
                break