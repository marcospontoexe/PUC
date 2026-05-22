import java.util.LinkedList;
import java.util.Scanner;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.charset.StandardCharsets;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Iterator;

public class BibliotecaVirtualApp {

    static class Livro {
        String titulo;
        String autor;
        String genero;
        int anoPublicacao;

        public Livro(String titulo, String autor, String genero, int anoPublicacao) {
            this.titulo = titulo;
            this.autor = autor;
            this.genero = genero;
            this.anoPublicacao = anoPublicacao;
        }
    }

    static class Biblioteca {
        private LinkedList<Livro> livros = new LinkedList<>();

        public boolean existeLivroComTitulo(String titulo) {
            for (Livro livro : livros) {
                if (livro.titulo.equalsIgnoreCase(titulo)) {
                    return true;
                }
            }
            return false;
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
                System.out.println("--------------------------");
            }
        }

        public void buscarLivro(String titulo) {
            for (Livro livro : livros) {
                if (livro.titulo.equalsIgnoreCase(titulo)) {
                    System.out.println("\nLivro encontrado!");
                    System.out.println("Título: " + livro.titulo);
                    System.out.println("Autor: " + livro.autor);
                    System.out.println("Gênero: " + livro.genero);
                    System.out.println("Ano: " + livro.anoPublicacao);
                    return;
                }
            }
            System.out.println("Livro não encontrado.");
        }

        public void removerLivro(String titulo, String caminhoArquivo) {
            Iterator<Livro> iterator = livros.iterator();

            while (iterator.hasNext()) {
                Livro livro = iterator.next();
                if (livro.titulo.equalsIgnoreCase(titulo)) {
                    iterator.remove();
                    salvarEmJson(caminhoArquivo);
                    System.out.println("Livro removido e alterações salvas com sucesso!");
                    return;
                }
            }

            System.out.println("Livro não encontrado.");
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
                json.append("    \"anoPublicacao\": ").append(livro.anoPublicacao).append("\n");
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
                        "\\{\\s*\"titulo\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"autor\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"genero\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"anoPublicacao\"\\s*:\\s*(-?\\d+)\\s*\\}"
                );

                Matcher matcher = pattern.matcher(conteudo);

                while (matcher.find()) {
                    String titulo = unescapeJson(matcher.group(1));
                    String autor = unescapeJson(matcher.group(2));
                    String genero = unescapeJson(matcher.group(3));
                    int ano = Integer.parseInt(matcher.group(4));

                    livros.add(new Livro(titulo, autor, genero, ano));
                }

                System.out.println("Livros carregados do JSON com sucesso!");
            } catch (IOException e) {
                System.out.println("Erro ao carregar JSON: " + e.getMessage());
            }
        }

        private String escapeJson(String texto) {
            if (texto == null) return "";
            return texto.replace("\\", "\\\\").replace("\"", "\\\"");
        }

        private String unescapeJson(String texto) {
            if (texto == null) return "";
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