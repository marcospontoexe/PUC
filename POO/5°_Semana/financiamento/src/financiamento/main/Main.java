package financiamento.main;

import financiamento.modelo.Casa;
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
        int contador = 0, prazoAnos = 0;
        double valorTotalImoveis = 0, valorTotalFinanciamentos = 0, valorImovel = 0, juroAnual =0;
        Locale.setDefault(new Locale("pt", "BR"));     //define as configurações regionais deste código para pt-BR (português do Brasil), troca o . pela ,
        Scanner teclado = new Scanner(System.in);
        ArrayList<Financiamento> listaFinanciamentos = new ArrayList<Financiamento>();  // instancia um arraylist de objetos da classe "Financiamento"
        InterfaceUsuario pessoa = new InterfaceUsuario();

        while (true){
            System.out.printf("Digite os dados para o financiamento da %d° casa:\n", contador+1);
            valorImovel = pessoa.getValorImovel();
            prazoAnos = pessoa.getPrazoFinanciamentoAnos();
            juroAnual = pessoa.getTaxaJurusAnual();
            listaFinanciamentos.add(new Casa(valorImovel, prazoAnos, juroAnual));
            System.out.printf("Pagamento mensal da casa financiada: %.2f R$\n", listaFinanciamentos.get(contador).calcularPagamentoMensal());
            System.out.printf("Pagamento total do financiamento da casa: %.2f R$\n\n", listaFinanciamentos.get(contador).calcularTotalPago());
            valorTotalImoveis += valorImovel;
            valorTotalFinanciamentos += listaFinanciamentos.get(contador).calcularTotalPago();

            System.out.printf("Simulando o financiamento do %d° apartamento...\n", contador+1);
            listaFinanciamentos.add(new Casa(valorImovel, prazoAnos, juroAnual));
            System.out.printf("Pagamento mensal do apartamento financiada: %.2f R$\n", listaFinanciamentos.get(contador+1).calcularPagamentoMensal());
            System.out.printf("Pagamento total do financiamento da apartamento: %.2f R$\n\n", listaFinanciamentos.get(contador+1).calcularTotalPago());
            valorTotalImoveis += valorImovel;
            valorTotalFinanciamentos += listaFinanciamentos.get(contador+1).calcularTotalPago();
            try {
                // Delay de 2 segundos (2000 milissegundos)
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                // Tratar a exceção caso a thread seja interrompida
                System.out.println("A pausa foi interrompida!");
            }

            System.out.printf("Simulando o financiamento do %d° terreno...\n", contador+2);
            listaFinanciamentos.add(new Casa(valorImovel, prazoAnos, juroAnual));
            System.out.printf("Pagamento mensal do terreno financiado: %.2f R$\n", listaFinanciamentos.get(contador+2).calcularPagamentoMensal());
            System.out.printf("Pagamento total do financiamento do terreno: %.2f R$\n\n", listaFinanciamentos.get(contador+2).calcularTotalPago());
            valorTotalImoveis += valorImovel;
            valorTotalFinanciamentos += listaFinanciamentos.get(contador+2).calcularTotalPago();
            try {
                // Delay de 2 segundos (2000 milissegundos)
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                // Tratar a exceção caso a thread seja interrompida
                System.out.println("A pausa foi interrompida!");
            }

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