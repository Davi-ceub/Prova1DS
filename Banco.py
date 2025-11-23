import sqlite3

class Banco:
    def __init__(self, db_name="StarWars.db"):
        self.conexao = sqlite3.connect(db_name)
        self.cursor = self.conexao.cursor()
        self.iniciar_banco()

    def iniciar_banco(self):
        self.cursor.execute("PRAGMA foreign_keys = ON")
    
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS parceiro(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            idade INTEGER NOT NULL,
            planeta_de_origem TEXT NOT NULL
        )
        """)
    
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS personagem(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            classe TEXT NOT NULL,
            ranque TEXT NOT NULL,
            arma TEXT NOT NULL,
            filiacao TEXT NOT NULL,
            moralidade TEXT NOT NULL,
            parceiro_id INTEGER,
            FOREIGN KEY (parceiro_id) REFERENCES parceiro(id)
        )
        """)
        self.conexao.commit()

    def add_parceiro(self, nome, idade, planeta):
        try:
            self.cursor.execute(
                "INSERT INTO parceiro (nome, idade, planeta_de_origem) VALUES (?, ?, ?)",
                (nome, idade, planeta)
            )
            self.conexao.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def listar_parceiros(self):
        self.cursor.execute("SELECT * FROM parceiro")
        return self.cursor.fetchall()

    def atualizar_parceiro(self, id, nome, idade, planeta):
        self.cursor.execute(
            "UPDATE parceiro SET nome=?, idade=?, planeta_de_origem=? WHERE id=?",
            (nome, idade, planeta, id)
        )
        self.conexao.commit()

    def deletar_parceiro(self, id):
        self.cursor.execute("DELETE FROM parceiro WHERE id=?", (id,))
        self.conexao.commit()


    def add_personagem(self, nome, classe, ranque, arma, filiacao, moralidade, parceiro_id):
        try:
            self.cursor.execute(
                "INSERT INTO personagem (nome, classe, ranque, arma, filiacao, moralidade, parceiro_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (nome, classe, ranque, arma, filiacao, moralidade, parceiro_id)
            )
            self.conexao.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def listar_personagens(self):
        self.cursor.execute("""
        SELECT personagem.id, personagem.nome, personagem.classe, personagem.ranque, personagem.arma,
               personagem.filiacao, personagem.moralidade, parceiro.nome
        FROM personagem
        LEFT JOIN parceiro ON personagem.parceiro_id = parceiro.id
        """)
        return self.cursor.fetchall()

    def atualizar_personagem(self, id, nome, classe, ranque, arma, filiacao, moralidade, parceiro_id):
        self.cursor.execute("""
        UPDATE personagem SET nome=?, classe=?, ranque=?, arma=?, filiacao=?, moralidade=?, parceiro_id=?
        WHERE id=?
        """, (nome, classe, ranque, arma, filiacao, moralidade, parceiro_id, id))
        self.conexao.commit()

    def deletar_personagem(self, id):
        self.cursor.execute("DELETE FROM personagem WHERE id=?", (id,))
        self.conexao.commit()

    def fechar_banco(self):
        self.conexao.commit()
        self.conexao.close()
