# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import statistics
from datetime import datetime

app = Flask(__name__)
DATABASE = 'educollect.db'

def get_db():
    """Retourne une connexion à la base de données SQLite."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # pour accéder aux colonnes par nom
    return conn

def init_db():
    """Crée la table si elle n'existe pas."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            village TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            water_access TEXT NOT NULL,
            electricity_access TEXT NOT NULL,
            internet_access TEXT NOT NULL,
            school_quality INTEGER NOT NULL,
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialise la base au démarrage
with app.app_context():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Reçoit les données du formulaire et les enregistre."""
    data = (
        request.form['village'],
        float(request.form['latitude']),
        float(request.form['longitude']),
        request.form['water_access'],
        request.form['electricity_access'],
        request.form['internet_access'],
        int(request.form['school_quality']),
        request.form.get('comment', '')  # optionnel
    )
    conn = get_db()
    conn.execute('''
        INSERT INTO survey (village, latitude, longitude, water_access, electricity_access, internet_access, school_quality, comment)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    """Page d'analyse descriptive."""
    conn = get_db()
    surveys = conn.execute('SELECT * FROM survey').fetchall()
    conn.close()

    # Calculs statistiques globaux
    total = len(surveys)
    stats = {}
    if total > 0:
        school_scores = [s['school_quality'] for s in surveys]
        stats['moyenne_qualite'] = round(statistics.mean(school_scores), 2)
        stats['mediane_qualite'] = statistics.median(school_scores)
        stats['total'] = total
        stats['pourcent_eau'] = round(100 * sum(1 for s in surveys if s['water_access'] == 'Oui') / total, 1)
        stats['pourcent_electricite'] = round(100 * sum(1 for s in surveys if s['electricity_access'] == 'Oui') / total, 1)
        stats['pourcent_internet'] = round(100 * sum(1 for s in surveys if s['internet_access'] == 'Oui') / total, 1)
    else:
        stats = {
            'moyenne_qualite': 0,
            'mediane_qualite': 0,
            'total': 0,
            'pourcent_eau': 0,
            'pourcent_electricite': 0,
            'pourcent_internet': 0
        }

    # Préparation des données pour les graphiques Chart.js
    # Distribution des notes de qualité d'école (1 à 5)
    distribution = {i: 0 for i in range(1, 6)}
    for s in surveys:
        distribution[s['school_quality']] += 1
    chart_labels = list(distribution.keys())
    chart_data = list(distribution.values())

    return render_template('dashboard.html',
                           stats=stats,
                           chart_labels=chart_labels,
                           chart_data=chart_data)

@app.route('/map')
def map_view():
    """Carte avec tous les points enquêtés."""
    conn = get_db()
    surveys = conn.execute('SELECT * FROM survey').fetchall()
    conn.close()
    # Convertir en liste de dictionnaires pour le template
    points = [dict(s) for s in surveys]
    return render_template('map.html', points=points)

if __name__ == '__main__':
    app.run(debug=True)
