from rich.console import Console

c = Console()


class ErrorMessages:

    def bug_to_creat_db(self):
        """Simple message to report that there is no data to record

        Returns:
            str: information message
        """
        return c.print("[bold red]Créer d'abord un tournois ou des joueurs"
                       "[bold red]")

    def bug_in_report(self):
        """Simple message to say that there is no data to data to show in 
        report section

        Returns:
            str: information message
        """
        return c.print(
            "[bold red] Vous n'avez aucune données à consulter.[bold red]")

    def bug_cannot_load_db(self):
        """Simple message to say that there is no db to load

        Returns:
            str: information message
        """
        return c.print("[bold red]Vous n'avez pas de base de données à \
            charger[bold red]")
