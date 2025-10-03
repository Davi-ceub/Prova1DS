
import sqlite3 

conexao = sqlite3.connect("StarWars.db")
cursor = conexao.cursor()


def iniciar_banco():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personagem(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT UNIQUE NOT NULL,
                   classe TEXT NOT NULL,
                   ranque TEXT NOT NULL,
                   arma TEXT NOT NULL,
                   filiacao TEXT NOT NULL,
                   moralidade TEXT NOT NULL                         
 )
    """)
    conexao.commit()

def inserir_personagem(nome, classe, ranque, arma, filiacao, moralidade):
    try:
        cursor.execute("INSERT INTO personagem (nome, classe, ranque, arma, filiacao, moralidade) VALUES (?, ?, ?, ?, ?, ?)", 
                           (nome, classe, ranque, arma, filiacao, moralidade))
        conexao.commit()
        print("Personagem inserido com sucesso")
    except sqlite3.IntegrityError:
        print("Erro: Personagem já existente")

def listar_personagens():
    cursor.execute("SELECT * FROM personagem")
    personagens = cursor.fetchall()
    for personagem in personagens:
        print(personagem)

def atualizar_personagem_por_id(id_personagem, novo_nome, nova_classe, novo_ranque, nova_arma, nova_filiacao, nova_moralidade):
    cursor.execute("""
        UPDATE personagem
        SET nome = ?, classe = ?, ranque = ?, arma = ?, filiacao = ?, moralidade = ?
        WHERE id = ?
    """, (novo_nome, nova_classe, novo_ranque, nova_arma, nova_filiacao, nova_moralidade, id_personagem))
    
    if cursor.rowcount > 0:
        print("Personagem atualizado com sucesso!")
        conexao.commit()
    else:
        print("Personagem não encontrado!")

def atualizar_personagens_por_filiacao(filiacao_antiga, novo_nome, nova_classe, novo_ranque, nova_arma, nova_filiacao, nova_moralidade):
    cursor.execute("""
        UPDATE personagem
        SET nome = ?, classe = ?, ranque = ?, arma = ?, filiacao = ?, moralidade = ?
        WHERE filiacao = ?
    """, (novo_nome, nova_classe, novo_ranque, nova_arma, nova_filiacao, nova_moralidade, filiacao_antiga))
    
    if cursor.rowcount > 0:
        print("Personagens da filiacao atualizados com sucesso!")
        conexao.commit()
    else:
        print("Nenhum personagem encontrado para essa filiacao!")

def atualizar_personagem_por_moralidade(moralidade):
    cursor.execute("""
        UPDATE personagem
        SET moralidade = ?
        WHERE moralidade = ?
    """, (moralidade, moralidade))
    
    if cursor.rowcount > 0:
        print("Personagens com a moralidade atualizados com sucesso!")
        conexao.commit()
    else:
        print("Nenhum personagem encontrado para essa moralidade!")

def atualizar_personagem_por_ranque(ranque):
    cursor.execute("""
        UPDATE personagem
        SET ranque = ?
        WHERE ranque = ?
    """, (ranque, ranque))
    
    if cursor.rowcount > 0:
        print("Personagens com o ranque atualizados com sucesso!")
        conexao.commit()
    else:
        print("Nenhum personagem encontrado para esse ranque!")

def excluir_personagem_por_id(id_personagem):
    cursor.execute("DELETE FROM personagem WHERE id = ?", (id_personagem,))
    if cursor.rowcount > 0:
        print("Personagem excluído com sucesso!")
        conexao.commit()
    else:
        print("Personagem não encontrado!")

def excluir_personagens_por_filiacao(filiacao):
    cursor.execute("DELETE FROM personagem WHERE filiacao = ?", (filiacao,))
    if cursor.rowcount > 0:
        print("Personagens excluídos com sucesso!")
        conexao.commit()
    else:
        print("Nenhum personagem encontrado para essa filiacao!")

def excluir_personagens_por_moralidade(moralidade):
    cursor.execute("DELETE FROM personagem WHERE moralidade = ?", (moralidade,))
    if cursor.rowcount > 0:
        print("Personagens excluídos com sucesso!")
        conexao.commit()
    else:
        print("Nenhum personagem encontrado para essa moralidade!")

def fechar_banco():
    conexao.commit()
    conexao.close()