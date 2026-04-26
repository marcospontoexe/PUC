"""Banco de dados simulado com SQLite para o AtendeBot."""

import os
import random
import sqlite3
from datetime import datetime, timedelta


DB_PATH = os.path.join(os.path.dirname(__file__), "teleconecta.db")


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Cria as tabelas e popula com dados simulados."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            email TEXT,
            telefone TEXT
        );

        CREATE TABLE IF NOT EXISTS planos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            velocidade TEXT,
            franquia_dados TEXT,
            preco REAL NOT NULL,
            descricao TEXT
        );

        CREATE TABLE IF NOT EXISTS contratos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            plano_id INTEGER NOT NULL,
            data_inicio TEXT NOT NULL,
            status TEXT DEFAULT 'ativo',
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (plano_id) REFERENCES planos(id)
        );

        CREATE TABLE IF NOT EXISTS faturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contrato_id INTEGER NOT NULL,
            mes_referencia INTEGER NOT NULL,
            ano_referencia INTEGER NOT NULL,
            valor REAL NOT NULL,
            vencimento TEXT NOT NULL,
            status TEXT DEFAULT 'pendente',
            codigo_barras TEXT,
            FOREIGN KEY (contrato_id) REFERENCES contratos(id)
        );

        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            tipo_servico TEXT NOT NULL,
            tipo_problema TEXT NOT NULL,
            descricao TEXT,
            protocolo TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'aberto',
            data_abertura TEXT NOT NULL,
            previsao_resolucao TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
    """)

    cursor.execute("SELECT COUNT(*) FROM clientes")
    if cursor.fetchone()[0] == 0:
        _seed_data(cursor)

    conn.commit()
    conn.close()


def _seed_data(cursor: sqlite3.Cursor):
    """Popula o banco com dados fictícios para demonstração."""
    planos = [
        ("Básico Móvel", "celular", None, "5GB", 39.90,
         "Ligações ilimitadas + 5GB de internet"),
        ("Essencial Móvel", "celular", None, "15GB", 59.90,
         "Ligações ilimitadas + 15GB de internet + apps de mensagem ilimitados"),
        ("Premium Móvel", "celular", None, "50GB", 99.90,
         "Ligações ilimitadas + 50GB de internet + apps ilimitados + roaming nacional"),
        ("Fibra 100", "internet", "100 Mbps", None, 89.90,
         "Internet fibra óptica 100 Mbps + Wi-Fi 5"),
        ("Fibra 300", "internet", "300 Mbps", None, 119.90,
         "Internet fibra óptica 300 Mbps + Wi-Fi 6"),
        ("Fibra 500", "internet", "500 Mbps", None, 149.90,
         "Internet fibra óptica 500 Mbps + Wi-Fi 6 + IP fixo"),
        ("TV Essencial", "tv", None, None, 69.90,
         "80 canais incluindo HD + 3 telas simultâneas"),
        ("TV Premium", "tv", None, None, 119.90,
         "150 canais + canais premium (HBO, Telecine) + 5 telas"),
        ("Combo Família", "combo", "300 Mbps", "30GB", 199.90,
         "Fibra 300 + Essencial Móvel + TV Essencial"),
    ]
    cursor.executemany(
        "INSERT INTO planos (nome, tipo, velocidade, franquia_dados, preco, descricao) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        planos,
    )

    clientes = [
        ("12345678901", "Maria Silva", "maria@email.com", "(11) 99999-1234"),
        ("98765432100", "João Santos", "joao@email.com", "(21) 98888-5678"),
        ("11122233344", "Ana Oliveira", "ana@email.com", "(31) 97777-9012"),
        ("55566677788", "Carlos Pereira", "carlos@email.com", "(41) 96666-3456"),
        ("99988877766", "Patrícia Costa", "patricia@email.com", "(51) 95555-7890"),
    ]
    cursor.executemany(
        "INSERT INTO clientes (cpf, nome, email, telefone) VALUES (?, ?, ?, ?)",
        clientes,
    )

    contratos_data = [
        (1, 2, "2024-03-15"),  # Maria - Essencial Móvel
        (1, 5, "2024-03-15"),  # Maria - Fibra 300
        (2, 3, "2023-11-01"),  # João - Premium Móvel
        (3, 9, "2024-01-10"),  # Ana - Combo Família
        (4, 4, "2024-06-20"),  # Carlos - Fibra 100
        (5, 1, "2024-08-05"),  # Patrícia - Básico Móvel
    ]
    cursor.executemany(
        "INSERT INTO contratos (cliente_id, plano_id, data_inicio) VALUES (?, ?, ?)",
        contratos_data,
    )

    now = datetime.now()
    for contrato_id in range(1, 7):
        for months_back in range(3):
            ref_date = now - timedelta(days=30 * months_back)
            mes = ref_date.month
            ano = ref_date.year
            vencimento = ref_date.replace(day=10).strftime("%Y-%m-%d")

            cursor.execute(
                "SELECT p.preco FROM planos p "
                "JOIN contratos c ON c.plano_id = p.id "
                "WHERE c.id = ?",
                (contrato_id,),
            )
            row = cursor.fetchone()
            valor = row[0] if row else 99.90

            status = "pago" if months_back > 0 else random.choice(["pendente", "pago"])
            barcode = f"23793.{random.randint(10000,99999)} {random.randint(10000,99999)}.{random.randint(100000,999999)} {random.randint(1,9)} {random.randint(10000000,99999999)}"

            cursor.execute(
                "INSERT INTO faturas (contrato_id, mes_referencia, ano_referencia, valor, vencimento, status, codigo_barras) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (contrato_id, mes, ano, valor, vencimento, status, barcode),
            )


def buscar_cliente_por_cpf(cpf: str) -> dict | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def buscar_planos_cliente(cliente_id: int) -> list[dict]:
    conn = get_connection()
    rows = conn.execute(
        "SELECT p.*, c.data_inicio, c.status as contrato_status "
        "FROM planos p "
        "JOIN contratos c ON c.plano_id = p.id "
        "WHERE c.cliente_id = ? AND c.status = 'ativo'",
        (cliente_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def buscar_faturas_cliente(cliente_id: int, mes: int | None = None) -> list[dict]:
    conn = get_connection()
    if mes:
        rows = conn.execute(
            "SELECT f.*, p.nome as plano_nome "
            "FROM faturas f "
            "JOIN contratos c ON c.id = f.contrato_id "
            "JOIN planos p ON p.id = c.plano_id "
            "WHERE c.cliente_id = ? AND f.mes_referencia = ? "
            "ORDER BY f.ano_referencia DESC, f.mes_referencia DESC",
            (cliente_id, mes),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT f.*, p.nome as plano_nome "
            "FROM faturas f "
            "JOIN contratos c ON c.id = f.contrato_id "
            "JOIN planos p ON p.id = c.plano_id "
            "WHERE c.cliente_id = ? "
            "ORDER BY f.ano_referencia DESC, f.mes_referencia DESC "
            "LIMIT 6",
            (cliente_id,),
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def buscar_planos_upgrade(tipo: str | None = None) -> list[dict]:
    conn = get_connection()
    if tipo:
        rows = conn.execute(
            "SELECT * FROM planos WHERE tipo = ? ORDER BY preco",
            (tipo,),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM planos ORDER BY tipo, preco"
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def criar_chamado(
    cliente_id: int,
    tipo_servico: str,
    tipo_problema: str,
    descricao: str,
) -> dict:
    protocolo = f"TC{datetime.now().strftime('%Y%m%d')}{random.randint(1000, 9999)}"
    data_abertura = datetime.now().strftime("%Y-%m-%d %H:%M")
    previsao = (datetime.now() + timedelta(hours=random.choice([24, 48, 72]))).strftime(
        "%Y-%m-%d %H:%M"
    )

    conn = get_connection()
    conn.execute(
        "INSERT INTO chamados (cliente_id, tipo_servico, tipo_problema, descricao, protocolo, data_abertura, previsao_resolucao) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (cliente_id, tipo_servico, tipo_problema, descricao, protocolo, data_abertura, previsao),
    )
    conn.commit()
    conn.close()

    return {
        "protocolo": protocolo,
        "data_abertura": data_abertura,
        "previsao_resolucao": previsao,
        "status": "aberto",
    }


def gerar_segunda_via(contrato_id: int) -> dict:
    """Simula a geração de segunda via de boleto."""
    barcode = f"23793.{random.randint(10000,99999)} {random.randint(10000,99999)}.{random.randint(100000,999999)} {random.randint(1,9)} {random.randint(10000000,99999999)}"
    link = f"https://teleconecta.com.br/boleto/{random.randint(100000, 999999)}"
    return {
        "link": link,
        "codigo_barras": barcode,
        "validade": (datetime.now() + timedelta(days=3)).strftime("%d/%m/%Y"),
    }
