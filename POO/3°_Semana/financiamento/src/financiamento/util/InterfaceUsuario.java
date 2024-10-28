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
         * @return Double com o valor doimóvel.
         */
        double valor = -1;
        System.out.println("Digite o valor do imóvel financiado :");
        while (true) {
            if(teclado.hasNextDouble()){  // Verifica se o valor digitado é um double maior que zero
                valor = teclado.nextDouble();
                if (valor > 0 && valor <= 1000000) {    // Verifica se o valor é maior que zero
                    break; // Valor válido, saida condicional if
                }
                else if(valor > 1000000){
                    System.out.println("Esse sistema não financia imóvel a partir de 1 milhão de reais!");
                }
                else if(valor < 0){
                    System.out.println("O valor digitado deve ser maior que zero!");
                }
                else{
                    System.out.println("O valor digitado está incorreto!");
                }
            }else{
                System.out.println("Valor incorreto!. Digite um valor numérico (R$) usando vírgula: ");
                teclado.next(); // Limpa a entrada inválida
            }
        }
        return valor;
    }

    public int getPrazoFinanciamentoAnos(){
        /**
         * Este método pede ao usuário para que digite o prazo do financiamento em anos.
         * @return int com o valor digitado pelo usuário.
         */
        int valor = -1;
        System.out.println("Digite o prazo do financiamento em anos:");
        while (true) {
            if(teclado.hasNextInt()){  // Verifica se o valor digitado é um tipo int maior que zero
                valor = teclado.nextInt();
                if (valor > 0 && valor <= 35) {    // Verifica se o valor é maior que zero
                    break; // Valor válido, saida condicional if
                }
                else if(valor > 35){
                    System.out.println("O prazo máximo permitido é de 35 anos!");
                }
                else if(valor < 0){
                    System.out.println("O valor digitado deve ser maior que zero!");
                }
                else{
                    System.out.println("O valor digitado está incorreto!");
                }
            }
            else{
                System.out.println("Valor incorreto!. Digite um valor numérico: ");
                teclado.next(); // Limpa a entrada inválida
            }
        }
        return valor;
    }

    public double getTaxaJurusAnual(){
        /**
         * Este método pede ao usuário para que digite a taxa de juros anual.
         * @return double com o valor digitado pelo usuário.
         */
        double valor = -1;
        System.out.println("Digite a taxa de juros anual:");
        while (true) {
            if(teclado.hasNextDouble()){  // Verifica se o valor digitado é um double maior que zero
                valor = teclado.nextDouble();
                if (valor > 0 && valor <= 100) {    // Verifica se o valor é maior que zero
                    break; // Valor válido, saida condicional if
                }
                else if(valor > 100){
                    System.out.println("A taxa de jurus não deve ser maior que 100%!");
                }
                else if(valor < 0){
                    System.out.println("O valor digitado deve ser maior que zero!");
                }
                else {
                    System.out.println("O valor digitado está incorreto!");
                }
            }else{
                System.out.println("Valor incorreto!. Digite um valor numérico usando vírgula: ");
                teclado.next(); // Limpa a entrada inválida
            }
        }
        return valor;
    }
}
