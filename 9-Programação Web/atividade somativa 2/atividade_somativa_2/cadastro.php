<html>
    <!-------------------------------------------------------------------------------
    Desenvolvimento Web
    PUCPR
    Profa. Cristina V. P. B. Souza
    Agosto/2022
---------------------------------------------------------------------------------->
<!-- Cadastro.php --> 
	<head>
    <meta charset="UTF-8">
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

        $nome    = $conn->real_escape_string($_POST['nome']); // prepara a string recebida para ser utilizada em comando SQL
        $login   = $conn->real_escape_string($_POST['Login']); // prepara a string recebida para ser utilizada em comando SQL
        $celular = $conn->real_escape_string($_POST['celular']); // prepara a string recebida para ser utilizada em comando SQL
        $senha   = $conn->real_escape_string($_POST['Senha1']); // prepara a string recebida para ser utilizada em comando SQL
        
        // Faz Select na Base de Dados
        $sql = "INSERT INTO Clientes (Nome, Login, Celular, Senha, Acesso) VALUES ('$nome','$login','$celular',md5('$senha'),'cliente')";

        if ($result = $conn->query($sql)) {
            $msg = "Registro cadastrado com sucesso! Você já pode realizar login.";
            $_SESSION ['nao_autenticado'] = true;
            $_SESSION ['mensagem_header'] = "Cadastro";
            $_SESSION ['mensagem']        = $msg;
            header('location: /atividade_somativa_2/form.html');
            exit();
        } else {
            $msg = "Erro executando INSERT: " . $conn->connect_error . " Tente novo cadastro.";
            $_SESSION ['nao_autenticado'] = true;
            $_SESSION ['mensagem_header'] = "Cadastro";
            $_SESSION ['mensagem']        = $msg;
            header('location: /atividade_somativa_2/form.html');
            exit();
            }
            header('location: form.html');

        $conn->close();  //Encerra conexao com o BD
    ?>
    <?php require 'geral/rodape.php'; ?>
	</body>
</html>