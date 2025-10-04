package financiamento.modelo;

public class Apartamento extends Financiamento{
    private int prazomensal, vagasGaragem, andares;
    private double taxamensal;

    public Apartamento(double valor, int prazo, double taxa, int garagens, int andares){
        /**
         * Este é o método construtor que inicia um objeto.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         * @param Int com a quantidade de garagens.
         * @param Int com a quantidade de andares.
         */
        super(valor, prazo, taxa);      // chama o construtor da classe mãe
        setTaxamensal();
        setPrazomensal();
        setVagasGaragem(garagens);
        setAndares(andares);
    }

    @Override
    public double calcularPagamentoMensal(){    //sobreposição do método da classe mãe
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

    public int getVagasGaragem() {
        return vagasGaragem;
    }

    private void setVagasGaragem(int vagasGaragem) {
        this.vagasGaragem = vagasGaragem;
    }

    public int getAndares() {
        return andares;
    }

    private void setAndares(int andares) {
        this.andares = andares;
    }
    //método especial
    @Override
    public String toString() {  // retorna uma string com o estado dos atributos
        return "Dados do apartamento {" + "Valor : " + super.getValorImovel() + ", Prazo em anos: " + super.getPrazoFinanciamento() + ", Taxa de jurus anual: " + super.getTaxaJurosAnual()*100 + "%, Vagas de garagem: " + vagasGaragem + ", Quantidade de andares: " + andares + '}';
    }
}
