# -*- coding: utf-8 -*-
"""
DataPromo — Jeu de données du brief
------------------------------------
Ce fichier contient les données BRUTES de la promotion, telles qu'elles ont
été saisies à la main au fil des inscriptions. Elles sont volontairement
« sales » : espaces en trop, casse incohérente pour les villes, et quelques
informations manquantes (note absente, âge manquant).

Votre travail consiste à NETTOYER ces données puis à en tirer des indicateurs.
Ne modifiez pas ce fichier : importez-le dans votre script.

    from donnees_promo import PROMOTION

Chaque apprenant est un dictionnaire :
    - "prenom" : chaîne de caractères (parfois avec des espaces superflus)
    - "ville"  : chaîne de caractères (casse incohérente)
    - "age"    : entier, ou None si l'information manque
    - "notes"  : liste de notes sur 20 (parfois vide ou incomplète)
"""

PROMOTION = [
    {"prenom": "  aya",        "ville": "MARSEILLE", "age": 22,   "notes": [14, 12, 16]},
    {"prenom": "Yanis ",       "ville": "marseille", "age": 19,   "notes": [8, 11, 9]},
    {"prenom": "  LÉA  ",      "ville": "Aix",       "age": 25,   "notes": [17, 15, 18]},
    {"prenom": "mohamed",       "ville": "Marseille ", "age": None, "notes": [10, 9, 12]},
    {"prenom": "Chloé",         "ville": "AIX",       "age": 20,   "notes": [13, 14]},        # une note manquante
    {"prenom": " Tom",          "ville": "aubagne",   "age": 23,   "notes": [6, 8, 7]},
    {"prenom": "Ines ",         "ville": "Aix ",      "age": 21,   "notes": [15, 16, 14]},
    {"prenom": "  KEVIN",       "ville": "MARSEILLE", "age": 28,   "notes": []},              # aucune note saisie
    {"prenom": "sarah",         "ville": "Aubagne",   "age": 24,   "notes": [11, 13, 10]},
    {"prenom": "Lucas  ",       "ville": "aix",       "age": 18,   "notes": [9, 7, 8]},
    {"prenom": "Nadia",         "ville": "marseille ", "age": 26,  "notes": [18, 17, 19]},
    {"prenom": "  hugo ",       "ville": "Aubagne",   "age": None, "notes": [12, 12, 13]},
]
