# EduCollect 🎓

Application web de collecte de données terrain sur les conditions éducatives en milieu rural (accès à l'eau, l'électricité, Internet, qualité des écoles).

## 🛠 Stack Technique

- **Backend** : Python / Flask
- **Base de données** : SQLite
- **Frontend** : HTML, Bootstrap 5, Chart.js, Leaflet.js
- **Cartographie** : OpenStreetMap via Leaflet

## 📂 Structure du projet

```
EduCollect/
├── app.py              # Application Flask principale
├── wsgi.py             # Point d'entrée WSGI (pour PythonAnywhere)
├── requirements.txt    # Dépendances Python
├── educollect.db       # Base SQLite (créée automatiquement)
├── templates/
│   ├── base.html       # Template de base (navbar, footer)
│   ├── index.html      # Formulaire de collecte
│   ├── dashboard.html  # Tableau de bord analytique (Chart.js)
│   └── map.html        # Carte interactive (Leaflet)
└── README.md
```

## 🚀 Lancement en local

```bash
# 1. Cloner le dépôt
git clone https://github.com/MoakoEkangoBillArmel/EduCollect.git
cd EduCollect

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement
# Windows :
venv\Scripts\activate
# Linux/Mac :
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer l'application
python app.py
```
Puis ouvrir http://127.0.0.1:5000

---

## ☁️ Déploiement sur PythonAnywhere

### Étape 1 : Créer un compte
Allez sur [www.pythonanywhere.com](https://www.pythonanywhere.com) et créez un compte gratuit.

### Étape 2 : Cloner le projet
Dans la console Bash de PythonAnywhere :
```bash
cd ~
git clone https://github.com/MoakoEkangoBillArmel/EduCollect.git
```

### Étape 3 : Créer un environnement virtuel
```bash
cd ~/EduCollect
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Étape 4 : Configurer l'application web
1. Allez dans l'onglet **Web** de PythonAnywhere
2. Cliquez sur **Add a new web app**
3. Choisissez **Manual configuration** → **Python 3.10**
4. Dans la section **Code** :
   - **Source code** : `/home/VOTRE_NOM/EduCollect`
   - **Working directory** : `/home/VOTRE_NOM/EduCollect`
5. Dans la section **WSGI configuration file**, cliquez sur le lien du fichier et remplacez TOUT son contenu par :

```python
import sys
import os

project_home = '/home/VOTRE_NOM/EduCollect'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
```

6. Dans la section **Virtualenv**, indiquez :
   `/home/VOTRE_NOM/EduCollect/venv`

7. Cliquez sur **Reload** (le gros bouton vert)

### Étape 5 : Tester
Votre application est accessible à :
`https://VOTRE_NOM.pythonanywhere.com`

---

## 👤 Auteur
**MOAKO EKANGO BILL ARMEL**

## 📄 Licence
MIT
