import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.Iterator;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.charset.StandardCharsets;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BibliotecaVirtualApp {

    enum TipoRelacao {
        SEMELHANCA,
        MESMO_GENERO,
        MESMO_AUTOR,
        RECOMENDADO
    }

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

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof Livro)) return false;

            Livro outro = (Livro) obj;

            return titulo.equalsIgnoreCase(outro.titulo);
        }

        @Override
        public int hashCode() {
            return titulo.toLowerCase().hashCode();
        }
    }

    static class EstadoDijkstra {
        Livro livro;
        int distancia;

        EstadoDijkstra(Livro livro, int distancia) {
            this.livro = livro;
            this.distancia = distancia;
        }
    }

    static class ResultadoDijkstra {
        Map<Livro, Integer> distancias = new HashMap<>();
        Map<Livro, Livro> anteriores = new HashMap<>();
    }

    static class Biblioteca {


        private LinkedList<Livro> livros = new LinkedList<>();

        private Map<String, Queue<String>> filasEspera = new HashMap<>();

        private Stack<Livro> historicoNavegacao = new Stack<>();

        private HashMap<Livro, HashMap<TipoRelacao, Set<Livro>>> grafoRelacoes = new HashMap<>();

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
            historicoNavegacao.push(livro);
        }

        private void adicionarRelacao(Livro origem, Livro destino, TipoRelacao tipo) {

            grafoRelacoes.putIfAbsent(origem, new HashMap<>());

            grafoRelacoes.get(origem).putIfAbsent(tipo, new LinkedHashSet<>());

            grafoRelacoes.get(origem).get(tipo).add(destino);
        }

        private int calcularSimilaridade(Livro a, Livro b) {

            int score = 0;

            if (a.genero.equalsIgnoreCase(b.genero)) {
                score += 3;
            }

            if (a.autor.equalsIgnoreCase(b.autor)) {
                score += 2;
            }

            int diferencaAno = Math.abs(a.anoPublicacao - b.anoPublicacao);

            if (diferencaAno <= 5) {
                score += 2;
            } else if (diferencaAno <= 15) {
                score += 1;
            }

            return score;
        }

        private void reconstruirGrafoRelacoes() {

            grafoRelacoes.clear();

            for (Livro livro : livros) {

                List<Livro> candidatos = new ArrayList<>();

                for (Livro outro : livros) {

                    if (!livro.equals(outro)) {

                        candidatos.add(outro);

                        if (livro.genero.equalsIgnoreCase(outro.genero)) {
                            adicionarRelacao(livro, outro, TipoRelacao.MESMO_GENERO);
                        }

                        if (livro.autor.equalsIgnoreCase(outro.autor)) {
                            adicionarRelacao(livro, outro, TipoRelacao.MESMO_AUTOR);
                        }

                        if (calcularSimilaridade(livro, outro) >= 3) {
                            adicionarRelacao(livro, outro, TipoRelacao.SEMELHANCA);
                        }
                    }
                }

                candidatos.sort((a, b) -> {
                    int scoreB = calcularSimilaridade(livro, b);
                    int scoreA = calcularSimilaridade(livro, a);

                    return Integer.compare(scoreB, scoreA);
                });

                int limite = Math.min(3, candidatos.size());

                for (int i = 0; i < limite; i++) {
                    adicionarRelacao(livro, candidatos.get(i), TipoRelacao.RECOMENDADO);
                }
            }
        }

        public boolean existeLivroComTitulo(String titulo) {
            return encontrarLivro(titulo) != null;
        }

        public boolean adicionarLivro(
                String titulo,
                String autor,
                String genero,
                int anoPublicacao,
                String caminhoArquivo
        ) {

            if (existeLivroComTitulo(titulo)) {

                System.out.println("Já existe um livro com esse título.");

                return false;
            }

            livros.add(new Livro(titulo, autor, genero, anoPublicacao));

            reconstruirGrafoRelacoes();

            salvarEmJson(caminhoArquivo);

            System.out.println("Livro cadastrado com sucesso!");

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
                System.out.println("Status: " +
                        (livro.emprestado ? "Emprestado" : "Disponível"));

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

                    System.out.println("--------------------------");

                    encontrou = true;
                }
            }

            if (!encontrou) {
                System.out.println("Nenhum livro encontrado.");
            }
        }

        public void buscarLivro(String titulo) {

            Livro livro = encontrarLivro(titulo);

            if (livro == null) {

                System.out.println("Livro não encontrado.");

                return;
            }

            registrarVisualizacao(livro);

            System.out.println("\n===== LIVRO ENCONTRADO =====");

            System.out.println("Título: " + livro.titulo);
            System.out.println("Autor: " + livro.autor);
            System.out.println("Gênero: " + livro.genero);
            System.out.println("Ano: " + livro.anoPublicacao);

            System.out.println("Status: " +
                    (livro.emprestado ? "Emprestado" : "Disponível"));
        }

        public void removerLivro(String titulo, String caminhoArquivo) {

            Iterator<Livro> iterator = livros.iterator();

            while (iterator.hasNext()) {

                Livro livro = iterator.next();

                if (livro.titulo.equalsIgnoreCase(titulo)) {

                    iterator.remove();

                    filasEspera.remove(normalizar(titulo));

                    reconstruirGrafoRelacoes();

                    salvarEmJson(caminhoArquivo);

                    System.out.println("Livro removido.");

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

                System.out.println("Livro já emprestado.");

                return;
            }

            livro.emprestado = true;

            salvarEmJson(caminhoArquivo);

            System.out.println("Livro emprestado.");
        }

        public void devolverLivro(String titulo, String caminhoArquivo) {

            Livro livro = encontrarLivro(titulo);

            if (livro == null) {

                System.out.println("Livro não encontrado.");

                return;
            }

            Queue<String> fila = obterFila(titulo);

            if (!fila.isEmpty()) {

                String usuario = fila.poll();

                System.out.println(
                        "Livro reservado automaticamente para: " + usuario
                );

                livro.emprestado = true;

            } else {

                livro.emprestado = false;

                System.out.println("Livro devolvido.");
            }

            salvarEmJson(caminhoArquivo);
        }

        public void entrarNaFilaDeEspera(
                String titulo,
                String usuario
        ) {

            Livro livro = encontrarLivro(titulo);

            if (livro == null) {

                System.out.println("Livro não encontrado.");

                return;
            }

            if (!livro.emprestado) {

                System.out.println("Livro disponível. Não é necessário fila.");

                return;
            }

            Queue<String> fila = obterFila(titulo);

            fila.offer(usuario);

            System.out.println("Usuário adicionado na fila.");
        }

        public void mostrarFilaDeEspera(String titulo) {

            Queue<String> fila = filasEspera.get(normalizar(titulo));

            if (fila == null || fila.isEmpty()) {

                System.out.println("Fila vazia.");

                return;
            }

            System.out.println("\n===== FILA DE ESPERA =====");

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

            System.out.println("\n===== HISTÓRICO =====");

            for (int i = historicoNavegacao.size() - 1; i >= 0; i--) {

                Livro livro = historicoNavegacao.get(i);

                System.out.println(
                        livro.titulo + " | " +
                                livro.autor + " | " +
                                livro.genero
                );
            }
        }

        public void mostrarRelacoesDoLivro(String titulo) {

            Livro livro = encontrarLivro(titulo);

            if (livro == null) {

                System.out.println("Livro não encontrado.");

                return;
            }

            Map<TipoRelacao, Set<Livro>> relacoes = grafoRelacoes.get(livro);

            if (relacoes == null || relacoes.isEmpty()) {

                System.out.println("Sem relações cadastradas.");

                return;
            }

            System.out.println(
                    "\n===== RELAÇÕES DE: " + livro.titulo + " ====="
            );

            for (TipoRelacao tipo : relacoes.keySet()) {

                System.out.println("\n" + tipo + ":");

                for (Livro relacionado : relacoes.get(tipo)) {

                    System.out.println(
                            "- " +
                                    relacionado.titulo +
                                    " | " +
                                    relacionado.autor +
                                    " | " +
                                    relacionado.genero
                    );
                }
            }
        }

        public void recomendarLivrosPorTitulo(String titulo) {

            Livro livro = encontrarLivro(titulo);

            if (livro == null) {

                System.out.println("Livro não encontrado.");

                return;
            }

            ResultadoDijkstra resultado = djikstra(livro);

            List<Map.Entry<Livro, Integer>> proximos = new ArrayList<>();

            for (Map.Entry<Livro, Integer> entrada : resultado.distancias.entrySet()) {
                if (!entrada.getKey().equals(livro)) {
                    proximos.add(entrada);
                }
            }

            proximos.sort((a, b) -> {
                int comparacao = Integer.compare(a.getValue(), b.getValue());
                if (comparacao != 0) {
                    return comparacao;
                }

                return a.getKey().titulo.compareToIgnoreCase(b.getKey().titulo);
            });

            if (proximos.isEmpty()) {

                System.out.println("Sem recomendações.");

                return;
            }

            System.out.println("\n===== RECOMENDAÇÕES PARA: " + livro.titulo + " =====");

            int limite = Math.min(3, proximos.size());

            for (int i = 0; i < limite; i++) {
                Livro recomendado = proximos.get(i).getKey();
                int distancia = proximos.get(i).getValue();

                System.out.println(
                        "- " +
                                recomendado.titulo +
                                " | distância: " +
                                distancia +
                                " | autor: " +
                                recomendado.autor +
                                " | gênero: " +
                                recomendado.genero
                );
            }
        }

        public void recomendarLivrosBaseadoNoUltimoVisualizado() {


            if (historicoNavegacao.isEmpty()) {

                System.out.println("Histórico vazio.");

                return;
            }

            Livro ultimo = historicoNavegacao.peek();

            recomendarLivrosPorTitulo(ultimo.titulo);
        }

        private int pesoDaRelacao(Livro origem, Livro destino, TipoRelacao tipo) {

            int similaridade = calcularSimilaridade(origem, destino);

            switch (tipo) {
                case MESMO_AUTOR:
                    return 1;
                case RECOMENDADO:
                    return 1;
                case SEMELHANCA:
                    if (similaridade >= 6) {
                        return 1;
                    }

                    if (similaridade >= 4) {
                        return 2;
                    }

                    return 3;
                case MESMO_GENERO:
                    return 2;
                default:
                    return 3;
            }
        }

        private Map<Livro, Integer> obterVizinhosComPesos(Livro livro) {

            Map<Livro, Integer> vizinhos = new HashMap<>();

            Map<TipoRelacao, Set<Livro>> relacoes = grafoRelacoes.get(livro);

            if (relacoes == null) {
                return vizinhos;
            }

            for (Map.Entry<TipoRelacao, Set<Livro>> entrada : relacoes.entrySet()) {

                TipoRelacao tipo = entrada.getKey();

                for (Livro vizinho : entrada.getValue()) {

                    int peso = pesoDaRelacao(livro, vizinho, tipo);

                    if (!vizinhos.containsKey(vizinho) || peso < vizinhos.get(vizinho)) {
                        vizinhos.put(vizinho, peso);
                    }
                }
            }

            return vizinhos;
        }

        private ResultadoDijkstra djikstra(Livro origem) {

            ResultadoDijkstra resultado = new ResultadoDijkstra();

            PriorityQueue<EstadoDijkstra> fila = new PriorityQueue<>(
                    Comparator.comparingInt(estado -> estado.distancia)
            );

            resultado.distancias.put(origem, 0);
            fila.add(new EstadoDijkstra(origem, 0));

            while (!fila.isEmpty()) {

                EstadoDijkstra estadoAtual = fila.poll();
                Livro atual = estadoAtual.livro;
                int distanciaAtual = estadoAtual.distancia;

                if (distanciaAtual != resultado.distancias.getOrDefault(atual, Integer.MAX_VALUE)) {
                    continue;
                }

                Map<Livro, Integer> vizinhos = obterVizinhosComPesos(atual);

                for (Map.Entry<Livro, Integer> entrada : vizinhos.entrySet()) {

                    Livro vizinho = entrada.getKey();
                    int novaDistancia = distanciaAtual + entrada.getValue();

                    if (novaDistancia < resultado.distancias.getOrDefault(vizinho, Integer.MAX_VALUE)) {
                        resultado.distancias.put(vizinho, novaDistancia);
                        resultado.anteriores.put(vizinho, atual);
                        fila.add(new EstadoDijkstra(vizinho, novaDistancia));
                    }
                }
            }

            return resultado;
        }

        private List<Livro> reconstruirCaminho(
                Livro origem,
                Livro destino,
                Map<Livro, Livro> anteriores
        ) {

            LinkedList<Livro> caminho = new LinkedList<>();
            Livro atual = destino;

            while (atual != null) {
                caminho.addFirst(atual);

                if (atual.equals(origem)) {
                    break;
                }

                atual = anteriores.get(atual);
            }

            if (caminho.isEmpty() || !caminho.getFirst().equals(origem)) {
                return new ArrayList<>();
            }

            return caminho;
        }

        private String formatarCaminho(List<Livro> caminho) {

            if (caminho == null || caminho.isEmpty()) {
                return "sem caminho";
            }

            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < caminho.size(); i++) {
                sb.append(caminho.get(i).titulo);

                if (i < caminho.size() - 1) {
                    sb.append(" -> ");
                }
            }

            return sb.toString();
        }

        public void mostrarLivrosMaisProximosPorTitulo(String titulo) {

            Livro livro = encontrarLivro(titulo);

            if (livro == null) {

                System.out.println("Livro não encontrado.");

                return;
            }

            ResultadoDijkstra resultado = djikstra(livro);

            List<Map.Entry<Livro, Integer>> proximos = new ArrayList<>();

            for (Map.Entry<Livro, Integer> entrada : resultado.distancias.entrySet()) {
                if (!entrada.getKey().equals(livro)) {
                    proximos.add(entrada);
                }
            }

            proximos.sort((a, b) -> {
                int comparacao = Integer.compare(a.getValue(), b.getValue());
                if (comparacao != 0) {
                    return comparacao;
                }

                return a.getKey().titulo.compareToIgnoreCase(b.getKey().titulo);
            });

            if (proximos.isEmpty()) {

                System.out.println("Sem livros relacionados.");

                return;
            }

            System.out.println("\n===== LIVROS MAIS PRÓXIMOS DE: " + livro.titulo + " =====");

            for (Map.Entry<Livro, Integer> entrada : proximos) {

                Livro destino = entrada.getKey();
                int distancia = entrada.getValue();

                List<Livro> caminho = reconstruirCaminho(
                        livro,
                        destino,
                        resultado.anteriores
                );

                System.out.println(
                        "- " +
                                destino.titulo +
                                " | distância: " +
                                distancia +
                                " | caminho: " +
                                formatarCaminho(caminho)
                );
            }
        }

        public void salvarEmJson(String caminhoArquivo) {


            StringBuilder json = new StringBuilder();

            json.append("[\n");

            for (int i = 0; i < livros.size(); i++) {

                Livro livro = livros.get(i);

                json.append("  {\n");

                json.append("    \"titulo\": \"")
                        .append(escapeJson(livro.titulo))
                        .append("\",\n");

                json.append("    \"autor\": \"")
                        .append(escapeJson(livro.autor))
                        .append("\",\n");

                json.append("    \"genero\": \"")
                        .append(escapeJson(livro.genero))
                        .append("\",\n");

                json.append("    \"anoPublicacao\": ")
                        .append(livro.anoPublicacao)
                        .append(",\n");

                json.append("    \"emprestado\": ")
                        .append(livro.emprestado)
                        .append("\n");

                json.append("  }");

                if (i < livros.size() - 1) {
                    json.append(",");
                }

                json.append("\n");
            }

            json.append("]");

            try {

                Files.writeString(
                        Path.of(caminhoArquivo),
                        json.toString(),
                        StandardCharsets.UTF_8
                );

            } catch (IOException e) {

                System.out.println(
                        "Erro ao salvar JSON: " + e.getMessage()
                );
            }
        }

        public void carregarDeJson(String caminhoArquivo) {

            try {

                Path path = Path.of(caminhoArquivo);

                if (!Files.exists(path)) {

                    System.out.println(
                            "Arquivo JSON não encontrado."
                    );

                    return;
                }

                String conteudo = Files.readString(path);

                livros.clear();

                Pattern pattern = Pattern.compile(
                        "\\{\\s*\"titulo\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"autor\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"genero\"\\s*:\\s*\"(.*?)\"\\s*,\\s*\"anoPublicacao\"\\s*:\\s*(-?\\d+)(?:\\s*,\\s*\"emprestado\"\\s*:\\s*(true|false))?\\s*\\}",
                        Pattern.DOTALL
                );

                Matcher matcher = pattern.matcher(conteudo);

                while (matcher.find()) {

                    String titulo = unescapeJson(matcher.group(1));

                    String autor = unescapeJson(matcher.group(2));

                    String genero = unescapeJson(matcher.group(3));

                    int ano = Integer.parseInt(matcher.group(4));

                    boolean emprestado = false;

                    if (matcher.group(5) != null) {
                        emprestado = Boolean.parseBoolean(
                                matcher.group(5)
                        );
                    }

                    Livro livro =
                            new Livro(titulo, autor, genero, ano);

                    livro.emprestado = emprestado;

                    livros.add(livro);
                }

                reconstruirGrafoRelacoes();

                System.out.println("Livros carregados!");

            } catch (IOException e) {

                System.out.println(
                        "Erro ao carregar JSON: " + e.getMessage()
                );
            }
        }

        private String escapeJson(String texto) {

            if (texto == null) {
                return "";
            }

            return texto
                    .replace("\\", "\\\\")
                    .replace("\"", "\\\"");
        }

        private String unescapeJson(String texto) {

            if (texto == null) {
                return "";
            }

            return texto
                    .replace("\\\"", "\"")
                    .replace("\\\\", "\\");
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
            System.out.println("9 - Ver fila de espera");
            System.out.println("10 - Ver histórico");
            System.out.println("11 - Ver relações do livro");
            System.out.println("12 - Recomendar livros");
            System.out.println("13 - Recomendar pelo último visualizado");
            System.out.println("14 - Ver livros mais próximos (Dijkstra)");
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

                    System.out.print("Título: ");
                    String titulo = scanner.nextLine();

                    System.out.print("Autor: ");
                    String autor = scanner.nextLine();

                    System.out.print("Gênero: ");
                    String genero = scanner.nextLine();

                    System.out.print("Ano: ");

                    while (!scanner.hasNextInt()) {

                        System.out.print("Digite um ano válido: ");

                        scanner.next();
                    }

                    int ano = scanner.nextInt();

                    scanner.nextLine();

                    biblioteca.adicionarLivro(
                            titulo,
                            autor,
                            genero,
                            ano,
                            arquivoJson
                    );

                    break;

                case 2:

                    biblioteca.listarLivros();

                    break;

                case 3:

                    System.out.print("Título do livro: ");

                    biblioteca.buscarLivro(scanner.nextLine());

                    break;

                case 4:

                    System.out.print("Título do livro: ");

                    biblioteca.removerLivro(
                            scanner.nextLine(),
                            arquivoJson
                    );

                    break;

                case 5:

                    System.out.print("Gênero: ");

                    biblioteca.listarLivrosPorGenero(
                            scanner.nextLine()
                    );

                    break;

                case 6:

                    System.out.print("Título do livro: ");

                    biblioteca.emprestarLivro(
                            scanner.nextLine(),
                            arquivoJson
                    );

                    break;

                case 7:

                    System.out.print("Título do livro: ");

                    biblioteca.devolverLivro(
                            scanner.nextLine(),
                            arquivoJson
                    );

                    break;

                case 8:

                    System.out.print("Título do livro: ");
                    String tituloFila = scanner.nextLine();

                    System.out.print("Usuário: ");
                    String usuario = scanner.nextLine();

                    biblioteca.entrarNaFilaDeEspera(
                            tituloFila,
                            usuario
                    );

                    break;

                case 9:

                    System.out.print("Título do livro: ");

                    biblioteca.mostrarFilaDeEspera(
                            scanner.nextLine()
                    );

                    break;

                case 10:

                    biblioteca.mostrarHistoricoNavegacao();

                    break;

                case 11:

                    System.out.print("Título do livro: ");

                    biblioteca.mostrarRelacoesDoLivro(
                            scanner.nextLine()
                    );

                    break;

                case 12:

                    System.out.print("Título do livro: ");

                    biblioteca.recomendarLivrosPorTitulo(
                            scanner.nextLine()
                    );

                    break;

                case 13:

                    biblioteca.recomendarLivrosBaseadoNoUltimoVisualizado();

                    break;

                case 14:

                    System.out.print("Título do livro: ");

                    biblioteca.mostrarLivrosMaisProximosPorTitulo(
                            scanner.nextLine()
                    );

                    break;

                case 0:

                    biblioteca.salvarEmJson(arquivoJson);

                    System.out.println("Encerrando sistema...");

                    break;

                default:

                    System.out.println("Opção inválida.");
            }

        } while (opcao != 0);

        scanner.close();
    }
}