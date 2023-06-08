CREATE TABLE types_serveurs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  type VARCHAR(100),
  description TEXT
);


CREATE TABLE serveurs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  type_serveur_id INT,
  nombre_processeur INT,
  capacite_memoire INT,
  capacite_stockage INT,
  FOREIGN KEY (type_serveur_id) REFERENCES types_serveurs(id)
);


CREATE TABLE utilisateurs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  prenom VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE services (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom_du_service VARCHAR(100),
  date_lancement DATE,
  espace_memoire_utilise INT,
  memoire_vive_necessaire INT,
  serveur_lancement_id INT,
  FOREIGN KEY (serveur_lancement_id) REFERENCES serveurs(id)
);

CREATE TABLE applications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  logo VARCHAR(100),
  serveurs VARCHAR(100),
  utilisateur_id INT,
  FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id)
);

CREATE TABLE Usage_ressources (
  id INT AUTO_INCREMENT PRIMARY KEY,
  application_id INT,
  service_id INT,
  FOREIGN KEY (application_id) REFERENCES Applications(id),
  FOREIGN KEY (service_id) REFERENCES Services(id)
);