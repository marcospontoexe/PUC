package financiamento.modelo;

import financiamento.util.AumentoMaiorDoQueJurosException;
//Para exibir um número com vírgula no lugar de ponto como separador decimal
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

import java.sql.SQLOutput;

public class Casa extends Financiamento {
    //Atributos
    private double tamanhoAreaConstruida, tamanhoTerreno;
    private String valorFormatado;
    DecimalFormatSymbols simbolos = new DecimalFormatSymbols();
    DecimalFormat formatador = new DecimalFormat("#,##0.00", simbolos);

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
        simbolos.setDecimalSeparator(',');
        simbolos.setGroupingSeparator('.'); // Opcional: usa ponto como separador de milhares
    }

    private void SeguroMaiorQueJuros(double juros, double seguro) throws AumentoMaiorDoQueJurosException{
        if(seguro > juros){
            throw new AumentoMaiorDoQueJurosException(String.format("A taxa de seguro de %.2f R$ é maior que o juros da mensalidade de %.2f R$!", seguro, juros));
        }
    }

    @Override
    public double calcularPagamentoMensal(){        //sobreposição do método da classe mãe
        /**
         * Este método calcula o pagamento mensal do financiamento imobiliário de casa de acordo com o valor do seguro.
         * @return Double com o valor do pagamento mensal do financiamento da casa.
         */
        double valorMensalSemJuros = this.getValorImovel()/(this.getPrazoFinanciamento()*12);   //calcula o valor mensal sem o juros
        double valorMensalComJuros = (this.getValorImovel()/(this.getPrazoFinanciamento()*12))*(1+(this.getTaxaJurosAnual()/12));    //calcula o valor mensal com juros o juros
        double valorjuros = valorMensalComJuros - valorMensalSemJuros;   // calcula o juros cobrado a cada mes

        try {
            SeguroMaiorQueJuros(valorjuros, 80);
            return valorMensalComJuros + 80;
        }
        catch (AumentoMaiorDoQueJurosException e){
            System.out.println(e.getMessage());
            System.out.printf("Taxa de seguro reajustada para %.2f R$\n", valorjuros);
            return valorMensalComJuros + valorjuros;
        }
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

    //método especial
    @Override
    public String toString() {  // retorna uma string com o estado dos atributos
        StringBuilder sb = new StringBuilder();
        sb.append("Dados da casa:" + "\n");
        valorFormatado = formatador.format(this.getValorImovel());
        sb.append(String.format("Valor: %s R$.\n", valorFormatado));
        sb.append(String.format("Prazo: %d anos.\n", this.getPrazoFinanciamento() ));
        valorFormatado = formatador.format(this.getTaxaJurosAnual()*100);
        sb.append(String.format("Taxa de jurus anual: %s %%.\n", valorFormatado));
        valorFormatado = formatador.format(this.getTamanhoTerreno());
        sb.append(String.format("Tamanho do terreno: %s m²\n", valorFormatado));
        valorFormatado = formatador.format(this.getTamanhoAreaConstruida());
        sb.append(String.format("Área construida: %s m²\n", valorFormatado));

        return sb.toString();
    }
}
