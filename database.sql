USE sae;

CREATE TABLE administration_types_serveurs (
  id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  type VARCHAR(100) NOT NULL,
  description TEXT NULL DEFAULT NULL
);


CREATE TABLE administration_serveurs (
  id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  type_serveur_id BIGINT NOT NULL,
  nombre_processeur INT NOT NULL,
  capacite_memoire INT NOT NULL,
  capacite_stockage INT NOT NULL,
  FOREIGN KEY (type_serveur_id) REFERENCES administration_types_serveurs(id)
);


CREATE TABLE administration_utilisateurs (
  id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  prenom VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL
);

CREATE TABLE administration_services (
  id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  date_lancement DATE NOT NULL,
  espace_memoire_utilise BIGINT NOT NULL,
  memoire_vive_necessaire BIGINT NOT NULL,
  serveur_lancement_id BIGINT NOT NULL,
  FOREIGN KEY (serveur_lancement_id) REFERENCES administration_serveurs(id)
);

CREATE TABLE administration_applications (
  id BIGINT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  logo VARCHAR(100) NULL DEFAULT NULL,
  serveur_id BIGINT NOT NULL,
  utilisateur_id BIGINT NOT NULL,
  FOREIGN KEY (serveur_id) REFERENCES administration_serveurs(id),
  FOREIGN KEY (utilisateur_id) REFERENCES administration_utilisateurs(id)
);

CREATE TABLE administration_usage_ressources (
  id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  application_id BIGINT  NOT NULL,
  service_id BIGINT NOT NULL,
  FOREIGN KEY (application_id) REFERENCES administration_applications(id),
  FOREIGN KEY (service_id) REFERENCES administration_services(id)
);


INSERT INTO administration_utilisateurs (nom, prenom, email) VALUES ('admin', 'admin', 'admin@sae.com');
INSERT INTO administration_utilisateurs (nom, prenom, email) VALUES ('anonyme', 'anonyme', 'anonyme@sae.com');
INSERT INTO administration_types_serveurs (type, description) VALUES ('physique', 'Type de serveur physique');
INSERT INTO administration_types_serveurs (type, description) VALUES ('virtuel', 'Type de serveur virtuel');
INSERT INTO administration_services (nom, date_lancement, espace_memoire_utilise, memoire_vive_necessaire, serveur_lancement_id) VALUES
('Service de messagerie', '2023-06-01', 200, 500, 1),
('Service de stockage en ligne', '2023-05-15', 500, 1000, 2),
('Service de streaming vidéo', '2023-06-10', 800, 1500, 1),
('Service de sauvegarde automatique', '2023-06-05', 300, 700, 3);
INSERT INTO administration_serveurs (nom, type_serveur_id, nombre_processeur, capacite_memoire, capacite_stockage) VALUES
('Serveur 1', 1, 4, 8192, 500),
('Serveur 2', 2, 8, 16384, 1000),
('Serveur 3', 1, 6, 12288, 750),
('Serveur 4', 2, 16, 32768, 2000);