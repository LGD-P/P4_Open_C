from datetime import datetime
from rich.console import Console

import random
c = Console()


class Tournament:
    def __init__(self, name: str, date: str, place: str, tours: list, players: list,
                 time_control: str, description: str, number_of_rounds: int = 4, player_score: dict = []):
        self.name = name
        self.date = date
        self.place = place
        self.tours = tours
        self.players = players
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.player_score = player_score

    def __str__(self):
        return (
            f"\n- Nom du tounois: {self.name}\n"
            f"- Date du tournois: {self.date}\n"
            f"- Lieu du tournois: {self.place}\n"
            f"- Nombre de round: {self.number_of_rounds}\n"
            f"- Liste des tours: {self.tours}\n"
            f"- Liste des joueurs: {self.players}\n"
            f"- Mode de contrôle du temps: {self.time_control}\n"
            f"- Description: {self.description}\n"
            f"- Nombre de round: {self.number_of_rounds}\n"
            f"- Score des joueurs:{self.player_score}\n")

    def __repr__(self):
        return (
            f"\n- Nom du tounois: {self.name}\n"
            f"- Date du tournois: {self.date}\n"
            f"- Lieu du tournois: {self.place}\n"
            f"- Nombre de round: {self.number_of_rounds}\n"
            f"- Liste des tours: {self.tours}\n\n"
            f"- Liste des joueurs: {self.players}\n\n"
            f"- Mode de contrôle du temps: {self.time_control}\n"
            f"- Nombre de round: {self.number_of_rounds}\n\n"
            f"- Score des joueurs :{self.player_score}\n")


class Player:
    def __init__(self, last_name: str, first_name: str,
                 birth: str, sex: str, rank: int):

        self.last_name = last_name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.rank = rank

    def __str__(self):
        return (f"- Nom: {self.last_name}\n"
                f"- Prénom: {self.first_name}\n"
                f"- Date de naissance: {self.birth}\n"
                f"- Sexe: {self.sex}\n"
                f"- rank: {self.rank}\n"
                )

    def __repr__(self):
        return (f"\n- Nom : {self.last_name}"
                f" Prénom : {self.first_name} "
                f" Date de naissance : {self.birth} "
                f" Sexe : {self.sex}"
                f" rank: {self.rank}")


quick_players_list = [
    Player("DENIS", "Laurent", "11-12-2000", "h", 321),
    Player("LAURENT", "Denis", "11-10-2005", "h", 123),
    Player("MOINE", "Alice", "10-10-1990", "f", 100),
    Player("VAULT", "Lise", "01-02-1980", "f", 10),
    Player("CREPIN", "Maurice", "12-07-1950", "h", 40),
    Player("TIAGO", "Daniela", "05-06-1977", "f", 35),
    Player("EDON", "Gabrielle", "09-03-1985", "f", 25),
    Player("PATTON", "Gabriel", "09-03-1970", "h", 20)]


quick_tournament = [
    Tournament("PARIS Chess-Event", "Paris",
               datetime.now().strftime("%d-%m-%Y"),
                   [], quick_players_list[0:9], "Blitz",
               "Description", 4, [])
]


round = random.randint(0, 1)

for tournament in quick_tournament:
    for player in tournament.players:
        if round == 0:
            score = 0
        else:
            score = random.randint(0, 5)
        #score = 0
        tournament.player_score.append(
            {"player": player, "player_rank": player.rank, 'score': score})


tournament = quick_tournament[0]


c.print(tournament.player_score)

"""tournament_to_run_players = sorted(tournament.player_score,
                                   key=itemgetter("player_rank", 'score'))

c.print(tournament_to_run_players)

"""


if round == 0:
    print("pas de round \n")
    tournament_to_run_players = sorted(
        tournament.player_score, key=lambda k: (k["player_rank"]))


elif round > 0:
    print("déjà un Round \n")
    tournament_to_run_players = sorted(
        tournament.player_score, key=lambda k: (-k["score"], k["player_rank"]))

c.print(tournament_to_run_players)


half_list = len(tournament_to_run_players)//2

first_part = tournament_to_run_players[0:half_list]
second_part = tournament_to_run_players[half_list:]
c.print(first_part)
c.print("[bold red ]*************************[bold red]")
c.print(second_part)
