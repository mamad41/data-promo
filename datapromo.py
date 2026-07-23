from donnees_promo import PROMOTION

# 1. Définition des fonctions 🛠️

def calculer_moyenne(notes):
    if len(notes) > 0:
        return sum(notes) / len(notes)
    else:
        return None

def calculer_moyenne_promo(liste_moyennes):
    if len(liste_moyennes) > 0:
        return sum(liste_moyennes) / len(liste_moyennes)
    else:
        return None

def definir_statut(moyenne):
    if moyenne is None:
        return "À contacter (aucune note)"
    elif moyenne < 10:
        return "Accompagnement prioritaire"
    else:
        return "Rien à signaler"


# 2. Nettoyage et calcul des moyennes individuelles 🧹

promo_clean = []

for apprenant in PROMOTION:
    apprenant_propre = {
        "prenom": apprenant["prenom"].strip().capitalize(),
        "ville": apprenant["ville"].strip().capitalize(),
        "age": apprenant["age"],
        "notes": apprenant["notes"],
        "moyenne": calculer_moyenne(apprenant["notes"])
    }
    promo_clean.append(apprenant_propre)


# 3. Calcul de la moyenne générale 📊

moyennes_valides = [apprenant["moyenne"] for apprenant in promo_clean if apprenant["moyenne"] is not None]
moyenne_promo = calculer_moyenne_promo(moyennes_valides)

print(f"La moyenne générale de la promo est de {moyenne_promo:.2f} / 20\n")


# 4. Identification des étudiants à accompagner 🎯

accompagnes_prioritaires = []

for apprenant in promo_clean:
    statut = definir_statut(apprenant["moyenne"])
    if statut != "Rien à signaler":
        accompagnes_prioritaires.append({
            "prenom": apprenant["prenom"],
            "statut": statut
        })


# 5. Affichage de la liste prioritaire 📋

print("=== ÉTUDIANTS À ACCOMPAGNER EN PRIORITÉ ===")

# La boucle 'for' permet de regarder chaque 'eleve' de la liste un par un
for eleve in accompagnes_prioritaires:
    if eleve["statut"] == "À contacter (aucune note)":
        print(f"- {eleve['prenom']} : {eleve['statut']}")
    else:
        print(f"- {eleve['prenom']} : {eleve['statut']}")