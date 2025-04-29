CREATE VIEW mydb.listaVinhos AS
select nomeVinho, anoVinho, nomeVinicula, nomeRegiao from mydb.vinho as vinho join mydb.vinicula as vinicula	#juntando a instancia vinho com a instância venicula
on vinho.codVinho = vinicula.codVinicula		#fazendo a conexão entre as duas instancias
join mydb.regiao as reg		#juntando a instancia Item_Pedido com a instância de conexão
on vinicula.codVinicula = reg.codRegiao;		#fazendo a conexão entre as duas instancias

select * from mydb.listaVinhos

drop view mydb.listaVinhos