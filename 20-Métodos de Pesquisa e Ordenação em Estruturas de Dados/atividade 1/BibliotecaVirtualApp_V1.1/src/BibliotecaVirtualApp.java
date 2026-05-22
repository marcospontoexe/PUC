import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.Iterator;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.charset.StandardCharsets;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BibliotecaVirtualApp {

    static class Livro {
        String titulo;
        String autor;
        String genero;
        int anoPublicacao;
        boolean emprestado;

        public Livro(String titulo, String autor, String genero, int anoPublicacao) {
            this.titulo = titulo;
            this.autor = autor;
            this.genero = genero;
            this.anoPublicacao = anoPublicacao;
            this.emprestado = false;
        }
    }

    static class Biblioteca {
        private LinkedList<Livro> livros = new LinkedList<>();
        private Map<String, Queue<String>> filasEspera = new HashMap<>();
        private Stack<String> historicoNavegacao = new Stack<>();

        private String normalizar(String texto) {
            return texto == null ? "" : texto.trim().toLowerCase();
        }

        private Livro encontrarLivro(String titulo) {
            for (Livro livro : livros) {
                if (livro.titulo.equalsIgnoreCase(titulo)) {
                    return livro;
                }
            }
            return null;
        }

        private Queue<String> obterFila(String titulo) {
            String chave = normalizar(titulo);
            return filasEspera.computeIfAbsent(chave, k -> new LinkedList<>());
        }

        private void registrarVisualizacao(Livro livro) {
            historicoNavegacao.push(
                    livro.titulo + " | " + livro.autor + " | " + livro.genero + " | " + livro.anoPublicacao
            );
        }

        public boolean existeLivroComTitulo(String titulo) {
            return encontrarLivro(titulo) != null;
        }

        public boolean adicionarLivro(String titulo, String autor, String genero, int anoPublicacao, String caminhoArquivo) {
            if (existeLivroComTitulo(titulo)) {
                System.out.println("Já existe um livro com esse título. Cadastro não realizado.");
                return false;
            }

            livros.add(new Livro(titulo, autor, genero, anoPublicacao));
            salvarEmJson(caminhoArquivo);
            System.out.println("Livro cadastrado e salvo com sucesso!");
            return true;
        }

        public void listarLivros() {
            if (livros.isEmpty()) {
                System.out.println("A biblioteca está vazia.");
                return;
            }

            System.out.println("\n===== LISTA DE LIVROS =====");
            for (Livro livro : livros) {
                System.out.println("Título: " + livro.titulo);
                System.out.println("Autor: " + livro.autor);
                System.out.println("Gênero: " + livro.genero);
                System.out.println("Ano: " + livro.anoPublicacao);
                System.out.println("Status: " + (livro.emprestado ? "Emprestado" : "Disponível"));
                System.out.println("--------------------------");
            }
        }

        public void listarLivrosPorGenero(String generoBusca) {
            boolean encontrou = false;

            System.out.println("\n===== LIVROS DO GÊNERO: " + generoBusca + " =====");

            for (Livro livro : livros) {
                if (livro.genero.equalsIgnoreCase(generoBusca)) {
                    System.out.println("Título: " + livro.titulo);
                    System.out.println("Autor: " + livro.autor);
                    System.out.println("Ano: " + livro.anoPublicacao);
                    System.out.println("Status: " + (livro.emprestado ? "Emprestado" : "Disponível"));
                    System.out.println("--------------------------");
                    encontrou = true;
                }
            }

            if (!encontrou) {
                System.out.println("Nenhum livro encontrado para este gênero.");
            }
        }

        public void buscarLivro(String titulo) {
            Livro livro = encontrarLivro(titulo);

            if (livro != null) {
                registrarVisualizacao(livro);

                System.out.println("\nLivro encontrado!");
                System.out.println("Título: " + livro.titulo);
                System.out.println("Autor: " + livro.autor);
                System.out.println("Gênero: " + livro.genero);
                System.out.println("Ano: " + livro.anoPublicacao);
                System.out.println("Status: " + (livro.emprestado ? "Emprestado" : "Disponível"));
            } else {
                System.out.println("Livro não encontrado.");
            }
        }

        public void removerLivro(String titulo, String caminhoArquivo) {
            Iterator<Livro> iterator = livros.iterator();

            while (iterator.hasNext()) {
                Livro livro = iterator.next();
                if (livro.titulo.equalsIgnoreCase(titulo)) {
                    iterator.remove();
                    filasEspera.remove(normalizar(titulo));
                    salvarEmJson(caminhoArquivo);
                    System.out.println("Livro removido e alterações salvas com sucesso!");
                    return;
                }
            }

            System.out.println("Livro não encontrado.");
        }

        public void emprestarLivro(String titulo, String caminhoArquivo) {
            Livro livro = encontrarLivro(titulo);

            if (livro == null) {
                System.out.println("Livro não encontrado.");
                return;
            }

            if (livro.emprestado) {
                System.out.println("Livro já está emprestado.");
                return;
            }

            livro.emprestado = true;
            salvarEmJson(caminhoArquivo);
            System.out.println("Livro emprestado com sucesso!");
        }

        public void devolverLivro(String titulo, String caminhoArquivo) {
            Livro livro = encontrarLivro(titulo);

            if (livro == null) {
                System.out.println("Livro não encontrado.");
                return;
            }

            if (!livro.emprestado) {
                System.out.println("Este livro já está disponível.");
                return;
            }

            Queue<String> fila = obterFila(titulo);

            if (!fila.isEmpty()) {
                String proximoUsuario = fila.poll();
                System.out.println("Livro devolvido e automaticamente reservado para o próximo da fila: " + proximoUsuario);
                livro.emprestado = true;
            } else {
                livro.emprestado = false;
                System.out.println("Livro devolvido com sucesso! Agora ele está disponível.");
            }

            salvarEmJson(caminhoArquivo);
        }

        public void entrarNaFilaDeEspera(String titulo, String nomeUsuario) {
            Livro livro = encontrarLivro(titulo);

            if (livro == null) {
                System.out.println("Livro não encontrado.");
                return;
            }

            if (!livro.emprestado) {
                System.out.println("Este livro está disponível. Não há necessidade de entrar na fila.");
                return;
            }

            Queue<String> fila = obterFila(titulo);

            if (fila.contains(nomeUsuario)) {
                System.out.println("Este usuário já está na fila de espera para este livro.");
                return;
            }

            fila.offer(nomeUsuario);
            System.out.println("Usuário adicionado à fila de espera com sucesso.");

            int posicao = 1;
            for (String usuario : fila) {
                if (usuario.equalsIgnoreCase(nomeUsuario)) {
                    break;
                }
                posicao++;
            }

            System.out.println("Posição na fila: " + posicao);
        }

        public void mostrarFilaDeEspera(String titulo) {
            Queue<String> fila = filasEspera.get(normalizar(titulo));

            if (fila == null || fila.isEmpty()) {
                System.out.println("Não há fila de espera para este livro.");
                return;
            }

            System.out.println("\n===== FILA DE ESPERA DE: " + titulo + " =====");
            int posicao = 1;

            for (String usuario : fila) {
                System.out.println(posicao + " - " + usuario);
                posicao++;
            }
        }

        public void mostrarHistoricoNavegacao() {
            if (historicoNavegacao.isEmpty()) {
                System.out.println("Histórico vazio.");
                return;
            }

            System.out.println("\n===== HISTÓRICO DE NAVEGAÇÃO =====");

            for (int i = historicoNavegacao.size() - 1; i >= 0; i--) {
                System.out.println((historicoNavegacao.size() - i) + " - " + historicoNavegacao.get(i));
            }
        }

        public void salvarEmJson(String caminhoArquivo) {
            StringBuilder json = new StringBuilder();
            json.append("[\n");

            for (int i = 0; i < livros.size(); i++) {
                Livro livro = livros.get(i);

                json.append("  {\n");
                json.append("    \"titulo\": \"").append(escapeJson(livro.titulo)).append("\",\n");
                json.append("    \"autor\": \"").append(escapeJson(livro.autor)).append("\",\n");
                json.append("    \"genero\": \"").append(escapeJson(livro.genero)).append("\",\n");
                json.append("    \"anoPublicacao\": ").append(livro.anoPublicacao).append(",\n");
                json.append("    \"emprestado\": ").append(livro.emprestado).append("\n");
                json.append("  }");

                if (i < livros.size() - 1) {
                    json.append(",");
                }

                json.append("\n");
            }

            json.append("]");

            try {
                Files.writeString(Path.of(caminhoArquivo), json.toString(), StandardCharsets.UTF_8);
            } catch (IOException e) {
                System.out.println("Erro ao salvar JSON: " + e.getMessage());
            }
        }

        public void carregarDeJson(String caminhoArquivo) {
            try {
                Path path = Path.of(caminhoArquivo);

                if (!Files.exists(path)) {
                    System.out.println("Arquivo JSON não encontrado. Biblioteca iniciada vazia.");
                    return;
                }

                String conteudo = Files.readString(path);
                livros.clear();

                Pattern pattern = Pattern.compile(
                        "\\{\\s*\"titulo\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"autor\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"genero\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"anoPublicacao\"\\s*:\\s*(-?\\d+)\\s*,\\s*\"emprestado\"\\s*:\\s*(true|false)\\s*\\}",
                        Pattern.DOTALL
                );

                Matcher matcher = pattern.matcher(conteudo);

                while (matcher.find()) {
                    String titulo = unescapeJson(matcher.group(1));
                    String autor = unescapeJson(matcher.group(2));
                    String genero = unescapeJson(matcher.group(3));
                    int ano = Integer.parseInt(matcher.group(4));
                    boolean emprestado = Boolean.parseBoolean(matcher.group(5));

                    Livro livro = new Livro(titulo, autor, genero, ano);
                    livro.emprestado = emprestado;
                    livros.add(livro);
                }

                System.out.println("Livros carregados do JSON com sucesso!");
            } catch (IOException e) {
                System.out.println("Erro ao carregar JSON: " + e.getMessage());
            }
        }

        private String escapeJson(String texto) {
            if (texto == null) {
                return "";
            }
            return texto.replace("\\", "\\\\").replace("\"", "\\\"");
        }

        private String unescapeJson(String texto) {
            if (texto == null) {
                return "";
            }
            return texto.replace("\\\"", "\"").replace("\\\\", "\\");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Biblioteca biblioteca = new Biblioteca();
        String arquivoJson = "livros_biblioteca.json";

        biblioteca.carregarDeJson(arquivoJson);

        int opcao;

        do {
            System.out.println("\n===== BIBLIOTECA VIRTUAL =====");
            System.out.println("1 - Cadastrar livro");
            System.out.println("2 - Listar livros");
            System.out.println("3 - Buscar livro");
            System.out.println("4 - Remover livro");
            System.out.println("5 - Listar livros por gênero");
            System.out.println("6 - Emprestar livro");
            System.out.println("7 - Devolver livro");
            System.out.println("8 - Entrar na fila de espera");
            System.out.println("9 - Ver fila de espera de um livro");
            System.out.println("10 - Ver histórico de navegação");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            while (!scanner.hasNextInt()) {
                System.out.print("Digite um número válido: ");
                scanner.next();
            }

            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o título: ");
                    String titulo = scanner.nextLine();

                    System.out.print("Digite o autor: ");
                    String autor = scanner.nextLine();

                    System.out.print("Digite o gênero: ");
                    String genero = scanner.nextLine();

                    System.out.print("Digite o ano de publicação: ");
                    while (!scanner.hasNextInt()) {
                        System.out.print("Digite um ano válido: ");
                        scanner.next();
                    }
                    int ano = scanner.nextInt();
                    scanner.nextLine();

                    biblioteca.adicionarLivro(titulo, autor, genero, ano, arquivoJson);
                    break;

                case 2:
                    biblioteca.listarLivros();
                    break;

                case 3:
                    System.out.print("Digite o título do livro: ");
                    String tituloBusca = scanner.nextLine();
                    biblioteca.buscarLivro(tituloBusca);
                    break;

                case 4:
                    System.out.print("Digite o título do livro para remover: ");
                    String tituloRemover = scanner.nextLine();
                    biblioteca.removerLivro(tituloRemover, arquivoJson);
                    break;

                case 5:
                    System.out.print("Digite o gênero: ");
                    String generoBusca = scanner.nextLine();
                    biblioteca.listarLivrosPorGenero(generoBusca);
                    break;

                case 6:
                    System.out.print("Digite o título do livro para emprestar: ");
                    String tituloEmprestimo = scanner.nextLine();
                    biblioteca.emprestarLivro(tituloEmprestimo, arquivoJson);
                    break;

                case 7:
                    System.out.print("Digite o título do livro para devolver: ");
                    String tituloDevolucao = scanner.nextLine();
                    biblioteca.devolverLivro(tituloDevolucao, arquivoJson);
                    break;

                case 8:
                    System.out.print("Digite o título do livro: ");
                    String tituloFila = scanner.nextLine();

                    System.out.print("Digite o nome do usuário: ");
                    String nomeUsuario = scanner.nextLine();

                    biblioteca.entrarNaFilaDeEspera(tituloFila, nomeUsuario);
                    break;

                case 9:
                    System.out.print("Digite o título do livro: ");
                    String tituloFilaConsulta = scanner.nextLine();
                    biblioteca.mostrarFilaDeEspera(tituloFilaConsulta);
                    break;

                case 10:
                    biblioteca.mostrarHistoricoNavegacao();
                    break;

                case 0:
                    biblioteca.salvarEmJson(arquivoJson);
                    System.out.println("Encerrando o sistema...");
                    break;

                default:
                    System.out.println("Opção inválida!");
            }

        } while (opcao != 0);

        scanner.close();
    }
}