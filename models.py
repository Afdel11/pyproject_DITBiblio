import uuid #pour genere les id
from enum import Enum
from datetime import datetime

# 1. Énumération pour les statuts (évite les erreurs de saisie)
class StatutLivre(Enum):
    DISPONIBLE = "Disponible"
    EMPRUNTE = "Emprunté"
    RESERVE = "Réservé"


# 2. Classe Livre
class Livre:
    def __init__(self, isbn, titre, auteur, categorie, annee):
        self.isbn = isbn  # Numéro unique
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.annee = annee
        self.statut = StatutLivre.DISPONIBLE
        self.compteur_emprunts = 0

    def __str__(self):
        return f"[{self.isbn}] {self.titre} - {self.auteur} ({self.statut.value})"

# 3. Classe de base Utilisateur (Héritage)
class Utilisateur:
    def __init__(self, nom, email):
        self.id = str(uuid.uuid4())[:8] # Identifiant unique auto-généré
        self.nom = nom
        self.email = email
        self.historique_emprunts = []
        self.livres_actuels = [] # Liste des ISBN en cours d'emprunt
        self.limite_emprunts = 0 # Valeur par défaut

    def peut_emprunter(self):
        """Vérifie si l'utilisateur respecte son quota."""
        return len(self.livres_actuels) < self.limite_emprunts

# Sous-classes pour les types d'utilisateurs
class Etudiant(Utilisateur):
    def __init__(self, nom, email):
        super().__init__(nom, email)
        self.limite_emprunts = 3

class Enseignant(Utilisateur):
    def __init__(self, nom, email):
        super().__init__(nom, email)
        self.limite_emprunts = 10

class Personnel(Utilisateur):
    def __init__(self, nom, email):
        super().__init__(nom, email)
        self.limite_emprunts = 5

#Classe Emprunt
class Emprunt:
    def __init__(self, user_id, isbn, date_retour_prevue):
        self.user_id = user_id
        self.isbn = isbn
        self.date_emprunt = datetime.now().strftime("%Y-%m-%d")
        self.date_retour_prevue = date_retour_prevue
        self.date_retour_effective = None

#Classe Reservation
class Reservation:
    def __init__(self, isbn, user_id):
        self.isbn = isbn
        self.user_id = user_id
        self.date_reservation = datetime.now().strftime("%Y-%m-%d %H:%M")
