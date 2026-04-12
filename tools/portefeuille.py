"""
🎯 BUT :
Calculer la valeur d’un portefeuille boursier en temps réel

WHY:
- utiliser des données réelles (yfinance)
- montrer la capacité de l’agent à faire des calculs financiers

HOW:
- parser une string "AAPL:10|MSFT:5"
- récupérer les prix via yfinance
- calculer valeur ligne + total
- calculer variation %
"""

import yfinance as yf
#python tools/portefeuille.py

def calculer_portefeuille(input_str: str) -> str:
    """
    Entrée : "AAPL:10|MSFT:5"
    """

    try:
        positions = input_str.strip().split("|")

        total = 0
        variation_totale = 0
        result = "📊 Portefeuille :\n\n"

        for position in positions:
            symbole, quantite = position.split(":")
            symbole = symbole.strip().upper()
            quantite = float(quantite)

            stock = yf.Ticker(symbole)
            data = stock.history(period="2d")

            if data.empty or len(data) < 2:
                result += f"{symbole} non trouvé\n"
                continue

            prix_actuel = data["Close"].iloc[-1]
            prix_precedent = data["Close"].iloc[-2]

            # WHY : formule officielle variation %
            variation_pct = ((prix_actuel - prix_precedent) / prix_precedent) * 100

            valeur = prix_actuel * quantite

            total += valeur
            variation_totale += variation_pct * valeur  # pondération

            tendance = "📈" if variation_pct >= 0 else "📉"

            result += (
                f"{symbole} {tendance}\n"
                f"  Prix : {prix_actuel:.2f}$\n"
                f"  Quantité : {quantite}\n"
                f"  Valeur : {valeur:.2f}$\n"
                f"  Variation : {variation_pct:+.2f}%\n\n"
            )

        # moyenne pondérée
        variation_globale = variation_totale / total if total > 0 else 0

        result += "----------------------\n"
        result += f"💰 Total : {total:.2f}$\n"
        result += f"📊 Variation globale : {variation_globale:+.2f}%"

        return result

    except Exception as e:
        return f"Erreur portefeuille : {str(e)}"

from database import get_connection


def get_positions(_input: str = "") -> str:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT symbole, quantite FROM positions")
    results = cursor.fetchall()

    conn.close()

    if not results:
        return "Aucune position en base."

    res = "Portefeuille en base :\n"
    for symbole, quantite in results:
        res += f"{symbole}:{quantite}\n"

    return res

def analyser_portefeuille(_input: str = "") -> str:
    """
    Analyse le portefeuille depuis la base :
    - récupère positions
    - récupère prix via yfinance
    - calcule variation
    - classe les risques
    """

    import yfinance as yf
    from database import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT symbole, quantite FROM positions")
    positions = cursor.fetchall()
    conn.close()

    if not positions:
        return "Aucune position en base."

    result = "Analyse du portefeuille :\n\n"

    risques = []

    for symbole, quantite in positions:
        stock = yf.Ticker(symbole)
        data = stock.history(period="2d")

        if data.empty or len(data) < 2:
            continue

        prix_actuel = data["Close"].iloc[-1]
        prix_precedent = data["Close"].iloc[-2]

        variation = ((prix_actuel - prix_precedent) / prix_precedent) * 100

        # classification du risque
        if abs(variation) > 1:
            risque = "🔴 élevé"
        elif abs(variation) > 0.5:
            risque = "🟠 moyen"
        else:
            risque = "🟢 faible"

        risques.append((symbole, variation, risque))

        result += f"{symbole} → {variation:+.2f}% → risque {risque}\n"

    # trouver le plus risqué
    plus_risque = max(risques, key=lambda x: abs(x[1]))

    result += "\n----------------------\n"
    result += f"⚠️ Actif le plus risqué : {plus_risque[0]} ({plus_risque[1]:+.2f}%)"

    return result

if __name__ == "__main__":
    print(calculer_portefeuille("AAPL:10|MSFT:5"))
    print(get_positions())
    print(analyser_portefeuille())