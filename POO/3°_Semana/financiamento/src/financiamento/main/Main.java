package financiamento.main;

import financiamento.modelo.Financiamento;
import financiamento.util.InterfaceUsuario;

/**
 * @author Marcos Daniel Santana
 */
public class Main {
    public static void main(String[] args) {
        InterfaceUsuario pessoa = new InterfaceUsuario();
        InterfaceUsuario pessoa2 = new InterfaceUsuario();

        Financiamento finan = new Financiamento(pessoa.getValorImovel(), pessoa.getPrazoFinanciamentoAnos(), pessoa.getTaxaJurusAnual());

        System.out.printf("Pagamento mensal: %.2f R$\n", finan.calcularPagamentoMensal());
        System.out.printf("Pagamento total: %.2f R$\n", finan.calcularTotalPago());


    }
}