def add_player(player_info):
    return None

   
menu = {
    "1":{
        "label": "ajouter un joueur",
        "action": add_player
        }
    }

for menu_key, menu_info in menu.items():
    print(f"{menu_key} : {menu_info['label']}")
    
choix = input("Choix utilisateur")


if choix in menu:
    menu[choix]["action"]()
    



    
