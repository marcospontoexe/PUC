# criação das views
CREATE VIEW mydb.Vinicula_view AS
SELECT codVinicula, nomeVinicula FROM mydb.vinicula;

SELECT * FROM mydb.Vinicula_view;

SHOW CREATE VIEW mydb.Vinicula_view;


select mydb.vinho.nomeVinho AS `nomeVinho`,`mydb`.`vinho`.`anoVinho` AS `anoVinho`,`mydb`.`vinicula`.`nomeVinicula` AS `nomeVinicula`,`reg`.`nomeRegiao` AS `nomeRegiao` from ((`mydb`.`vinho` join `mydb`.`vinicula` on((`mydb`.`vinho`.`codVinho` = `mydb`.`vinicula`.`codVinicula`))) join `mydb`.`regiao` `reg` on((`mydb`.`vinicula`.`codVinicula` = `reg`.`codRegiao`)))

CREATE VIEW mydb.listavinhos AS 

select * from Cliente as c join Pedido as p	#juntando a instancia Cliente com a instância Pedido
on c.idCliente = p.CodCliente		#fazendo a conexão entre as duas instancias
join Item_Pedido as ip		#juntando a instancia Item_Pedido com a instância de conexão
on ip.CodPedido = p.idPedido		#fazendo a conexão entre as duas instancias




# criação de usuário e permissões
CREATE USER 'Somellier'@'localhost' IDENTIFIED BY '';

GRANT SELECT ON mydb.vinho TO 'Somellier'@'localhost';

GRANT SELECT ON mydb.vinicula_view TO 'Somellier'@'localhost';

ALTER USER 'Somellier'@'localhost' WITH MAX_QUERIES_PER_HOUR 3;
