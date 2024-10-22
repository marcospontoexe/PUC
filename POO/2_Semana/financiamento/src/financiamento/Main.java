package financiamento;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    /*
    i. Esta é a classe principal do programa.

    ii. Ela deve conter o método main(), onde o fluxo principal do programa será implementado.

    1. Dentro do método main() vocêdeve usar os métodos da classe InterfaceUsuario para ler os dados do financiamento.

    2. Após ler os dados do financiamento, instancie um objeto do tipo Financiamento para criar este financiamento.
     */
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.printf("Hello and welcome!");

        for (int i = 1; i <= 5; i++) {
            //TIP Press <shortcut actionId="Debug"/> to start debugging your code. We have set one <icon src="AllIcons.Debugger.Db_set_breakpoint"/> breakpoint
            // for you, but you can always add more by pressing <shortcut actionId="ToggleLineBreakpoint"/>.
            System.out.println("i = " + i);
        }
    }
}