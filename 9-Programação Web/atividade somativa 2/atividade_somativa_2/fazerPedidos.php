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
        <link rel="shortcut icon" href="imagem/Bakery.png" type="image/x-icon">     <!-- adiciona um favicon -->
        <title>faça seu pedido</title>
</head>

<body>
    
    <!-- Inclui MENU.PHP  -->
    <?php 
        require 'bd/conectaBD.php'; 
        require 'geral/menuCliente.php';
    ?>
           
    <main> 
        <?php
            // Cria conexão
            $conn = new mysqli($servername, $username, $password, $database);

            // Verifica conexão 
            if ($conn->connect_error) {
                die("<strong> Falha de conexão: </strong>" . $conn->connect_error);
            }

            // Obtém nome dos produtos do cardapio na Base de Dados para um combo box
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
                                                            
            $conn->close();
        ?>
        <!-- Acesso em:-->
        <?php

        date_default_timezone_set("America/Sao_Paulo");
        $data = date("d/m/Y H:i:s", time());
        echo "<p class='w3-small' > ";
        echo "Acesso em: ";
        echo $data;
        echo "</p> "
        ?>

        <h2 class="titleBottom">faça seu pedido</h2>
        
        <h2 class="titleBottom">Escolha seu bolinho</h2>
        <section class="content">
            <form class="w3-container" action="incluirPedido.php" method="post" enctype="multipart/form-data">
                <label for="iPedido"><b>CupCake</b>*</label>
                <select name="Pedido" id="iPedido" required>
                    <option value=""></option>
                    <?php
                    foreach ($optionsEspec as $key => $value) {
                        echo $value;
                    }
                    ?>
                </select>
                <div class="form-group form-button">
                    <input type="submit" class="form-submit" value="Finalizar">
                </div>
            </form>
            
        </section>

        
                     
    </main>
    <?php require 'geral/rodape.php'; ?>
</body>

</html>