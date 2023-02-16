from rich.console import Console

c = Console()


class ErrorMessages:

    def bug_in_db(self):
        """Simple message to report that there is no data to record

        Returns:
            str: information message
        """
        return c.print("[bold red]Créer d'abord un tournois ou des joueurs"
                       "[bold red]")
