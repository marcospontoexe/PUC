package financiamento.util;
import javax.lang.model.type.NullType;
import java.util.Locale;
import java.util.Scanner;   // para manipular entrada de dados

public class InterfaceUsuario {
    /**
     * Esta classe é responsável por lidar com a entrada de dados do usuário
     * @author Marcos Daniel Santana
     */
    static Scanner teclado = new Scanner(System.in);    //Cria um objeto estático para a classe "InterfaceUsuario()". "teclado" é o mesmo para todos os objetos da classe "InterfaceUsuario()"
    //Scanner teclado;
    //MÉTODOS

    public InterfaceUsuario(){
        Locale.setDefault(new Locale("pt", "BR"));     //define as configurações regionais deste código para pt-BR (português do Brasil), troca o . pela ,
        //this.teclado = new Scanner(System.in);
    }

    public double getValorImovel(){
        /**
         * Este método obtem do usuário o valor do imóvel.
         * @return Double com o valor doimóvel, caso o valor retornado seja -1 não foi posspivel capturar os dados fornecidos pelo usuário.
         */
        double valor = -1; // caso não seja possível capturar um valor do usuário, o método retorna -1, indicando erro
        System.out.println("Digite o valor do imóvel financiado :");
        while (true) {
            if(teclado.hasNextDouble()){  // Verifica se o valor digitado é um double
                valor = teclado.nextDouble();
                if (valor > 50000 && valor <= 1000000) {    // Verifica se o valor está entre cinquenta mil e um milhão de reais
                    return valor;
                }
                else if(valor > 1000000){
                    System.out.println("Esse sistema não financia imóvel a partir de 1 milhão de reais!");
                }
                else if(valor < 50000){
                    System.out.println("O valor digitado deve ser maior que cinquenta mil reais!");
                }
                else{
                    System.out.println("O valor digitado está incorreto!");
                }
            }else{
                System.out.println("Valor incorreto!. Digite um valor numérico (R$) usando vírgula: ");
                teclado.next(); // Limpa a entrada inválida
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
            if(teclado.hasNextInt()){  // Verifica se o valor digitado é um tipo int
                valor = teclado.nextInt();
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
            else{
                System.out.println("Valor incorreto!. Digite um valor numérico inteiro: ");
                teclado.next(); // Limpa a entrada inválida
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
            if(teclado.hasNextDouble()){  // Verifica se o valor digitado é um double maior que zero
                valor = teclado.nextDouble();
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
            }else{
                System.out.println("Valor incorreto!. Digite um valor numérico usando vírgula: ");
                teclado.next(); // Limpa a entrada inválida
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
            if(teclado.hasNextInt()){  // Verifica se o valor digitado é um tipo int
                valor = teclado.nextInt();
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
            else{
                System.out.println("Valor incorreto!. Digite um valor numérico inteiro: ");
                teclado.next(); // Limpa a entrada inválida
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
            if(teclado.hasNextInt()){  // Verifica se o valor digitado é um tipo int
                valor = teclado.nextInt();
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
            else{
                System.out.println("Valor incorreto!. Digite um valor numérico inteiro: ");
                teclado.next(); // Limpa a entrada inválida
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
            if(teclado.hasNextDouble()){  // Verifica se o valor digitado é um double maior que zero
                valor = teclado.nextDouble();
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
            }else{
                System.out.println("Valor incorreto!. Digite um valor numérico usando vírgula: ");
                teclado.next(); // Limpa a entrada inválida
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
            if(teclado.hasNextDouble()){  // Verifica se o valor digitado é um double maior que zero
                valor = teclado.nextDouble();
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
            }else{
                System.out.println("Valor incorreto!. Digite um valor numérico usando vírgula: ");
                teclado.next(); // Limpa a entrada inválida
            }
        }
    }

    public String getTipoTerreno(){
        /**
         * Este método pede ao usuário para que digite o tipo do terreno.
         * @return String com o valor digitado pelo usuário, caso o valor retornado seja NULL não foi possível capturar os dados fornecidos pelo usuário.
         */
        String valor = null;      // caso não seja possível capturar um valor do usuário, o método retorna um valor nulo, indicando erro
        System.out.println("Digite o tipo do terreno (residencial ou comercial):");
        valor = teclado.nextLine();
        while(valor.isEmpty()) {  // garante que a string não esteja vazia
            System.out.println("Você não digitou nada! Digite residencial ou comercial:");
            valor = teclado.nextLine();
        }
        while(!(valor.matches("[a-zA-Z]+"))){ //garante que seja digitado apenas letras
            System.out.println("Digite apenas letras:");
            valor = teclado.nextLine();
        }
        valor = valor.replaceAll("\\s+", "").toUpperCase();// Remove espaços em branco e converte para maiúsculas
        while(valor.charAt(0) != 'R' && valor.charAt(0) != 'C'){ // garante que o usuário digite a resposta correta
            System.out.println("Valor incorreto! Digite residencial ou comercial:");
            valor = teclado.nextLine();
            valor = valor.replaceAll("\\s+", "").toUpperCase();
            while(valor.isEmpty() || !(valor.matches("[a-zA-Z]+"))) {
                System.out.println("Valor incorreto! Digite residencial ou comercial:");
                valor = teclado.nextLine();
                valor = valor.replaceAll("\\s+", "").toUpperCase();
            }
        }
        if(valor.charAt(0) == 'R'){
            return "residencial";
        }
        else if(valor.charAt(0) == 'C'){
            return "comercial";
        }
        else{
            return null;
        }
    }
}
