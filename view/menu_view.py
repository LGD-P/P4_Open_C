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
        c.print("""[bold green3]
        ::
       !##7
       ?&@?               !7
     7YB&@#B?          ..^G#~.:            .:
     :P@@@@#^         .?G&@@@#J:           5B.         .J5?!~:
      !&@@@!            ^B@@@!           ~G&7PY.       .?&@@@&7J.        . . . ..
     .?&&@@J:           ^#&@@!          ^P@#P@@?      !B&&@@@@B@!!      .JG&G&BG:
    .!G&&&@#?.         !P&&&@#?.         ~B@@&Y:    ^G@@@@@&@@@&BG       ?@@@@@G          .^:
      :B@@#:            ^B@@#!           ~G&&&?.    ^YB@5!^!&@@@#?7      7G#&@&J         !B@@P
       5@@B              Y@@G            ^5@@#!.          :5@@@&#&Y       ~&@@7          ^#@@Y
      ^Y@@@~            .Y@@&:            ~&@5          ~P&@@@@&P7.       ^B@@7         .7#&@P^
    :7!P@@@&?:        .~!Y@@@B~.          !#@#.        Y@@@@@@@#BG^      .?G@@#:          J@&^
   :G&#&@@@@@#^       Y#B&@@@@@G.       ~YY&@@#?.       B@@@@@@&5~      :5Y&@@@#~        :J@@J
  :?#&&&&&@@@@Y^    .!B&@&&@@@@&?.     :B@@@@@@@7      :G&&@@@@@?       J&@@@@@@P.      5##@@@&
 :PGGGGBB##&@@@&:   JPGGBBB#&&@@@B.   !PGBB##&@@@5    ~5GBB##&@@@5    .YGBBB#&&@@B^   .YGB##&@@&?[bold green3]""")
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
