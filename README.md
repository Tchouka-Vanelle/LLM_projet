# 🤖 Agent Financier IA

Projet réalisé dans le cadre du TP LangChain – EPITA

---

# 📌 Description

Cet agent intelligent permet de répondre à des questions financières en langage naturel.

Fonctionnalités :

* 📊 Analyse de portefeuille
* 💰 Calculs financiers
* 🧠 Mémoire conversationnelle
* 🗄️ Interrogation base PostgreSQL
* 🌐 API REST (FastAPI)
* 🖥️ Interface web (Streamlit)

---

# 🧱 Architecture

* LangChain → Agent intelligent
* OpenAI → LLM (gpt-4o-mini)
* PostgreSQL (Docker) → Base de données
* FastAPI → API REST
* Streamlit → Interface utilisateur

---

# 🚀 Installation

## 1. Cloner le projet

```bash
git clone <repo_url>
cd TP_PROJET
```

## 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# 🐳 Base de données PostgreSQL (Docker)

## Démarrer le conteneur

```bash
docker start pgvector_db
```

## Vérifier

```bash
docker ps
```

## Connexion à la base

```bash
psql -h localhost -p 5433 -U postgres -d vectordb
```
## 🗄️ Initialisation de la base

Si la base est vide, exécuter :

```bash
psql -h localhost -p 5433 -U postgres -d vectordb -f init_db.sql
```

---

# 🖥️ Interface Web (C1 + C2)

## Lancer Streamlit

```bash
streamlit run app.py
```

## Accéder dans le navigateur

👉 http://localhost:8501

---

## 🎯 Ce que ça permet

* Poser des questions à l’agent
* Voir l’historique des échanges
* Utiliser la mémoire conversationnelle

---

## 🧠 Mémoire conversationnelle (C2)

L’agent utilise `ConversationBufferMemory`.

### Exemple à tester dans Streamlit :

1. Donne-moi les infos du client Sophie Bernard
2. Quel produit lui recommandes-tu ?
3. Calcule le prix TTC et dis-moi si elle peut se le permettre

👉 L’agent se souvient :

* du client (VIP)
* du produit recommandé
* du solde

---

# 🤖 Mode Terminal (optionnel)

```bash
python main.py
```

---

# 🌐 API REST (D1)

## Lancer l’API

```bash
uvicorn api:app --reload
```

## Accéder à la documentation Swagger

👉 http://127.0.0.1:8000/docs

---

## 📩 Endpoint principal

### POST `/api/agent/query`

### Exemple de requête

```json
{
  "question": "Quels sont mes actifs les plus risqués ?"
}
```

---

## 📊 Exemple de réponse

```json
{
  "question": "Quels sont mes actifs les plus risqués ?",
  "response": "Analyse du portefeuille..."
}
```

---

# 📊 Analyse de portefeuille (D1)

L’agent peut :

* Récupérer les positions depuis PostgreSQL
* Calculer la valeur du portefeuille
* Analyser les variations
* Identifier les actifs les plus risqués

---

# 🧪 Exemples de questions à tester

## Base de données

* Donne-moi les infos du client Sophie Bernard

## Finance

* Donne-moi le cours de AAPL

## Calculs

* Calcule la TVA sur 100€ avec 20%

## Portefeuille

* Quel est mon portefeuille ?
* Quels sont mes actifs ?
* Quels sont mes actifs les plus risqués ?

---

# 📁 Structure du projet

```
TP_PROJET/
│── agent.py
│── main.py
│── api.py
│── app.py
│── tools/
│   ├── database.py
│   ├── portefeuille.py
│   ├── finance.py
│   └── ...
│── venv/
```

---

# ⚠️ Configuration

Créer un fichier `.env` :

```env
OPENAI_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

# ✅ Conclusion

Ce projet implémente :

* ✔️ Agent LangChain avec outils
* ✔️ PythonREPLTool
* ✔️ Mémoire conversationnelle
* ✔️ Interface Streamlit
* ✔️ API REST
* ✔️ PostgreSQL (Docker)
* ✔️ Analyse financière avancée

---

# 👨‍💻 Auteur

Projet réalisé par : Vanelle TCHOUKA
