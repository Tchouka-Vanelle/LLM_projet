import psycopg2

#python tools/database.py
def get_connection():
    return psycopg2.connect(
        dbname="vectordb",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5433"   
    )


def rechercher_client(query: str) -> str:
    """Recherche un client par nom ou par identifiant."""
    query = query.strip()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nom, solde_compte, type_compte
        FROM clients
        WHERE id = %s OR nom ILIKE %s
    """, (query.upper(), f"%{query}%"))

    result = cursor.fetchone()
    conn.close()

    if not result:
        return f"Aucun client trouvé pour : '{query}'"

    nom, solde, type_compte = result

    return f"Client : {nom} | Solde : {solde:.2f} € | Type de compte : {type_compte}"


def rechercher_produit(query: str) -> str:
    """Recherche un produit par nom ou identifiant. Retourne prix HT, TVA, prix TTC, stock."""
    query = query.strip()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nom, prix_ht, stock
        FROM produits
        WHERE id = %s OR nom ILIKE %s
    """, (query.upper(), f"%{query}%"))

    result = cursor.fetchone()
    conn.close()

    if not result:
        return f"Aucun produit trouvé pour : '{query}'"

    nom, prix_ht, stock = result

    tva = prix_ht * 0.20
    prix_ttc = prix_ht + tva

    return (f"Produit : {nom} | Prix HT : {prix_ht:.2f} € "
            f"| TVA : {tva:.2f} € | Prix TTC : {prix_ttc:.2f} € | Stock : {stock}")


def lister_tous_les_clients() -> str:
    """Retourne la liste complète de tous les clients."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nom, solde_compte, type_compte
        FROM clients
    """)

    results = cursor.fetchall()
    conn.close()

    if not results:
        return "Aucun client en base."

    result = "Liste des clients :\n"

    for cid, nom, solde, type_compte in results:
        result += f"  {cid} : {nom} | {type_compte} | Solde : {solde:.2f} €\n"

    return result


if __name__ == "__main__":
    print("==== tester recherche client =====")
    print(rechercher_client("Marie Dupont"))
    print(rechercher_client("c002"))
    print(rechercher_client("yyy"))
    
    print("==== tester recherche produit =====")
    print(rechercher_produit("p001"))
    print(rechercher_produit("Souris"))
    print(rechercher_produit("inconnu"))
    
    print("==== Lister clients =====")
    print(lister_tous_les_clients())
