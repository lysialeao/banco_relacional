CREATE DATABASE IF NOT EXISTS gso;
USE gso;

CREATE TABLE IF NOT EXISTS Pessoa(
    id_pessoa INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NULL
);