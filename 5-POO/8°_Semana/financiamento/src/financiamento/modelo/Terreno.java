package financiamento.modelo;

//Para exibir um número com vírgula no lugar de ponto como separador decimal
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public final class Terreno extends Financiamento {      // classe final, não pode gerar classes filhas
    private String TipoTerreno;
    private String valorFormatado;
    DecimalFormatSymbols simbolos = new DecimalFormatSymbols();
    DecimalFormat formatador = new DecimalFormat("#,##0.00", simbolos);

    public Terreno(double valor, int prazo, double taxa, String terreno){
        /**
         * Este é o método construtor que inicia um objeto.
         * @param Double com o valor do imóvel.
         * @param Int com o prazo od financiamento em anos.
         * @param Double com a taxa de jurus anual.
         */
        super(valor, prazo, taxa);
        setTipoTerreno(terreno);
        simbolos.setDecimalSeparator(',');
        simbolos.setGroupingSeparator('.'); // Opcional: usa ponto como separador de milhares
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

    //método especial
    @Override
    public String toString() {  // retorna uma string com o estado dos atributos
        StringBuilder sb = new StringBuilder();
        sb.append("Dados do terreno:" + "\n");
        valorFormatado = formatador.format(this.getValorImovel());
        sb.append(String.format("Valor: %s R$.\n", valorFormatado));
        sb.append(String.format("Prazo: %d anos.\n", this.getPrazoFinanciamento() ));
        valorFormatado = formatador.format(this.getTaxaJurosAnual()*100);
        sb.append(String.format("Taxa de jurus anual: %s %%.\n", valorFormatado));
        sb.append(String.format("Tipo do terreno: %s.\n", this.getTipoTerreno()));


        return sb.toString();
    }
}
