package financiamento.modelo;

public final class Terreno extends Financiamento {      // classe final, não pode gerar classes filhas
    private String TipoTerreno;

    public Terreno(double valor, int prazo, double taxa, String terreno){
        /**
         * Este é o método construtor que inicia um objeto.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         */
        super(valor, prazo, taxa);
        setTipoTerreno(terreno);
    }

    @Override
    public double calcularPagamentoMensal(){    //sobreposição do método da classe mãe
        /**
         * Este método calcula o pagamento mensal do financiamento imobiliário de um terreno.
         * @return Double com o valor do pagamento mensal do financiamento de um terreno.
         */
        return (super.getValorImovel()/(super.getPrazoFinanciamento()*12))*(1+(super.getTaxaJurosAnual()/12)) * 1.02;     // calcula o pagamento mensal utilizando o método da classe mãe e soma 2%
    }

    public String getTipoTerreno() {
        return this.TipoTerreno;
    }

    private void setTipoTerreno(String tipoTerreno) {
        this.TipoTerreno = tipoTerreno;
    }
}
