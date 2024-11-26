package financiamento.modelo;

/**
 * @author Marcos Daniel Santana
 */

public abstract class Financiamento {
    /**
     * A classe Financiamento() calcula o financiamento imobiliário
     *
     */

    //region ATRIBUTOS
    protected double valorImovel;
    protected int prazoFinanciamento;
    protected double taxaJurosAnual;
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

    public abstract double calcularPagamentoMensal();

    public final double calcularTotalPago(){    // método final, não pode ser sobrescrito nas classes filhas
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

    protected void setValorImovel(double valorImovel) {
        this.valorImovel = valorImovel;
    }

    protected void setPrazoFinanciamento(int prazo) {
        this.prazoFinanciamento = prazo;
    }

    public int getPrazoFinanciamento() {
        return this.prazoFinanciamento;
    }

    public double getTaxaJurosAnual() {
        return (this.taxaJurosAnual)/100;
    }

    protected void setTaxaJurosAnual(double JurosAnual) {
        this.taxaJurosAnual = JurosAnual;
    }
    //endregion
}
