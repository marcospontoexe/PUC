package financiamento;

/**
 * @author Marcos Daniel Santana
 */
public class Main {
    public static void main(String[] args) {
        InterfaceUsuario pessoa = new InterfaceUsuario();
        InterfaceUsuario pessoa2 = new InterfaceUsuario();

        Financiamento finan = new Financiamento(pessoa.getValorImovel(), pessoa.getPrazoFinanciamentoAnos(), pessoa.getTaxaJurusAnual());
        Financiamento finan2 = new Financiamento(pessoa2.getValorImovel(), pessoa2.getPrazoFinanciamentoAnos(), pessoa2.getTaxaJurusAnual());

        System.out.printf("Pagamento mensal: %.2f R$\n", finan.calcularPagamentoMensal());
        System.out.printf("Pagamento total: %.2f R$\n", finan.calcularTotalPago());
        System.out.printf("Pagamento mensal: %.2f R$\n", finan2.calcularPagamentoMensal());
        System.out.printf("Pagamento total: %.2f R$\n", finan2.calcularTotalPago());

    }
}