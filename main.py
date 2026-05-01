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
    pass