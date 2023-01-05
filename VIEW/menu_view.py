from rich.console import Console




c = Console()

class MenuView:
    def __init__(self, menu_view ):
        self.menu_view = menu_view

    
    def display_menu_and_get_choice(self):
        c.print("\n[bold yellow] :clipboard: CHESS MENU Veuillez faire un choix "\
            "dans le menu: :clipboard: [bold yellow]\n")
        for element in self.menu_view:
            c.print(self.menu_view[element]["label"])
        menu_choice = c.input("[bold red]==> [bold red]")

        if menu_choice in self.menu_view:
            return self.menu_view[menu_choice]["action"]()
        c.print("\n[bold red]Merci de faire un choix présent"\
                " dans le menu[bold red]\n")