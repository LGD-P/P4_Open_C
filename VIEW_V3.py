from rich.console import Console

from CONTROLLER_V3 import MenuController
c = Console

class MenuView:
    def __init__(self, menu_view = dict, menu_choice = str ):
        self.menu_view = menu_view
        self.menu_choice = menu_choice
        self.launch_menu = MenuController().run_program
    
        
    def display_menu(self):
        c.print("\n[bold yellow] :clipboard: CHESS MENU Veuillez faire un choix "\
            "dans le menu: :clipboard: [bold yellow]\n")
        for element in MenuController.menu_view_in_controller:
            c.print(MenuController.menu_view_in_controller[element]["label"])
        self.menu_choice = c.input("[bold red]==> [bold red]")
        return self.menu_choice
        
    def display_choices(self):
        if self.menu_choice in MenuController.menu_view_in_controller:
            MenuController.menu_view_in_controller[self.menu_choice]["action"]()
        else:
            c.print("\n[bold red]Merci de faire un choix présent"\
                    " dans le menu[bold red]\n")
        
    
if __name__ == "__main__":
    MenuView().launch_menu
   

    