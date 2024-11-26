package financiamento.modelo;

public class Casa extends Financiamento {
    //Atributos
    private double tamanhoAreaConstruida, tamanhoTerreno;

    public Casa(double valor, int prazo, double taxa, double tamanhoTerreno, double areaConstruida){
        /**
         * Este é o método construtor que inicia um objeto.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         */
        super(valor, prazo, taxa);
        setTamanhoTerreno(tamanhoTerreno);
        setTamanhoAreaConstruida(areaConstruida);
    }

    @Override
    public double calcularPagamentoMensal(){        //sobreposição do método da classe mãe
        /**
         * Este método calcula o pagamento mensal do financiamento imobiliário de casa.
         * @return Double com o valor do pagamento mensal do financiamento da casa.
         */
        return (super.getValorImovel()/(super.getPrazoFinanciamento()*12))*(1+(super.getTaxaJurosAnual()/12)) + 80.00;     // calcula o pagamento mensal utilizando o método da classe mãe e soma 80
    }

    public double getTamanhoTerreno() {
        return tamanhoTerreno;
    }

    private void setTamanhoTerreno(double tamanhoTerreno) {
        this.tamanhoTerreno = tamanhoTerreno;
    }

    public double getTamanhoAreaConstruida() {
        return tamanhoAreaConstruida;
    }

    private void setTamanhoAreaConstruida(double tamanhoAreaConstruida) {
        this.tamanhoAreaConstruida = tamanhoAreaConstruida;
    }
}
