from rich.console import Console
c = Console()


class Match:
    def __init__(self, match: list):
        self.match = match

    def __str__(self):
        return print(f"{self.match}")

    def __repre__(self):
        return print(f"{self.match}")
