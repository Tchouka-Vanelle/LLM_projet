-- ============================================
-- 🗄️ INIT DB - PROJET LANGCHAIN
-- ============================================

-- ===============================
-- 👤 TABLE CLIENTS
-- ===============================
CREATE TABLE IF NOT EXISTS clients (
    id VARCHAR(10) PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    solde_compte FLOAT NOT NULL,
    type_compte VARCHAR(20) NOT NULL
);

INSERT INTO clients (id, nom, solde_compte, type_compte) VALUES
('C001', 'Marie Dupont', 12500, 'Standard'),
('C002', 'Jean Martin', 18500, 'Premium'),
('C003', 'Sophie Bernard', 28900, 'VIP')
ON CONFLICT (id) DO NOTHING;


-- ===============================
-- 🛍️ TABLE PRODUITS
-- ===============================
CREATE TABLE IF NOT EXISTS produits (
    id VARCHAR(10) PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prix_ht FLOAT NOT NULL,
    stock INT NOT NULL
);

INSERT INTO produits (id, nom, prix_ht, stock) VALUES
('P001', 'Ordinateur portable', 1000, 15),
('P002', 'Chaise ergonomique', 280, 20),
('P003', 'Casque audio', 129, 30),
('P004', 'Souris ergonomique', 49.9, 50)
ON CONFLICT (id) DO NOTHING;


-- ===============================
-- 📊 TABLE POSITIONS (D1)
-- ===============================
CREATE TABLE IF NOT EXISTS positions (
    id SERIAL PRIMARY KEY,
    symbole VARCHAR(10) NOT NULL,
    quantite FLOAT NOT NULL
);

INSERT INTO positions (symbole, quantite) VALUES
('AAPL', 10),
('MSFT', 5),
('TSLA', 2)
ON CONFLICT DO NOTHING;
