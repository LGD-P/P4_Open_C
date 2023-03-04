from rich.console import Console


c = Console()


class MenuView:
    def __init__(self, main_menu_view):
        self.main_menu_view = main_menu_view

    def display_menu_and_get_choice(self):
        """This function displays the dict view for menu_controller,
        and allows the execution of each menu function

        Returns:
            function: function choosen by user choice
        """
        c.print("\n[bold yellow] :clipboard: CHESS MENU Veuillez faire un "
                "choix dans le menu: :clipboard: [bold yellow]\n")
        for element in self.main_menu_view:
            c.print(self.main_menu_view[element]["label"])
        menu_choice = c.input("[bold red]==> [bold red]")

        if menu_choice in self.main_menu_view:
            return self.main_menu_view[menu_choice]["action"]()
        c.print("\n[bold red]Merci de faire un choix présent"
                " dans le menu[bold red]\n")

    def quit_message(self):
        c.print("[bold red]Merci à bientôt[bold red]")