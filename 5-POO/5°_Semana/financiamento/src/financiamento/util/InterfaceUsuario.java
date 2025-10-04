package financiamento.util;
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
}
