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


if __name__ == "__main__":
    print(calculer_portefeuille("AAPL:10|MSFT:5"))