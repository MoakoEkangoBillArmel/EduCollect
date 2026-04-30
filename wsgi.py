# Ce fichier est le point d'entrée WSGI pour PythonAnywhere.
# Dans la configuration PythonAnywhere, indiquez ce chemin pour le fichier WSGI :
#   /home/VOTRE_NOM_UTILISATEUR/EduCollect/wsgi.py
#
# Et dans la section "Source code", mettez :
#   /home/VOTRE_NOM_UTILISATEUR/EduCollect/

import sys
import os

# Ajouter le répertoire du projet au path Python
project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Importer l'application Flask
from app import app as application
