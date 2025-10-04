package financiamento.util;
import financiamento.modelo.Financiamento;

import javax.lang.model.type.NullType;
import java.io.*;
import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;   // para manipular entrada de dados
//Para exibir um número com vírgula no lugar de ponto como separador decimal
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

//exeções


public class InterfaceUsuario {
    /**
     * Esta classe é responsável por lidar com a entrada de dados do usuário
     * @author Marcos Daniel Santana
     */
    static FileWriter arquivo = null;   // objeto para escrita de arquivo
    static FileReader leitor = null;   // objeto para leitura de arquivo
    static ObjectOutputStream ObjetoGravado = null;     //Objeto para gravar um objeto serializavel
    static ObjectInputStream Objetolido = null;     //Objeto para ler um objeto serializavel
    static Scanner teclado = new Scanner(System.in);    //Cria um objeto estático para a classe "InterfaceUsuario()". "teclado" é o mesmo para todos os objetos da classe "InterfaceUsuario()"
    // Configura o formato para usar vírgula como separador decimal
    DecimalFormatSymbols simbolos = new DecimalFormatSymbols();
    DecimalFormat formatador = new DecimalFormat("#,##0.00", simbolos);

    //MÉTODOS
    public InterfaceUsuario(){
        Locale.setDefault(new Locale("pt", "BR"));     //define as configurações regionais deste código para pt-BR (português do Brasil), troca o . pela ,
        simbolos.setDecimalSeparator(',');
        simbolos.setGroupingSeparator('.'); // Opcional: usa ponto como separador de milhares
    }

    public double getValorImovel(){
        /**
         * Este método obtem do usuário o valor do imóvel.
         * @return Double com o valor doimóvel, caso o valor retornado seja -1 não foi posspivel capturar os dados fornecidos pelo usuário.
         */
        double valor = -1; // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite o valor do imóvel financiado :");
        while (true) {
            try {
                String entrada = teclado.next();    // lê a entrada do usuário como uma string, independente do tipo.
                entrada = entrada.replace(',', '.');   // Substitui a vírgula pelo ponto, para suportar o separador decimal padrão do Java
                valor = Double.parseDouble(entrada); // Tenta converter a string para double, caso não consiga lança uma exeção

                if (valor > 50000 && valor <= 1000000) {    // Verifica se o valor está entre cinquenta mil e um milhão de reais
                    return valor;
                } else if (valor > 1000000) {
                    System.out.println("Esse sistema não financia imóvel a partir de 1 milhão de reais!");
                } else if (valor < 50000) {
                    System.out.println("O valor digitado deve ser maior que cinquenta mil reais!");
                } else {
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            catch (NumberFormatException e){
                // Captura exceções inesperadas, exibe uma mensagem de erro e permite nova tentativa
                System.out.println("Entrada inválida! Por favor, digite um valor numérico válido (use vírgula como separador decimal).");
                System.out.println("Erro: " + e.getMessage());
            }
            finally {
                String valorFormatado = formatador.format(valor);
                System.out.printf("Valor do imóvel: %s R$.\n", valorFormatado);
            }
        }
    }

    public int getPrazoFinanciamentoAnos(){
        /**
         * Este método pede ao usuário para que digite o prazo do financiamento em anos.
         * @return int com o valor digitado pelo usuário, caso o valor retornado seja -1 não foi posspivel capturar os dados fornecidos pelo usuário.
         */
        int valor = -1;     // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite o prazo do financiamento em anos:");
        while (true) {
            try{
                String entrada = teclado.next(); // Lê a entrada do usuário como string
                valor = Integer.parseInt(entrada); // tenta converter a string para um número inteiro

                if (valor >= 5 && valor <= 35) {    // Verifica se o período está entre 5 e 35 anos
                    return valor;
                }
                else if(valor > 35){
                    System.out.println("O prazo máximo permitido é de 35 anos!");
                }
                else if(valor < 5){
                    System.out.println("O prazo mínimo é de cinco anos!");
                }
                else{
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            catch (NumberFormatException e) {
                System.out.println("Valor incorreto! Digite um valor numérico inteiro:");
            }
            finally {
                System.out.printf("Prazo de %d anos.\n", valor);
            }
        }
    }

    public double getTaxaJurusAnual(){
        /**
         * Este método pede ao usuário para que digite a taxa de juros anual.
         * @return double com o valor digitado pelo usuário, caso o valor retornado seja -1 não foi posspivel capturar os dados fornecidos pelo usuário.
         */
        double valor = -1;      // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite a taxa de juros anual:");
        while (true) {
            try {
                String entrada = teclado.next();    // lê a entrada do usuário como uma string, independente do tipo.
                entrada = entrada.replace(',', '.');   // Substitui a vírgula pelo ponto, para suportar o separador decimal padrão do Java
                valor = Double.parseDouble(entrada); // Tenta converter a string para double, caso não consiga lança uma exeção

                if (valor >= 2 && valor <= 100) {    // Verifica se a taxa de jurus anual está entre 2% e 100%
                    return valor;
                }
                else if(valor > 100){
                    System.out.println("A taxa de jurus não deve ser maior que 100%!");
                }
                else if(valor < 2){
                    System.out.println("A taxa de jurus anual mínima de é 2%");
                }
                else {
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            catch (NumberFormatException e){
                // Captura exceções inesperadas, exibe uma mensagem de erro e permite nova tentativa
                System.out.println("Entrada inválida! Por favor, digite um valor numérico válido (use vírgula como separador decimal).");
                System.out.println("Erro: " + e.getMessage());
            }
            finally {
                String valorFormatado = formatador.format(valor);
                System.out.printf("Taxa anual: %s %%.\n", valorFormatado);
            }
        }
    }

    public int getVagasGaragem() {
        /**
         * Este método pede ao usuário para que digite a quantidade de vagas de garagem do apartamento.
         * @return int com o valor digitado pelo usuário, caso o valor retornado seja -1 não foi posspivel capturar os dados fornecidos pelo usuário.
         */
        int valor = -1;     // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite a quantidade vagas de garagem:");
        while (true) {
            try{
                String entrada = teclado.next(); // Lê a entrada do usuário como string
                valor = Integer.parseInt(entrada); // tenta converter a string para um número inteiro

                if (valor >= 0 && valor <= 10) {    // Verifica se a quantidade de garagens está entre 0 e 10
                    return valor;
                }
                else if(valor > 10){
                    System.out.println("A quantidade máxima de garagens por apartamento é 10!");
                }
                else if(valor < 0){
                    System.out.println("Você digitou um valor negativo!");
                }
                else{
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            catch (NumberFormatException e) {
                System.out.println("Valor incorreto! Digite um valor numérico inteiro:");
            }
            finally {
                System.out.printf("Vagas de garagem: %d.\n", valor);
            }
        }
    }

    public int getAndares() {
        /**
         * Este método pede ao usuário para que digite a quantidade de andares do apartamento.
         * @return int com o valor digitado pelo usuário, caso o valor retornado seja -1 não foi posspivel capturar os dados fornecidos pelo usuário.
         */
        int valor = -1;     // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite a quantidade de andares:");

        while (true) {
            try {
                String entrada = teclado.next(); // Lê a entrada do usuário como string
                valor = Integer.parseInt(entrada); // tenta converter a string para um número inteiro

                if (valor > 0 && valor <= 5) {    // Verifica se a quantidade de andares está entre 1 e 5
                    return valor;
                }
                else if(valor > 5){
                    System.out.println("A quantidade máxima de andares por apartamento é 5!");
                }
                else if(valor == 0){
                    System.out.println("A quantidade de andares não pode ser zero!");
                }
                else if(valor < 0){
                    System.out.println("Você digitou um valor negativo!");
                }
                else{
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            catch (NumberFormatException e) {
                System.out.println("Valor incorreto! Digite um valor numérico inteiro:");
            }
            finally {
                System.out.printf("Quantidade de andares: %d.\n", valor);
            }
        }
    }

    public double getAreaConstruida(){
        /**
         * Este método pede ao usuário para que digite a área construída.
         * @return double com o valor digitado pelo usuário, caso o valor retornado seja -1 não foi possível capturar os dados fornecidos pelo usuário.
         */
        double valor = -1;      // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite a área construída em metros:");
        while (true) {
            try {
                String entrada = teclado.next();    // lê a entrada do usuário como uma string, independente do tipo.
                entrada = entrada.replace(',', '.');   // Substitui a vírgula pelo ponto, para suportar o separador decimal padrão do Java
                valor = Double.parseDouble(entrada); // Tenta converter a string para double, caso não consiga lança uma exeção

                if (valor >= 30 && valor <= 5000) {    // Verifica se a área construída está entre 30 e 5 mil metros quadrado
                    return valor;
                }
                else if(valor > 5000){
                    System.out.println("A área construída não pode ser maior do que 5 mil metros quadrado!");
                }
                else if(valor < 30){
                    System.out.println("A área construída não pode ser menor do que 30 metros quadrado!");
                }
                else {
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            catch (NumberFormatException e){
                // Captura exceções inesperadas, exibe uma mensagem de erro e permite nova tentativa
                System.out.println("Entrada inválida! Por favor, digite um valor numérico válido (use vírgula como separador decimal).");
                System.out.println("Erro: " + e.getMessage());
            }
            finally {
                String valorFormatado = formatador.format(valor);
                System.out.printf("Área construida: %s m².\n", valorFormatado);
            }
        }
    }

    public double getTamanhoTerreno(){
        /**
         * Este método pede ao usuário para que digite a área do terreno.
         * @return double com o valor digitado pelo usuário, caso o valor retornado seja -1 não foi possível capturar os dados fornecidos pelo usuário.
         */
        double valor = -1;      // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite o tamanho da área do terreno em metros:");
        while (true) {
            try{
                String entrada = teclado.next();    // lê a entrada do usuário como uma string, independente do tipo.
                entrada = entrada.replace(',', '.');   // Substitui a vírgula pelo ponto, para suportar o separador decimal padrão do Java
                valor = Double.parseDouble(entrada); // Tenta converter a string para double, caso não consiga lança uma exeção

                if (valor >= 40 && valor <= 96800) {    // Verifica se a área construída está entre 40 e 96800 metros quadrado
                    return valor;
                }
                else if(valor > 96800){
                    System.out.println("A área do terreno não pode ser maior do que 96800 metros quadrado!");
                }
                else if(valor < 40){
                    System.out.println("A área do terreno não pode ser menor do que 40 metros quadrado!");
                }
                else {
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            catch (NumberFormatException e){
                // Captura exceções inesperadas, exibe uma mensagem de erro e permite nova tentativa
                System.out.println("Entrada inválida! Por favor, digite um valor numérico válido (use vírgula como separador decimal).");
                System.out.println("Erro: " + e.getMessage());
            }
            finally {
                String valorFormatado = formatador.format(valor);
                System.out.printf("Tamanho do terreno: %s m².\n", valorFormatado);
            }
        }
    }

    public String getTipoTerreno() {
        /**
         * Este método pede ao usuário para que digite o tipo do terreno.
         * @return String com o valor digitado pelo usuário, caso o valor retornado seja NULL não foi possível capturar os dados fornecidos pelo usuário.
         */
        String terreno = null; // caso não seja possível capturar um valor do usuário, o método retorna um valor nulo, indicando erro
        System.out.println("Digite o tipo do terreno (residencial ou comercial):");
        String valor = teclado.nextLine();
        while (true) {
            try {
                valor = teclado.nextLine();

                // Garante que a entrada não esteja vazia
                if (valor.isEmpty()) {
                    throw new IllegalArgumentException("Você não digitou nada! Digite residencial ou comercial.");
                }

                // Garante que sejam digitadas apenas letras
                if (!valor.matches("[a-zA-Z\\s]+")) { // Permite letras e espaços
                    throw new IllegalArgumentException("Digite apenas letras.");
                }

                // Remove espaços em branco e converte para maiúsculas
                valor = valor.replaceAll("\\s+", "").toUpperCase();

                // Garante que o valor seja "RESIDENCIAL" ou "COMERCIAL"
                if (valor.charAt(0) != 'R' && valor.charAt(0) != 'C') {
                    throw new IllegalArgumentException("Valor incorreto! Digite residencial ou comercial.");
                }

                // Retorna o tipo do terreno correspondente
                terreno = (valor.charAt(0) == 'R') ? "residencial" : "comercial";
                return terreno;

            }
            catch (IllegalArgumentException e) {
                // Exibe a mensagem de erro para o usuário
                System.out.println(e.getMessage());
            }
            finally {
                System.out.printf("Tipo do terreno: %s.\n", terreno);
            }
        }
    }

    public void gravarDados(String nomeArquivo, String texto){
        /**
         * Este método tenta abrir um artquivo .txt, caso não exista, cria um arquivo .txt para gravar uma string fornecida.
         * @param String nome do arqivo .txt.
         * @param String com o valor a ser gravado.
         */
        System.out.printf("Gravando dados no arquivo %s.\n", nomeArquivo);
        //tenta abrir um artquivo .txt, caso não exista, cria um arquivo .txt
        try{
            arquivo = new FileWriter(nomeArquivo, true);  // tenta abrir no modo escrita o arquivo na pasta local
            arquivo.write(texto);        //escreve a string 'texto' no 'arquivo'
            arquivo.flush();          //limpa o buffer
            arquivo.close();        //fecha o arquivo
        }
        catch (FileNotFoundException e){
            System.out.println("O arquivo não foi encontrado.");
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }

    public void lerDados(String nomeArquivo){
        /**
         * Este método tenta abrir um objeto.
         * @param String nome do arqivo .txt
         */
        int caractere = 0;    //inteiro que recebe o valor ASCII do arquivo lido
        //tenta abrir um artquivo .txt
        try{
            leitor = new FileReader(nomeArquivo);  // tenta abrir no modo leitura o arquivo na pasta local
            while ((caractere = leitor.read()) != -1){   // lê caractere por caractere convertido para o padrão ASCII, quando receber -1 significa and of file
                System.out.print((char)caractere);
            }
            leitor.close();        //fecha o arquivo
        }
        catch (FileNotFoundException e){
            System.out.println("O arquivo não foi encontrado.");
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }

    public void gravarObjeto(String nomeArquivo, ArrayList classe){
        /**
         * Este método tenta gravar um objeto.
         * @param String nome do arqivo que gravará um objeto.
         * @param ArrayList com os objetos a serem gravados.
         */
        try{
            System.out.printf("Gravando dados no arquivo %s.\n", nomeArquivo);
            ObjetoGravado = new ObjectOutputStream(new FileOutputStream(nomeArquivo));  // Instancia o objeto 'ObjetoGravado' e cria um arquivo para salvar o objeto recebido
            ObjetoGravado.writeObject(classe);    // salvar o objeto recebido para dentro do arquivo 'nomeArquivo'
            ObjetoGravado.flush();  //limpa o buffer
            ObjetoGravado.close(); //fecha o obeto 'ObjetoGravado'
        }
        catch (IOException e){
            e.printStackTrace();
        }

    }

    public void lerObjeto(String nomeArquivo){
        /**
         * Este método tenta ler um objeto pertecente a determinada classe .
         * @param String com o nome do arqivo que gravará um objeto.
         */
        try {
            Objetolido = new ObjectInputStream(new FileInputStream(nomeArquivo));  // Instancia o objeto 'Objetolido' para abrir o objeto serializado recebido
            ArrayList<Financiamento> listaLida = (ArrayList<Financiamento>) Objetolido.readObject();
            System.out.printf("Lista de financiamentos lida do arquivo: %s\n", nomeArquivo);
            for (Financiamento f : listaLida) {
                System.out.println(f);
            }
            Objetolido.close(); //fecha o obeto 'ObjetoGravado'
        }
        catch (EOFException e){ // quando chega ao final do arquivo
            System.out.println("Sucesso ao ler o objeto salvo!");
        }
        catch (IOException e){
            e.printStackTrace();
        }
        catch (ClassNotFoundException e){
            System.out.println("A classe não foi encontrada!");
        }

    }


}
