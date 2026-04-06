import random, datetime
import yfinance as yf

import warnings
import logging

# empêcher affichage erreurs API
warnings.filterwarnings("ignore")
logging.getLogger("yfinance").setLevel(logging.CRITICAL)
 
def obtenir_cours_action(symbole: str) -> str:
    """
    🎯 BUT :
    Retourner prix + variation réelle d'une action

    WHY:
    - history() = fiable
    - permet calcul variation

    HOW:
    - on prend 2 jours
    - on calcule variation %
    """

    symbole = symbole.strip().upper()

    try:
        stock = yf.Ticker(symbole)

        # récupération données marché
        data = stock.history(period="2d")

        if data.empty or len(data) < 2:
            return f"Action '{symbole}' non trouvée."

        # prix réel (Close = prix de clôture)
        prix_actuel = data["Close"].iloc[-1]
        prix_precedent = data["Close"].iloc[-2]

        # variation officielle
        variation_pct = ((prix_actuel - prix_precedent) / prix_precedent) * 100

        tendance = "📈" if variation_pct >= 0 else "📉"

        return f"{symbole} {tendance} : {prix_actuel:.2f} $ ({variation_pct:+.2f}%)"

    except Exception as e:
        return f"Erreur action {symbole} : {str(e)}"

    
def obtenir_cours_crypto(symbole: str) -> str:

    symbole = symbole.strip().upper()
    ticker = f"{symbole}-USD"

    try:
        crypto = yf.Ticker(ticker)

        data = crypto.history(period="2d")

        if data.empty or len(data) < 2:
            return f"Crypto '{symbole}' non trouvée."

        prix_actuel = data["Close"].iloc[-1]
        prix_precedent = data["Close"].iloc[-2]

        variation_pct = ((prix_actuel - prix_precedent) / prix_precedent) * 100

        tendance = "📈" if variation_pct >= 0 else "📉"

        return f"{symbole} {tendance} : {prix_actuel:.2f} $ ({variation_pct:+.2f}%)"

    except Exception as e:
        return f"Erreur crypto {symbole} : {str(e)}"

if __name__ == "__main__":
    print("==== TEST ACTION =====")
    print(obtenir_cours_action("TSLA"))
    print(obtenir_cours_action("inconnu"))

    print("\n==== TEST CRYPTO =====")
    print(obtenir_cours_crypto("BTC"))
    print(obtenir_cours_crypto("ETH"))
    print(obtenir_cours_crypto("XXX"))
    