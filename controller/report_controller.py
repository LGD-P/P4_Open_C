from view.report_view import Report_View
from view.error_and_user_messages import ErrorAndUserMessages
from view.round_view import RoundView
from view.match_view import MatchView


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

    def report_player_by_rank(self):
        """This function use ReportView to display player by rank
        """
        Report_View()\
            .report_display_players_in_tournament_by_rank(
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

    def report_match_in_tournament(self):
        """This function use ReportView to display each match
        in tournament list
        """
        tournament_chosen = Report_View().report_display_match_in_tournament(self.tournament_list)
        MatchView().display_match_for_report(tournament_chosen)

    def report(self):
        """This function using ReportView allow acces to report menu.
        """

        if len(self.tournament_list) == 0 and len(self.player_list) == 0:
            ErrorAndUserMessages().bug_in_report()

        else:

            secondary_report_menu = {
                "1": {
                    "label": "[bold blue]- 01. Liste de tous les joueurs "
                    "par ordre alphabétique[bold blue]",
                    "action": self.report_players_alpahatical_order
                },
                "2": {
                    "label": "[bold blue]- 02. Liste de tous les joueurs d'un "
                    "tournoi "
                    "par classement[bold blue]",
                    "action": self.report_player_by_rank
                },
                "3": {
                    "label": "[bold blue]- 03. Liste de tous les tournois."
                    "[bold blue]",
                    "action": self.report_tournament_list
                },
                "4": {
                    "label": "[bold blue]- 04. Liste de tous les tours d'un "
                    "tournoi.[bold blue]",
                    "action": self.report_tour_in_tournament
                },
                "5": {
                    "label": "[bold blue]- 05. Liste de tous les matchs d'un "
                    "tournoi."
                    "[bold blue]",
                    "action": self.report_match_in_tournament
                },

            }

            Report_View().display_report(secondary_report_menu)
