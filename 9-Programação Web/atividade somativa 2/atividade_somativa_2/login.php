<html>
    <!-------------------------------------------------------------------------------
    Desenvolvimento Web
    PUCPR
    Profa. Cristina V. P. B. Souza
    Agosto/2022
---------------------------------------------------------------------------------->
<!-- Login.php --> 
	<head>
        <meta charset="UTF-8">          <!-- configurção de meta-dados, configuração de padrão de caracteres usados-->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">      <!--O site ocupará 100% da janela-->
        <meta name="keywords" content="cupcake">       <!-- palavras chaves usadas pelo navegador-->
        <meta name="description" content="página principal">    <!-- descrição da página, usada pelo navegador-->
        <link rel="stylesheet" href="estilo/style.css" type="text/css">     <!-- usa estilo externo -->
        <link rel="shortcut icon" href="imagem/Bakery.png" type="image/x-icon">     <!-- adiciona um favicon -->
    </head>
<body>

<?php
    session_start(); // informa ao PHP que iremos trabalhar com sessão
    require 'bd/conectaBD.php'; 

    // Cria conexão
    $conn = new mysqli($servername, $username, $password, $database);

    // Verifica conexão 
    if ($conn->connect_error) {
        die("<strong> Falha de conexão: </strong>" . $conn->connect_error);
    }

    $usuario = $conn->real_escape_string($_POST['Login']); // prepara a string recebida para ser utilizada em comando SQL
    $senha   = $conn->real_escape_string($_POST['Senha']); // prepara a string recebida para ser utilizada em comando SQL

    
    // Faz Select na Base de Dados
    $sql = "SELECT idCliente, Nome, Acesso FROM Clientes WHERE Login = '$usuario' AND Senha = md5('$senha')";
    
    if ($result = $conn->query($sql)) {
        
        /*
        Para comandos como INSERT, UPDATE e DELETE, query() retorna:
            true em caso de sucesso;
            false em caso de erro.
        Para SELECT, retorna um objeto mysqli_result que você pode percorrer com fetch_assoc(), fetch_row(), etc
        */
        if ($result->num_rows == 1) {
            $row = $result->fetch_assoc();
            
            /*
            fetch_assoc(): Retorna uma linha do resultado como um array associativo, onde as chaves são os nomes das colunas da tabela.
            fetch_row(): Retorna uma linha como um array indexado numericamente, onde os índices são números, não nomes.
            */
            $acesso = $row['Acesso'];
            //print_r($acesso);
            //die;

            
            $_SESSION ['Login']       = $usuario;
            $_SESSION ['idCliente']  = $row['idCliente'];
            $_SESSION ['Nome']        = $row['Nome'];
           
            unset($_SESSION['nao_autenticado']);
            unset($_SESSION ['mensagem_header'] ); 
            unset($_SESSION ['mensagem'] ); 

            
            
            if ($acesso == 'administrador'){
                header('location: /atividade_somativa_2/listarPedidos.php');
            }   
            else{
                header('location: /atividade_somativa_2/fazerPedidos.php');
            }
            
            exit();
            
        }else{
            $_SESSION ['nao_autenticado'] = true;
            $_SESSION ['mensagem_header'] = "Login";
            $_SESSION ['mensagem']        = "ERRO: Login ou Senha inválidos.";
            header('location: /atividade_somativa_2/index.html');
            exit();
        }
    }
    else {
        echo "Erro ao acessar o BD: " . mysqli_error($conn);
    }
    $conn->close();  //Encerra conexao com o BD
?>
    <?php require 'geral/rodape.php'; ?>
	</body>
</html>