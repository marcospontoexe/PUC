package financiamento.modelo;

public class Apartamento extends Financiamento{
    private int prazomensal;
    private double taxamensal;
    public Apartamento(double valor, int prazo, double taxa){
        /**
         * Este é o método construtor que inicia um objeto.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         */
        super(valor, prazo, taxa);      // chama o construtor da classe mãe
        setTaxamensal();
        setPrazomensal();
    }

    public double calcularPagamentoMensal(){
        /**
         * Este método calcula o pagamento mensal do financiamento imobiliário de apartamento.
         * @return Double com o valor do pagamento mensal do financiamento do apartamento.
         */
        return (super.getValorImovel() * getTaxamensal() * Math.pow(1+getTaxamensal(), getPrazomensal())) / Math.pow(1+getTaxamensal(), getPrazomensal())-1;
        //double valor = (super.getValorImovel() * (1 + getTaxamensal() * getTaxamensal()) ^ (getPrazomensal()) / ((1 + getPrazomensal()) ^ getPrazomensal() - 1);
        //return valor;
    }

    public double getTaxamensal() {
        return this.taxamensal;
    }

    private void setTaxamensal() {
        this.taxamensal = super.getTaxaJurosAnual()/12;         // 'taxamensal' recebe o taxa anual da classe mãe dividido por 12 meses
    }

    public int getPrazomensal() {
        return this.prazomensal;
    }

    private void setPrazomensal() {
        this.prazomensal = super.getPrazoFinanciamento()*12;    // 'prazomensal' recebe o prazo anual da classe mãe multiplicado por 12 meses
    }
}
