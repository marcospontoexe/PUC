package financiamento.modelo;

/**
 * @author Marcos Daniel Santana
 */

public class Financiamento {
    /**
     * A classe Financiamento() calcula o financiamento imobiliário
     *
     */

    //region ATRIBUTOS
    private double valorImovel;
    private int prazoFinanciamento;
    private double taxaJurosAnual;
    //endregion

    //MÉTODOS
    public Financiamento(double valor, int prazo, double taxa){
        /**
         * Este é o método construtor que inicia um objeto.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         */
        setValorImovel(valor);
        setPrazoFinanciamento(prazo);
        setTaxaJurosAnual(taxa);
    }

    public double calcularPagamentoMensal(){
        /**
         * Este método calcula o pagamento mensal do financiamento imobiliário.
         * @return Double com o valor do pagamento mensal do financiamento.
         */
        return (getValorImovel()/(getPrazoFinanciamento()*12))*(1+(getTaxaJurosAnual()/12));
    }

    public double calcularTotalPago(){
        /**
         * Este método calcula o valor total pago do financiamento imobiliário.
         * @return Double com o valor total pago do financiamento imobiliário.
         */
        return this.calcularPagamentoMensal()*getPrazoFinanciamento()*12;
    }
    //region métodos acessores e modificadores
    public double getValorImovel() {
        return valorImovel;
    }

    public void setValorImovel(double valorImovel) {
        this.valorImovel = valorImovel;
    }

    public void setPrazoFinanciamento(int prazo) {
        this.prazoFinanciamento = prazo;
    }

    public int getPrazoFinanciamento() {
        return prazoFinanciamento;
    }

    public double getTaxaJurosAnual() {
        return taxaJurosAnual;
    }

    public void setTaxaJurosAnual(double JurosAnual) {
        this.taxaJurosAnual = JurosAnual;
    }
    //endregion
}
