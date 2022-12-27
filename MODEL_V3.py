class Tournament:
    def __init__(self, name, date, place, tours, players,
                 time_control, description, number_of_rounds):
        
        self.name = str
        self.date = str
        self.place = str
        self.tours = list
        self.players = list
        self.time_control = str
        self.description = str
        self.number_of_rounds = 4
        
    def __str__(self) -> str:
        return  (f"\n- Nom du tounois: {self.name}\n"
                f"- Date du tournois: {self.date}\n"
                f"- Lieu du tournois: {self.place}\n"
                f"- Nombre de round: {self.number_of_rounds}\n"
                f"- Liste des tours: {self.tours}\n"
                f"- Liste des joueurs: {self.players}\n"
                f"- Mode de contrôle du temps: {self.time_control}\n"
                f"- Description: {self.description}\n"
                )
        
    def __repr__(self) -> str:
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
    def __init__(self, last_name, first_name, 
                 birth, sex,rank,points):
    
        self.last_name: str
        self.first_name: str  
        self.birth: str
        self.sex: str
        self.rank: int
        self.points: int 
        
    def __str__(self) -> str:
        return (f"- Nom: {self.last_name}\n"
                f"- Prénom: {self.first_name}\n"
                f"- Date de naissance: {self.birth}\n"
                f"- Sexe: {self.sex}\n"
                f"- rank: {self.rank}\n"
                f"- points: {self.points}\n"
                )
        
    def __repr__(self) -> str:
        return (f"{self.last_name}\n"
                f"{self.first_name}\n"
                f"{self.birth}\n"
                f"{self.sex}\n"
                f"{self.rank}\n"
                f"{self.points}\n"
                )
    
    