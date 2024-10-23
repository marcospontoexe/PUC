package financiamento;
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
        System.out.println("Digite o valor do imóvel financiado:");
        return teclado.nextDouble();
    }

    public int getPrazoFinanciamentoAnos(){
        /**
         * Este método pede ao usuário para que digite o prazo do financiamento em anos.
         * @return int com o valor digitado pelo usuário.
         */
        System.out.println("Digite o prazo do financiamento em anos:");
        return teclado.nextInt();
    }

    public double getTaxaJurusAnual(){
        /**
         * Este método pede ao usuário para que digite a taxa de juros anual.
         * @return double com o valor digitado pelo usuário.
         */
        System.out.println("Digite a taxa de juros anual:");
        return teclado.nextDouble();
    }
}
