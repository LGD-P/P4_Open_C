from datetime import datetime

class Tournament:
    def __init__(self, name=str, date=str, place=str, tours=list, players=list,
                 time_control=str, description=str, number_of_rounds=4):
        self.name = name
        self.date = date
        self.place = place
        self.tours = tours
        self.players = players
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        
    def __str__(self):
        return  (
                f"\n- Nom du tounois: {self.name}\n"
                f"- Date du tournois: {self.date}\n"
                f"- Lieu du tournois: {self.place}\n"
                f"- Nombre de round: {self.number_of_rounds}\n"
                f"- Liste des tours: {self.tours}\n"
                f"- Liste des joueurs: {self.players}\n"
                f"- Mode de contrôle du temps: {self.time_control}\n"
                f"- Description: {self.description}\n"
                )
        
    def __repr__(self):
        return (f"\n{self.name}\n"
                f"{self.date}\n"
                f"{self.place}\n"
                f"{self.number_of_rounds}\n"
                f"{self.tours}\n"
                f"{self.players}\n"
                f"{self.time_control}\n"
                f"{self.description}\n"
                )
        
    
    
class Players:
    def __init__(self, last_name=str, first_name=str, 
                 birth=str, sex=str,rank=int,points=int):
    
        self.last_name = last_name
        self.first_name = first_name  
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.points =  points
        
    def __str__(self):
        return (f"- Nom: {self.last_name}\n"
                f"- Prénom: {self.first_name}\n"
                f"- Date de naissance: {self.birth}\n"
                f"- Sexe: {self.sex}\n"
                f"- rank: {self.rank}\n"
                f"- points: {self.points}\n"
                )
        
    def __repr__(self):
        return (f"{self.last_name} "
                f"{self.first_name} "
                f"{self.birth} "
                f"{self.sex} "
                f"{self.rank} "
                f"{self.points}\n"
                )
        
        
    def add_in_tournament(self):
        print(f"- {self.last_name}, {self.first_name}, classement = {self.rank}\n")
