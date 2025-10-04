<!DOCTYPE html>
<!-------------------------------------------------------------------------------
    Desenvolvimento Web
    PUCPR
    Profa. Cristina V. P. B. Souza
    Agosto/2022
---------------------------------------------------------------------------------->
<!-- medListar.php -->

<html>

<head>
    <meta charset="UTF-8">          <!-- configurção de meta-dados, configuração de padrão de caracteres usados-->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">      <!--O site ocupará 100% da janela-->
        <meta name="keywords" content="cupcake">       <!-- palavras chaves usadas pelo navegador-->
        <meta name="description" content="página principal">    <!-- descrição da página, usada pelo navegador-->
        <link rel="stylesheet" href="estilo/style.css" type="text/css">     <!-- usa estilo externo -->
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="css/customize.css">
        <link rel="shortcut icon" href="imagem/Bakery.png" type="image/x-icon">     <!-- adiciona um favicon -->
        <title>Listagem de pedidos</title>
</head>

<body>
    <!-- Inclui MENU.PHP  -->
    <?php require 'bd/conectaBD.php'; ?>
    <?php require 'geral/menu.php';   ?>

    <main>
        <div class="w3-main w3-container">
            <div class="w3-panel w3-padding-large w3-card-4 w3-light-grey">
                <p class="w3-large">
                <p>
                <div class="w3-code cssHigh notranslate">

                    <!-- Acesso em:-->
                    <?php

                        date_default_timezone_set("America/Sao_Paulo");
                        $data = date("d/m/Y H:i:s", time());
                        echo "<p> ";
                        echo "Acesso em: ";
                        echo $data;
                        echo "</p> "
                        ?>
                    
                        <div class="w3-container w3-theme">
                            <h2>Listagem de Pedidos</h2>
                        </div>
                        <!-- Acesso ao BD-->
                        <?php
                        // Cria conexão
                        $conn = new mysqli($servername, $username, $password, $database);

                        // Verifica conexão 
                        if ($conn->connect_error) {
                            die("<strong> Falha de conexão: </strong>" . $conn->connect_error);
                        }

                        // Faz Select na Base de Dados
                        $sql = "select p.idPedidos, c.idCardapio, c.Nome, c.Preco, cl.idCliente, cl.Nome, cl.Celular 
                        from Pedidos as p join Cardapio as c
                        on c.idCardapio	 = p.ID_Cardapio
                        join Clientes as cl		
                        on cl.idCliente = p.ID_Clientes";
                        $result = $conn->query($sql);
                        
                        echo "<div class='w3-responsive w3-card-4'>";
                        if ($result->num_rows >0) {
                            echo "<table class='w3-table-all'>";
                            echo "	<tr>";           
                            echo "	  <th width='7%'>Pedido</th>";
                            echo "	  <th width='18%'>Item</th>";
                            echo "	  <th width='7%'>Preço</th>";
                            echo "	  <th width='18%'>Cliente</th>";
                            echo "	  <th width='15%'>Celular</th>";           
                            echo "	  <th width='7%'> </th>";
                            echo "	  <th width='7%'> </th>";
                            echo "	</tr>";
                            // Apresenta cada linha da tabela
                            while ($row = $result->fetch_row()) {
                                
                                $item = $row[0];
                                echo "<tr>";
                                echo "<td>";
                                echo $item;
                                echo "</td><td>";
                                echo $row[2];
                                echo "</td><td>";
                                echo $row[3];
                                echo "</td><td>";
                                echo $row[5];
                                echo "</td><td>";
                                echo $row[6];
                                echo "</td>";
                                //Atualizar e Excluir registro de médicos
                                    ?>
                                    <td>
                                        <a href='atualizarPedido.php?id=<?php echo $item; ?>&id_item=<?php echo $row[1]; ?>&id_cliente=<?php echo $row[4]; ?>'><img src='imagens/Edit.png' title='Editar Médico' width='32'></a>
                                    </td>
                                    <td>
                                        <a href='excluirPedido.php?id=<?php echo $item; ?>'><img src='imagens/Delete.png' title='Excluir Médico' width='32'></a>
                                    </td>
                                    </tr>
                            <?php
                            }
                            echo "</table>";
                            echo "</div>";
                        } else {
                            echo "<p style='text-align:center'>Erro executando SELECT: " . $conn->connect_error . "</p>";
                        }
                        $conn->close();
                    ?>
                </div>
            </div>
            
        </div>
    </main>
    <?php require 'geral/rodape.php'; ?>
</body>

</html>