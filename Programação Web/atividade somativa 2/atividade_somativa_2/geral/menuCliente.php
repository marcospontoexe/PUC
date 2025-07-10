<!-------------------------------------------------------------------------------
    Desenvolvimento Web
    PUCPR
    Profa. Cristina V. P. B. Souza
    Agosto/2022
---------------------------------------------------------------------------------->
<!-- menu.php -->

	<!-- Top -->
	
	<?php 
	
	session_start();
	/*
	if(!isset($_SESSION ['login'])){                              // Não houve login ainda
        unset($_SESSION ['nao_autenticado']);
		unset($_SESSION ['mensagem_header'] ); 
		unset($_SESSION ['mensagem'] ); 
		header('location: /atividade_somativa_2/index.html');    // Vai para a página inicial
		exit();
    }
	*/
	?>
	
	<header class="titleTop">
		<h2>Cupcake Backery Shop</h2>
		
		<div class="menuRight"> 
			Cliente: <?php echo $_SESSION ['Nome']; ?>&nbsp;<a href="logout.php" >&nbsp;Sair&nbsp;</a>
		</div >
    </header>

	<!-- Sidebar -->
	<nav class="sidebar">
        <a href="index.html" target="_self" rel="next">Home</a>
        <a href="news.html" target="_self" rel="next">News</a>
        <a class="active" textImghref="form.html" target="_blank" rel="next">Pedir</a> 
        <a href="about.html" target="_self" rel="next">About</a>
    </nav>


	<script type="text/javascript" src="script/myScriptClinic.js"></script>
