# Tournois d'Echecs 

*Le but de ce projet est de créer un script qui gère des tournois d'échecs.*

* La mise en oeuvre devra respecter le schema Model View Controller.

* L'algorithme suisse est mis en oeuvre pour la gestion des paires de joueurs

* Une base de donnée TinyDB devra stocker les résultats du tournois. Un rapport pourra être généré à la fin du tournois. De plus l'état du programme pourra être chargé à tout moment entre les actions de l'utilisateur.

* La norme PEP8 devra être vérifier grace à l'outil flake8

------

# Déroulement de base d'un tournois:

    1. Créer un nouveau tournoi.
    2. Ajouter huit joueurs.
    3. L'ordinateur génère des paires de joueurs pour le premier tour.
    4. Lorsque le tour est terminé, entrez les résultats.
    5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.



# Un tournois est constitué de: 
    • Nom
    • Lieu :
    • Date
        ◦ Il pourrait être organisé des tournois de plusieurs jours à l'avenir, ce qui devrait donc permettre de varier les dates.
    • Nombre de tours
        ◦ La valeur par défaut est 4.
    • Tournées
        ◦ La liste des instances rondes.
    • Joueurs
        ◦ Liste des indices correspondant aux instances du joueur stockées en mémoire.
    • Contrôle du temps
        ◦ C'est toujours un bullet, un blitz ou un coup rapide.
    • Description
        ◦ Les remarques générales du directeur du tournoi vont ici.

# Un joueur est constitué de:

    • Nom de famille
    • Prénom
    • Date de naissance
    • Sexe
    • Classement
        ◦ Il s'agit d'un chiffre positif.

# Le rapport est constitué de:


    • Liste de tous les acteurs :
        ◦ par ordre alphabétique ;
        ◦ par classement.
    • Liste de tous les joueurs d'un tournoi :
        ◦ par ordre alphabétique ;
        ◦ par classement.
    • Liste de tous les tournois.
    • Liste de tous les tours d'un tournoi.
    • Liste de tous les matchs d'un tournoi.



---------


Liste des commandes à exécuter pour lancer le programme:

Pré-requis: se placer depuis le terminal dans le dossier où l'on exécute le script:

Avant toute chose on clone le répository git:

    git clone https://github.com/LGD-P/P4_Open_C.git

Une fois le projet cloné on crée et on active l'environnement virtuel:

    python3 -m venv env
    source env/bin/activate

Puis on lance l'installation des modules nécessaires au fonctionnement du script:

    pip install -m requirements.txt

Il n'y a plus qu'à exécuter le script:

    python3 main.py

