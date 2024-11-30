package financiamento.main;

import financiamento.modelo.Apartamento;
import financiamento.modelo.Casa;
import financiamento.modelo.Financiamento;
import financiamento.modelo.Terreno;
import financiamento.util.InterfaceUsuario;
import java.util.ArrayList;
import java.util.Scanner;   // para manipular entrada de dados
import java.util.Locale;    // para definir as configurações regionais deste código para pt-BR
//Para exibir um número com vírgula no lugar de ponto como separador decimal
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;



/**
 * @author Marcos Daniel Santana
 */
public class Main {
    public static void esperaSegundos(int tempo){
        try {
            // Delay de 2 segundos (2000 milissegundos)
            Thread.sleep(tempo*1000);
        } catch (InterruptedException e) {
            // Tratar a exceção caso a thread seja interrompida
            System.out.println("A pausa foi interrompida!");
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        int contador = 0, indice = 0, prazoAnos = 0, andares = 0, garagem = 0;
        double valorTotalImoveis = 0, valorTotalFinanciamentos = 0, valorImovel = 0, juroAnual =0, tamanhoTerreno = 0, areaConstruida = 0;
        String tipoTerreno = "", valorFormatado="", informacaoFinanciamento ="";
        String arquivo = "dados.txt";   //nome do arquivo gravado
        Locale.setDefault(new Locale("pt", "BR"));     //define as configurações regionais deste código para pt-BR (português do Brasil), troca o . pela ,
        Scanner teclado = new Scanner(System.in);


        DecimalFormatSymbols simbolos = new DecimalFormatSymbols();
        simbolos.setDecimalSeparator(',');
        simbolos.setGroupingSeparator('.'); // Opcional: usa ponto como separador de milhares
        DecimalFormat formatador = new DecimalFormat("#,##0.00", simbolos);
        ArrayList<Financiamento> listaFinanciamentos = new ArrayList<Financiamento>();  // instancia um arraylist de objetos da classe "Financiamento"
        InterfaceUsuario pessoa = new InterfaceUsuario();
        
        while (true){
            pessoa.gravarDados(arquivo, String.format("Dados do %d° financiamneto:\n", contador+1));
            //region financiamneto da casa
            System.out.printf("Digite os dados para o financiamento da %d° casa:\n", contador+1);
            valorImovel = pessoa.getValorImovel();
            prazoAnos = pessoa.getPrazoFinanciamentoAnos();
            juroAnual = pessoa.getTaxaJurusAnual();
            tamanhoTerreno = pessoa.getTamanhoTerreno();
            areaConstruida = pessoa.getAreaConstruida();
            listaFinanciamentos.add(new Casa(valorImovel, prazoAnos, juroAnual, tamanhoTerreno, areaConstruida));
            System.out.printf("Pagamento mensal da casa financiada: %.2f R$\n", listaFinanciamentos.get(indice).calcularPagamentoMensal());
            System.out.printf("Pagamento total do financiamento da casa: %.2f R$\n\n", listaFinanciamentos.get(indice).calcularTotalPago());
            informacaoFinanciamento = listaFinanciamentos.get(indice).toString();
            System.out.println(informacaoFinanciamento);
            pessoa.gravarDados(arquivo, informacaoFinanciamento);
            pessoa.gravarDados(arquivo, "\n");
            indice += 1;
            //endregion

            //region financiamento do apartamento
            System.out.printf("Simulando o financiamento do %d° apartamento...\n", contador+1);
            esperaSegundos(2);
            andares = pessoa.getAndares();
            garagem = pessoa.getVagasGaragem();
            listaFinanciamentos.add(new Apartamento(valorImovel, prazoAnos, juroAnual, garagem, andares));
            System.out.printf("Pagamento mensal do apartamento financiada: %.2f R$\n", listaFinanciamentos.get(indice).calcularPagamentoMensal());
            System.out.printf("Pagamento total do financiamento da apartamento: %.2f R$\n\n", listaFinanciamentos.get(indice).calcularTotalPago());
            informacaoFinanciamento = listaFinanciamentos.get(indice).toString();
            System.out.println(informacaoFinanciamento);
            pessoa.gravarDados(arquivo, informacaoFinanciamento);
            pessoa.gravarDados(arquivo, "\n");
            indice += 1;
            //endregion

            //region financiamento do terreno
            System.out.printf("Simulando o financiamento do %d° terreno...\n", contador+1);
            esperaSegundos(2);
            tipoTerreno = pessoa.getTipoTerreno();
            listaFinanciamentos.add(new Terreno(valorImovel, prazoAnos, juroAnual, tipoTerreno));
            System.out.printf("Pagamento mensal do terreno financiado: %.2f R$\n", listaFinanciamentos.get(indice).calcularPagamentoMensal());
            System.out.printf("Pagamento total do financiamento do terreno: %.2f R$\n\n", listaFinanciamentos.get(indice).calcularTotalPago());
            informacaoFinanciamento = listaFinanciamentos.get(indice).toString();
            System.out.println(informacaoFinanciamento);
            pessoa.gravarDados(arquivo, informacaoFinanciamento);
            pessoa.gravarDados(arquivo, "----------------------------------------------------------------------------\n");
            indice += 1;
            //endregion

            System.out.println("Deseja continuar? (S/N):");
            String resposta = teclado.nextLine();              //recebe uma string de teclado
            resposta = resposta.replaceAll("\\s+", "").toUpperCase();   // Remove espaços em branco e converte para maiúsculas
            while(resposta.isEmpty()){  // garante que a string não esteja vazia
                System.out.println("Você não digitou nada! Digite S ou N :");
                resposta = teclado.nextLine();
                resposta = resposta.replaceAll("\\s+", "").toUpperCase();
            }
            while(resposta.charAt(0) != 'S' && resposta.charAt(0) != 'N'){ // garante que o usuário digite a resposta correta
                System.out.println("Valor incorreto! Digite S ou N:");
                resposta = teclado.nextLine();
                resposta = resposta.replaceAll("\\s+", "").toUpperCase();
                while(resposta.isEmpty()){  // garante que a string não esteja vazia
                    System.out.println("Você não digitou nada! Digite S ou N :");
                    resposta = teclado.nextLine();
                    resposta = resposta.replaceAll("\\s+", "").toUpperCase();
                }
            }

            if(resposta.charAt(0) == 'N'){
                break;
            }
            else{
                contador += 1;
            }
        }

        for (Financiamento f : listaFinanciamentos) { // imprime elemento por elemento
            valorTotalImoveis += f.getValorImovel();
            valorTotalFinanciamentos += f.calcularTotalPago();
        }
        valorFormatado = formatador.format(valorTotalImoveis);
        pessoa.gravarDados(arquivo, String.format("O valor total pago nos imóveis é: %s R$\n", valorFormatado));
        System.out.printf("O valor total pago nos imóveis é: %s R$\n", valorFormatado);
        valorFormatado = formatador.format(valorTotalFinanciamentos);
        pessoa.gravarDados(arquivo, String.format("O valor total pago nos financiamentos é: %s R$\n", valorFormatado));
        System.out.printf("O valor total pago nos financiamentos é: %s R$\n", valorFormatado);

        System.out.println("Dados do arquivo gravado:");
        pessoa.lerDados(arquivo);
    }
}