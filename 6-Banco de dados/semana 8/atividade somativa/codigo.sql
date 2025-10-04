#Aluno: Marcos Daniel Santana
#Grupo: 45

-- -----------------------------------------------------
-- Criando o banco de dados
-- -----------------------------------------------------
CREATE SCHEMA `mydb`  #cria um banco de dados com constraitns.
DEFAULT CHARACTER SET utf8  #codificação de caracteres (utf8 possui acentos)
default collate utf8_general_ci;  # definindo um collation

-- -----------------------------------------------------
-- Criando oas tabelas
-- -----------------------------------------------------
use mydb;				#Abre o banco de dados

-- -----------------------------------------------------
-- Table `mydb`.`Regiao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Regiao` (
  `codRegiao` BIGINT(0) NOT NULL AUTO_INCREMENT,
  `nomeRegiao` VARCHAR(100) NOT NULL,
  `descricaoRegiao` TEXT(0) NULL,
  PRIMARY KEY (`codRegiao`)
)
ENGINE = InnoDB
default charset = utf8;

-- -----------------------------------------------------
-- Table `mydb`.`Vinicula`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Vinicula` (
  `codVinicula` BIGINT(0) NOT NULL AUTO_INCREMENT,
  `nomeVinicula` VARCHAR(100) NULL,
  `descricaoVinicula` TEXT(0) NULL,
  `foneVinicula` VARCHAR(15) NULL,
  `emailVinicula` VARCHAR(15) NULL,
  `codRegiao` BIGINT(0) NOT NULL,
  PRIMARY KEY (`codVinicula`),
  INDEX `fk_Vinicula_Regiao1_idx` (`codRegiao` ASC) VISIBLE,
  CONSTRAINT `fk_Vinicula_Regiao1`
    FOREIGN KEY (`codRegiao`)
    REFERENCES `mydb`.`Regiao` (`codRegiao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
default charset = utf8;

-- -----------------------------------------------------
-- Table `mydb`.`Vinho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Vinho` (
  `codVinho` BIGINT(0) NOT NULL AUTO_INCREMENT,
  `nomeVinho` VARCHAR(50) NOT NULL,
  `tipoVinho` VARCHAR(30) NOT NULL,
  `anoVinho` INT NOT NULL,
  `descricaoVinho` TEXT(0) NULL,
  `codVinicula` BIGINT(0) NOT NULL,
  PRIMARY KEY (`codVinho`),
  INDEX `fk_Vinho_Vinicula_idx` (`codVinicula` ASC) VISIBLE,
  CONSTRAINT `fk_Vinho_Vinicula`
    FOREIGN KEY (`codVinicula`)
    REFERENCES `mydb`.`Vinicula` (`codVinicula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
default charset = utf8;

-- -----------------------------------------------------
-- Inserindo dados nas tabelas
-- -----------------------------------------------------
use mydb;	

insert into mydb.regiao values 
(default,'Campo Largo - PR', 'Região sul do brasil'),
(default, 'Curitiba - PR', 'Região sul do brasil'),
(default, 'Araucária - PR', 'Região sul do brasil'),
(default, 'Quitandinha - PR', 'Região sul do brasil'),
(default, 'Mandirituba - PR', 'Região sul do brasil');

insert into mydb.vinicula values
(default, 'Da casa', 'vinícula regional ', '3396-5588', 'dacasa', '1'),
(default, 'Dubom', 'vinícula colonial', '99985-568', 'vinho', '2'),
(default, 'do gole', 'vinicula fodona', '95623-9874', 'gole', '3'),
(default, 'sabor da uva', 'vinícula ', '99888-8888', 'boa', '4'),
(default, 'GOLE ETERNO', 'vinícula ', '98475-8877', 'BOA', '5');

insert into  mydb.vinho values
(default, 'campo largo', 'tinto suave', '2025', 'ruim', '1'),
(default, 'puro sangue', 'tinto suave', '2024', 'ruim', '1'),
(default, 'del rei', 'tinto seco rose', '2022', 'da pra tomar', '2'),
(default, 'del rei', 'branco seco', '2023', 'da pra tomar', '2'),
(default, 'Colonial', 'tinto seco', '2025', 'cooler de vinho', '3'),
(default, 'do avô', 'tinto suave', '2025', 'cooler de vinho', '5');

-- -----------------------------------------------------
-- Consutando dados nas tabelas
-- -----------------------------------------------------
SELECT * FROM mydb.regiao;
SELECT * FROM mydb.vinicula;
SELECT * FROM mydb.vinho;

-- -----------------------------------------------------
-- Criando Views
-- -----------------------------------------------------
#Faça uma consulta que liste o nome e ano dos  vinhos, incluindo o nome da vinícula e o nome da região que ela pertence:
CREATE VIEW mydb.listavinhos AS 
select vinho.nomeVinho, vinho.anoVinho, vinicula.nomeVinicula, reg.nomeRegiao from mydb.vinho as vinho join mydb.vinicula as vinicula	#juntando a instancia vinho com a instância vinicula
on vinho.codVinho = vinicula.codVinicula		#fazendo a conexão entre as duas instancias
join mydb.regiao as reg		#juntando a instancia vinicula com a instância regiao
on reg.codRegiao = vinicula.codVinicula;		#fazendo a conexão entre as duas instancias

SELECT * FROM mydb.listavinhos;

# Usuário Somelier deve ter acesso pelo localhost ao Select do campo codVinicula e nomeVinicula da tabela Vinicula
CREATE VIEW mydb.Vinicula_view AS
SELECT codVinicula, nomeVinicula FROM mydb.vinicula;

SELECT * FROM mydb.Vinicula_view;

-- -----------------------------------------------------
-- Criação de usuários e permissões
-- -----------------------------------------------------
#Crie um usuário Somellier:
CREATE USER 'Somellier'@'localhost' IDENTIFIED BY '';

# Somellier deve ter acesso pelo localhost ao Select da tabela Vinho:
GRANT SELECT ON mydb.vinho TO 'Somellier'@'localhost';	

#Somellier deve ter acesso pelo localhost ao Select do campo codVinicula e nomeVinicula da tabela Vinicula.
GRANT SELECT ON mydb.vinicula_view TO 'Somellier'@'localhost';	# acesso pelo localhost ao Select da tabela Vinho e ao Select do campo codVinicula e nomeVinicula da tabela Vinicula

# Somellier pode realizar 40 consultas por hora
ALTER USER 'Somellier'@'localhost' WITH MAX_QUERIES_PER_HOUR 40;

