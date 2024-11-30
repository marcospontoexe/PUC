package financiamento.modelo;

//Para exibir um número com vírgula no lugar de ponto como separador decimal
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class Apartamento extends Financiamento{
    private int prazomensal, vagasGaragem, andares;
    private double taxamensal;
    private String valorFormatado;
    DecimalFormatSymbols simbolos = new DecimalFormatSymbols();
    DecimalFormat formatador = new DecimalFormat("#,##0.00", simbolos);

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
        simbolos.setDecimalSeparator(',');
        simbolos.setGroupingSeparator('.'); // Opcional: usa ponto como separador de milhares
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
        StringBuilder sb = new StringBuilder();
        sb.append("Dados do apartamento:" + "\n");
        valorFormatado = formatador.format(this.getValorImovel());
        sb.append(String.format("Valor: %s R$.\n", valorFormatado));
        sb.append(String.format("Prazo: %d anos.\n", this.getPrazoFinanciamento() ));
        valorFormatado = formatador.format(this.getTaxaJurosAnual()*100);
        sb.append(String.format("Taxa de jurus anual: %s %%.\n", valorFormatado));
        sb.append(String.format("Vagas de garagem: %d.\n", this.getVagasGaragem()));
        sb.append(String.format("Quantidade de andares: %d.\n", this.getAndares()));

        return sb.toString();
    }
}
