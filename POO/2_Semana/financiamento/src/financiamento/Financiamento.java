package financiamento;

/**
 * @author Marcos Daniel Santana
 */

public class Financiamento {
    /**
     * A classe Financiamento() calcula o financiamento imobiliários
     *
     */

    //ATRIBUTOS
    private double valorImovel;
    private int prazoFinanciamento;
    private double taxaJurosAnual;

    //MÉTODOS
    public Financiamento(double valor, int prazo, double taxa){
        this.valorImovel = valor;
        this.prazoFinanciamento = prazo;
        this.taxaJurosAnual = taxa;
    }

    public double calcularPagamentoMensal(){
        /**
         * Este método calcula o pagamento mensal do financiamento.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         * @return Double com o valor do pagamento mensal do financiamento.
         */
        // Pagamento mensal = (valor do imóvel / (prazo do financiamento em anos * 12)) * (1 + (taxa anual / 12))
    }

    public double calcularTotalPago(){
        //Total do pagamento = pagamento mensal * prazo do financiamento em anos * 12'
    }

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

}
