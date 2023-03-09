from rich.console import Console

c = Console()


class ErrorAndUserMessages:

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
        return c.print("[bold red]Vous n'avez pas de base de données à charger[bold red]")

    def database_created(self):
        """Simple message to say that database is created

        Returns:
            str: information message
        """
        return c.print("\n[bold green3]La sauvegarde a bien été réalisée 👍 [bold green3]")

    def database_loaded(self):
        """Simple message to say that database is loaded

        Returns:
            str: information message
        """
        return c.print("\n[bold green3]La base de donnée a bien été chargée 👍 [bold green3]")

    def score_added(self):
        """Simple message to say that database is loaded

        Returns:
            str: information message
        """
        return c.print("\n[bold green3]Les scores ont été ajoutés 👍 [bold green3]")
