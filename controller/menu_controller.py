from rich.console import Console


from view.menu_view import MenuView


from controller.player_controller import PlayerController
from controller.tournament_controller import TournamentController
from controller.db_controller import DataBase
from controller.report_controller import ReportController


c = Console()


class MenuController:
    def __init__(self):
        self.running_program = True
        self.player_controller = PlayerController([])
        self.tournament_controller = TournamentController([], self.player_controller.player_list)
        self.db_controller = DataBase(self.tournament_controller.player_list,
                                      self.tournament_controller.tournament_list)
        self.report_view = ReportController(self.tournament_controller.tournament_list,
                                            self.tournament_controller.player_list)
        self.main_menu_view_in_controller = MenuView({
            "1": {
                "label": "[bold blue]- 1. Créer des tournois :pencil: [bold blue]",
                "action": self.tournament_controller.add_tournament,
            },
            "2": {
                "label": "[bold blue]- 2. Créer des joueurs :pencil: [bold blue]",
                "action": self.player_controller.add_player,
            },
            "3": {
                "label": "[bold blue]- 3. Ajouter des joueurs à un tournois :pencil:[bold blue]",
                "action": self.tournament_controller.add_player_in_tournament,
            },
            "4": {
                "label": "[bold blue]- 4. Lancer un Round :watch:[bold blue]",
                "action": self.tournament_controller.
                fill_round_instance_create_announcement
            },
            "5": {
                "label": "[bold blue]- 5. Ajouter des résultats :trophy: [bold blue]",
                "action": self.tournament_controller.fill_result,
            },
            "6": {
                "label": "[bold blue]- 6. Montrer le rapport :bar_chart: [bold blue]",
                "action": self.report_view.report,
            },
            "7": {
                "label": "[bold blue]- 7. Sauvegarder les données :dvd: [bold blue]",
                "action": self.db_controller.creat_db
            },
            "8": {
                "label": "[bold blue]- 8. Charger les données 🔄 [bold blue]",
                "action": self.db_controller.load_data,
            },
            "9": {
                "label": "[bold blue]- 9. Quitter :raising_hand:  "
                "[bold blue]\n",
                "action": self.quit_menu,
            }
        })

    def run_program(self):
        """This function creat the loop used to run main menu"""
        while self.running_program:
            self.main_menu_view_in_controller.display_menu_and_get_choice()

    def quit_menu(self):
        """Quit menu killing main loop
        """
        self.main_menu_view_in_controller.quit_message()
        self.running_program = False
