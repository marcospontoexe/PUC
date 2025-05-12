# criação das views
CREATE VIEW mydb.Vinicula_view AS
SELECT codVinicula, nomeVinicula FROM mydb.vinicula;

SELECT * FROM mydb.Vinicula_view;

CREATE VIEW mydb.listavinhos AS 
select vinho.nomeVinho, vinho.anoVinho, vinicula.nomeVinicula, reg.nomeRegiao from mydb.vinho as vinho join mydb.vinicula as vinicula	#juntando a instancia vinho com a instância vinicula
on vinho.codVinho = vinicula.codVinicula		#fazendo a conexão entre as duas instancias
join mydb.regiao as reg		#juntando a instancia vinicula com a instância regiao
on reg.codRegiao = vinicula.codVinicula;		#fazendo a conexão entre as duas instancias

SELECT * FROM mydb.listavinhos;


# criação de usuário e permissões
CREATE USER 'Somellier'@'localhost' IDENTIFIED BY '';

GRANT SELECT ON mydb.vinho TO 'Somellier'@'localhost';

GRANT SELECT ON mydb.vinicula_view TO 'Somellier'@'localhost';

ALTER USER 'Somellier'@'localhost' WITH MAX_QUERIES_PER_HOUR 40;
