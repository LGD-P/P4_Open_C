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
     !5:
    :P@?.         !~
   :5@@@Y       !J##J~        !~        ..:..
    7@@#.       .5@@5.      .JBJJ      J&&#J!      :.:.:
   :Y&&&7.      :5&@5:      ^#&&&^   ~G@@@@&#J.    J&#&G.
   .!#@B^       :5@@5:      .Y&@J   .P@BJJ@@@G~    ?&&@P      :5G7
    .G@5         ~@@^        7&&!     °  5@@&B?     5@B.      ^&@Y
   .~B@&!       .7&@5.       :#&.       @@@@#5^     J@&:      :G@?
  ^BB&@@@P     !BB@@@#~     !Y&@B!     G@@@@&?.   .JG@@#^     :P@?
 ~5##&&&@@5:  !P#&&&@@B!   !#&&@@&!   ^P&&@@@?   .J&&&@@G^   7#&@@B^
 !J?JJJYYY5^  ???JJJYY5?  .??JJJY5J   7??JJYYY:  ^J?JJJY5!  :??JJY57 [bold green3]""")

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
        import time
        message = "\x1b[38;5;1mMerci et à Bientôt ! 🖖 \x1b[0m\n"
        for char in message:
            print(char, end="", flush=True)
            time.sleep(0.05)
