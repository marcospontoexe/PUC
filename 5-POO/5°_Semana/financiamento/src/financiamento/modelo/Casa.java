package financiamento.modelo;

public class Casa extends Financiamento {
    public Casa(double valor, int prazo, double taxa){
        /**
         * Este é o método construtor que inicia um objeto.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         */
        super(valor, prazo, taxa);
    }

    public double calcularPagamentoMensal(){
        /**
         * Este método calcula o pagamento mensal do financiamento imobiliário de casa.
         * @return Double com o valor do pagamento mensal do financiamento da casa.
         */
        return super.calcularPagamentoMensal() + 80.00;     // calcula o pagamento mensal utilizando o método da classe mãe e soma 80
    }
}
