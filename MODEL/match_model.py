from rich.console import Console
c = Console()


class Match:
    def __init__(self, match: list):
        self.match = match

    def __str__(self):
        for element in self.match:
            return print(f"{element}")

    def __repre__(self):
        for element in self.match:
            return print(f"{element}")
