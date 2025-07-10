-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 02-Dez-2022 às 03:35
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `panificadora`
--

-- --------------------------------------------------------

-- Adiciona a tabela cliente
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Clientes` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Login` VARCHAR(45) NOT NULL,
  `Celular` VARCHAR(17) NOT NULL,
  `Senha` VARCHAR(40) NOT NULL,
  `Acesso` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idCliente`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Inserindo dados da tabela `cliente`
-- senha de administrador Abc@456
--
insert into Clientes values 
('1', 'Franciscão da Silva', 'francisco.silva', '(41) 99999-9898', '9e6d17674bd014ca519e37136d6c8a87', 'administrador'),
('2', 'Creuza Souza', 'creuza.souza', '(41) 99791-9898', '70b4269b412a8af42b1f7b0d26eceff2', 'cliente'),
('3', 'João de Deus', 'joao.deus', '(41) 99199-9100', '70b4269b412a8af42b1f7b0d26eceff2', 'cliente');


-- --------------------------------------------------------

-- Adiciona a tabela cardapio
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cardapio` (
  `idCardapio` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Descricao`  VARCHAR(45) NOT NULL,
  `Preco` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`idCardapio`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Inserindo dados da tabela `cardapio`
--
insert into Cardapio values 
('1', 'Delicinha de morango', 'Um delicioso sabor de morango estragado', '9.90'),
('2', 'Delicinha de abacaxi', 'Um delicioso sabor de abacaxi azedo', '9.90'),
('3', 'Algodão doce', 'Um delicioso sabor de algodão doce', '9.90'),
('4', 'Floresta negra', 'Um delicioso sabor de chocolate amargo', '12.90'),
('5', 'Delicinha de limão', 'Um delicioso sabor de limão', '12.90'),
('6', 'Limonada de morango', 'Um delicioso sabor de morango azedo', '12.90');


-- Adiciona a tabela pedidos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pedidos` (
  `idPedidos` INT NOT NULL AUTO_INCREMENT,
  ID_Clientes INT,
  ID_Cardapio INT,
  PRIMARY KEY (`idPedidos`),
  foreign key (ID_Clientes) references Clientes(idCliente),
	foreign key (ID_Cardapio) references Cardapio(idCardapio)		
)ENGINE=InnoDB DEFAULT CHARSET=latin1;




