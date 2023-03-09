from view.report_view import Report_View
from view.error_and_user_messages import ErrorAndUserMessages
from view.round_view import RoundView


class ReportController:
    def __init__(self, tournament_list, player_list):
        self.tournament_list = tournament_list
        self.player_list = player_list

    def report_players_alpahatical_order(self):
        """This function use ReportView to display
        players by alphabetic order
        """
        Report_View()\
            .report_display_all_players_by_alphabetical_order(
                self.player_list)

    def report_players_in_tournament_by_alpahatical_order(self):
        """This function use ReportView to display
        players by alphabetic order
        """
        Report_View()\
            .report_display_players_in_tournament_by_alphabetical_order(
                self.tournament_list)

    def report_tournament_list(self):
        """This function use ReportView to display tournaments
        of tournament_list
        """
        Report_View().display_tournament(
            self.tournament_list)

    def report_tour_in_tournament(self):
        """This function use ReportView to display each touch
        in tournament_list
        """
        tournament_chosen = Report_View().report_display_tour_in_tournament(self.tournament_list)
        RoundView().display_for_tournament(tournament_chosen)

    def name_and_date_of_a_tournament(self):
        Report_View().name_and_date_of_touranment(self.tournament_list)

    def report(self):
        """This function using ReportView allow acces to report menu.
        """

        if len(self.tournament_list) == 0 and len(self.player_list) == 0:
            ErrorAndUserMessages().bug_in_report()

        else:

            secondary_report_menu = {
                "1": {
                    "label": "[bold blue]- 01. liste de tous les joueurs par ordre alphabétique.[bold blue]",
                    "action": self.report_players_alpahatical_order
                },
                "2": {
                    "label": "[bold blue]- 02. Liste de tous les tournois.[bold blue]",
                    "action": self.report_tournament_list
                },
                "3":
                    {
                    "label": "[bold blue]- 03. Nom et dates d’un tournoi donné. [bold blue] ",
                    "action": self.name_and_date_of_a_tournament
                },
                "4": {
                    "label": "[bold blue]- 04. Liste des joueurs du tournoi par ordre alphabétique [bold blue]",
                    "action": self.report_players_in_tournament_by_alpahatical_order
                },
                "5": {
                    "label": "[bold blue]- 05. Liste de tous les tours du tournoi et de tous les matchs du "
                    "tour.[bold blue]",
                    "action": self.report_tour_in_tournament
                },

            }

            Report_View().display_report(secondary_report_menu)
