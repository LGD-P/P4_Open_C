<p align="center">
    <img src="menu.gif">
</p>

# ♖ Tournoi d'Echecs ♖

*Le but de ce projet est de créer un script qui gère des tournois d'échecs.*

* La mise en oeuvre devra respecter le schema :  Model View Controller.

```mermaid
graph LR;
    A[USER] --> |Ask something\n to the program| B(VIEW);
    B --> | Give the request \nto Controller |C{CONTROLLER};
    C --> | Ask which Model\n to use|D(MODEL);
    D --> | Give data\n back to Controller|C;
    C --> | Process request\n give answer back\n to the View|B; 
    B --> |display answer| A;
```

* L'algorithme suisse est implanté pour la gestion des paires de joueurs

* Une base de donnée TinyDB devra stocker les résultats du tournoi. Un rapport pourra être généré à la fin du tournoi. De plus, l'état du programme pourra être chargé à tout moment entre les actions de l'utilisateur.

* La norme PEP8 devra être vérifiée grâce à l'outil flake8


---

# ♝ Déroulement de base d'un tournoi: 

    1. Créer un nouveau tournoi.
    2. Ajouter huit joueurs.
    3. L'ordinateur génère des paires de joueurs pour le premier tour.
    4. Lorsque le tour est terminé, entrez les résultats.
    5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.

---

# ♘ Un tournoi est constitué de : 
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

---

# ♗ Un joueur est constitué de :

    • Nom de famille
    • Prénom
    • Date de naissance
    • Sexe
    • Classement
        ◦ Il s'agit d'un chiffre positif.

---

# ♔ Le rapport est constitué de :

    • liste de tous les joueurs par ordre alphabétique 
    • liste de tous les tournois 
    • nom et dates d’un tournoi donné 
    • liste des joueurs du tournoi par ordre alphabétique 
    • liste de tous les tours du tournoi et de tous les matchs du tour

---------

# ♙ Liste des commandes à exécuter pour lancer le programme : 

Pré-requis: se placer depuis le terminal dans le dossier où l'on exécute le script:

Avant toute chose on clone le répository git:

    git clone https://github.com/LGD-P/P4_Open_C.git

Une fois le projet cloné on crée et on active l'environnement virtuel:

    python3 -m venv env

suivi de:

```bash
source env/bin/activate
```  

Puis on lance l'installation des modules nécessaires au fonctionnement du script:

```bash
pip install -r requirements.txt
```

Générer avec flake8-html, un rapport montrant bien que le code ne contient aucune erreur de peluchage:

```bash
flake8 --format=html --htmldir=flake-report
```


Il n'y a plus qu'à exécuter le script:

```bash
python3 main.py
```

