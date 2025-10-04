package financiamento.main;

import financiamento.modelo.Financiamento;
import financiamento.util.InterfaceUsuario;
import java.util.ArrayList;
import java.util.Scanner;   // para manipular entrada de dados
import java.util.Locale;

/**
 * @author Marcos Daniel Santana
 */
public class Main {
    public static void main(String[] args) {
        int contador = 0;
        double valorTotalImoveis = 0, valorTotalFinanciamentos = 0, valorImovel = 0;
        Locale.setDefault(new Locale("pt", "BR"));     //define as configurações regionais deste código para pt-BR (português do Brasil), troca o . pela ,
        Scanner teclado = new Scanner(System.in);
        ArrayList<Financiamento> listaFinanciamentos = new ArrayList<Financiamento>();  // instancia um arraylist de objetos da classe "Financiamento"
        InterfaceUsuario pessoa = new InterfaceUsuario();

        while (true){
            System.out.println("Digite os dados para o financiamneto:");
            valorImovel = pessoa.getValorImovel();
            listaFinanciamentos.add(new Financiamento(valorImovel, pessoa.getPrazoFinanciamentoAnos(), pessoa.getTaxaJurusAnual()));
            System.out.printf("Pagamento mensal: %.2f R$\n", listaFinanciamentos.get(contador).calcularPagamentoMensal());
            System.out.printf("Pagamento total: %.2f R$\n", listaFinanciamentos.get(contador).calcularTotalPago());
            valorTotalImoveis += valorImovel;
            valorTotalFinanciamentos += listaFinanciamentos.get(contador).calcularTotalPago();
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
        System.out.printf("O valor total pago nos imóveis é: %.2f R$\n", valorTotalImoveis);
        System.out.printf("O valor total pago nos financiamentos é: %.2f R$\n", valorTotalFinanciamentos);
    }
}