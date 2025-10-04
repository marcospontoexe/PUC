package financiamento.modelo;

import financiamento.util.AumentoMaiorDoQueJurosException;

import java.sql.SQLOutput;

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
        double valorMensalSemJuros = super.getValorImovel()/(super.getPrazoFinanciamento()*12);   //calcula o valor mensal sem o juros
        double valorMensalComJuros = (super.getValorImovel()/(super.getPrazoFinanciamento()*12))*(1+(super.getTaxaJurosAnual()/12));    //calcula o valor mensal com juros o juros
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
}
