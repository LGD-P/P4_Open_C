from VIEW.report_view import Report_View
from VIEW.error_messages import ErrorMessages


class ReportController:
    def __init__(self, tournament_list, player_list, round_list):
        self.tournament_list = tournament_list
        self.player_list = player_list
        self.round_list = round_list

    def report_players_alpahatical_order(self):
        Report_View()\
            .report_display_players_in_tournament_by_alphabetical_order(
                self.tournament_list)

    def report_player_by_rank(self):
        Report_View()\
            .report_display_players_in_tournament_by_rank(
                self.tournament_list)

    def report_tournament_list(self):
        Report_View().report_display_tournament_list(
            self.tournament_list)

    def report_tour_in_tournament(self):
        Report_View().report_display_tour_in_tournament(
            self.tournament_list, self.round_list)

    def report_match_in_tournament(self):
        Report_View().report_display_match_in_tournament(
            self.tournament_list)

    def report(self):
        """This function using tournament.view.display_report()
        allow acces to report menu.
        """
        '''                        
        self.tournament_view.display_report(
            self.tournament_list, self.round_list, self.unique_match_list,
            self.match_view, self.round_view)
        '''
        #

        if len(self.tournament_list) == 0:
            ErrorMessages().bug_in_report()

        else:

            secondary_report_menu = {
                "1": {
                    "label": "[bold blue]- 01. Liste de tous les joueurs "
                    "d'un tournoi par ordre alphabétique[bold blue]",
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
