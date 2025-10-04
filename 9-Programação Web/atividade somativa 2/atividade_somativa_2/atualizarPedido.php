<!DOCTYPE html>
<!-------------------------------------------------------------------------------
    Desenvolvimento Web
    PUCPR
    Profa. Cristina V. P. B. Souza
    Agosto/2022
---------------------------------------------------------------------------------->
<!-- MedAtualizar.php -->

<html>

<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">      <!--O site ocupará 100% da janela-->
        <meta name="keywords" content="cupcake">       <!-- palavras chaves usadas pelo navegador-->
        <meta name="description" content="página principal">    <!-- descrição da página, usada pelo navegador-->
        <link rel="stylesheet" href="estilo/style.css" type="text/css">     <!-- usa estilo externo -->
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="css/customize.css">
        <link rel="shortcut icon" href="imagem/Bakery.png" type="image/x-icon">     <!-- adiciona um favicon -->
        <title>Pedidos</title>
</head>

<body onload="w3_show_nav('menuMedico')">
	<!-- Inclui MENU.PHP  -->
	<?php require 'geral/menu.php'; ?>
	<?php require 'bd/conectaBD.php'; ?>
	<main>
		<!-- Conteúdo Principal: deslocado para direita em 270 pixels quando a sidebar é visível -->
		<div class="w3-main w3-container" >
			<div class="w3-panel  w3-card-4 w3-light-grey">
				<p class="w3-large">
					<div class="w3-code cssHigh notranslate">
						<!-- Acesso em:-->
						<?php
							date_default_timezone_set("America/Sao_Paulo");
							$data = date("d/m/Y H:i:s", time());
							echo "<p class='w3-small' > ";
							echo "Acesso em: ";
							echo $data;
							echo "</p> "
						?>

						<!-- Acesso ao BD-->
						<?php
							$id = $_GET['id']; // Obtém PK do Médico que será atualizado
							$IdItem = $_GET['id_item'];
							$IdCliente= $_GET['id_cliente'];

							// Cria conexão
							$conn = new mysqli($servername, $username, $password, $database);

							// Verifica conexão 
							if ($conn->connect_error) {
								die("<strong> Falha de conexão: </strong>" . $conn->connect_error);
							}

							// Faz Select na Base de Dados
							$sql = "select p.idPedidos, c.Nome, c.Preco, cl.Nome, cl.Celular 
							from Pedidos as p join Cardapio as c
							on c.idCardapio	 = p.ID_Cardapio
							join Clientes as cl		
							on cl.idCliente = p.ID_Clientes";

							//Inicio DIV form
							echo "<div class='w3-responsive w3-card-4'>";
							if ($result = $conn->query($sql)) {   // Consulta ao BD ok
								if ($result->num_rows == 1) {          // Retorna 1 registro que será atualizado  
									$row = $result->fetch_row();
									$Pedido = $row[0];				
									$Item   = $row[2];
									$Preco  = $row[3];
									
																	
									// Obtém cardápio na Base de Dados para um combo box
									$sqlG = "SELECT idCardapio, Nome FROM Cardapio";
									$result = $conn->query($sqlG);
									$optionsEspec = array();

									if ($result->num_rows > 0) {
										while ($row = $result->fetch_assoc()) {
											array_push($optionsEspec, "\t\t\t<option value='" . $row["idCardapio"] . "'>" . $row["Nome"] . "</option>\n");
										}
									} else {
										echo "Erro executando SELECT: " . $conn->connect_error;
									}

									// Obtém clientes na Base de Dados para um combo box
									$sqlCliente = "SELECT idCliente, Nome FROM Clientes";
									$resultCliente = $conn->query($sqlCliente);
									$optionsCliente = array();

									if ($resultCliente->num_rows > 0) {
										while ($rowCliente = $resultCliente->fetch_assoc()) {
											array_push($optionsCliente, "\t\t\t<option value='" . $rowCliente["idCliente"] . "'>" . $rowCliente["Nome"] . "</option>\n");
										}
									} else {
										echo "Erro executando SELECT: " . $conn->connect_error;
									}

						?>
						<div class="w3-container w3-theme">
							<h2>Altere os dados do pedido. = [<?php echo $Pedido; ?>]</h2>
						</div>
						<form class="w3-container" action="atualizarPedido_exe.php?Pedido=<?php echo $Pedido; ?>&id_item=<?php echo $IdItem; ?>&id_cliente=<?php echo $IdCliente; ?>" method="get" enctype="multipart/form-data">
							<table class='w3-table-all'>
								<tr>
									<td style="width:50%;">
										<p>
											<input type="hidden" id="Id" name="Id" value="<?php echo $Pedido; ?>">
										
										<p><label class="w3-text-IE"><b>Nome</b>*</label>
											<select name="Item" id="item" class="w3-input w3-border w3-light-grey " required>
											<?php
											foreach ($optionsCliente as $key => $value) {
												echo $value;
											}
											?>
											</select>
										</p>
										

										<p><label class="w3-text-IE"><b>Item</b>*</label>
											<select name="Item" id="item" class="w3-input w3-border w3-light-grey " required>
											<?php
											foreach ($optionsEspec as $key => $value) {
												echo $value;
											}
											?>
											</select>
										</p>

									</td>
								</tr>
								<tr>
									<td colspan="2" style="text-align:center">
									<p>
										<input type="submit" value="Alterar" class="w3-btn w3-red">
										<input type="button" value="Cancelar" class="w3-btn w3-theme" onclick="window.location.href='listarPedidos.php'">
									</p>
									</td>
								</tr>
							</table>
							<br>
						</form>
						<?php
							} else { ?>
								<div class="w3-container w3-theme">
									<h2>Médico inexistente</h2>
								</div>
							<br>
						<?php
								}
							} else {					
								echo "<p style='text-align:center'>Erro executando UPDATE: " . $conn->connect_error . "</p>";
							}
							echo "</div>"; //Fim form
							$conn->close(); //Encerra conexao com o BD
						?>
					</div>
				</p>
			</div>

		</div>
		<!-- Inclui RODAPE.PHP  -->
		<?php require 'geral/rodape.php'; ?>
	</main>

</body>

</html>