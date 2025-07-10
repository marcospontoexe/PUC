<!DOCTYPE html>
<!-------------------------------------------------------------------------------
    Desenvolvimento Web
    PUCPR
    Profa. Cristina V. P. B. Souza
    Agosto/2022
---------------------------------------------------------------------------------->
<!-- medIncluir_exe.php -->

<html>
<head>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">      <!--O site ocupará 100% da janela-->
        <meta name="keywords" content="cupcake">       <!-- palavras chaves usadas pelo navegador-->
        <meta name="description" content="página principal">    <!-- descrição da página, usada pelo navegador-->
        <link rel="stylesheet" href="estilo/style.css" type="text/css">     <!-- usa estilo externo -->
        <link rel="shortcut icon" href="imagem/Bakery.png" type="image/x-icon">     <!-- adiciona um favicon -->
        <title>faça seu pedido</title>
</head>

<body>
	<?php 
        session_start(); // informa ao PHP que iremos trabalhar com sessão
        require 'bd/conectaBD.php'; 
       // require 'geral/menuCliente.php';
    ?>
	<main>
		<!-- Acesso ao BD-->
		<?php
			$id_cliente = $_SESSION ['idCliente'];
			$pedido   = $_POST['Pedido'];
						
			// Cria conexão
			$conn = new mysqli($servername, $username, $password, $database);
			// Verifica conexão
			if ($conn->connect_error) {
				die("<strong> Falha de conexão: </strong>" . $conn->connect_error);
			}      
			
			// Faz Select na Base de Dados   
			$sql = "insert into Pedidos (ID_Clientes, ID_Cardapio) values ('$id_cliente', '$pedido')";
			if ($result = $conn->query($sql)) {
				echo '<h2 class="titleBottom">Pedido realizado!</h2>';
			} 	

			$conn->close();  //Encerra conexao com o BD
		?>
		
	</main>

	<?php require 'geral/rodape.php'; ?>
</body>

</html>