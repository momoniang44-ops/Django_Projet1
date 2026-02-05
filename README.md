# Projet Django - MonProjet

## Description
Application web Django comprenant trois pages : Accueil, A propos et Contact.
Ce projet demontre l'utilisation des vues, templates avec heritage et fichiers statiques.

## Etapes suivies

### 1. Configuration de l'environnement
- Creation d'un environnement virtuel Python
- Installation de Django via pip

### 2. Creation du projet
- Initialisation du projet Django "MonProjet"
- Creation de l'application "monapp"

### 3. Implementation des vues
- Vue accueil : Page d'accueil avec message de bienvenue
- Vue a_propos : Informations sur le site avec une image
- Vue contact : Formulaire de contact et coordonnees

### 4. Configuration des templates
- Creation d'un template de base (base.html) avec heritage
- Implementation de 3 templates enfants

### 5. Fichiers statiques
- Ajout d'une feuille de style CSS
- Integration d'images

## Difficultes rencontrees
- Configuration initiale des chemins de fichiers statiques
- Comprehension du systeme de routage des URLs

## Fonctionnalites implementees
- Navigation entre les 3 pages
- Design responsive avec CSS
- Heritage de templates
- Chargement des fichiers statiques

## Installation et execution

```bash
# Cloner le projet
git clone [URL_DU_REPO]
cd MonProjet

# Creer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Installer les dependances
pip install -r requirements.txt

# Lancer le serveur
python manage.py runserver