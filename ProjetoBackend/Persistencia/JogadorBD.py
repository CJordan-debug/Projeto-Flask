from Modelo.Jogador import Jogador
import sqlite3

caminhoBancoDados = './BancoDeDados/Dados.db'

class JogadorBD(object):
    
    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDados)
        with self.__conexao as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Jogador(
                    id integer not null primary key autoincrement,
                    nome text not null,
                    dataNasc text not null,
                    apelido text not null
                )
            """)
            conn.commit()

    def incluir(self, jogador):
        if isinstance(jogador,Jogador):
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO jogador(nome, dataNasc, apelido) 
                    values (?,?,?)
                """, (jogador.nome, jogador.dataNasc, jogador.apelido))
                jogador.id = cursor.lastrowid        
                conn.commit()

    def apagar(self, jogador):
        if isinstance(jogador, Jogador):
            with self.__conexao as conn:
                conn.execute("""
                    DELETE FROM jogador WHERE id = ?
                """,[jogador.id])
                conn.commit()    

    def atualizar(self, jogador):
        if isinstance(jogador,Jogador):
            with self.__conexao as conn:
                conn.execute("""
                    UPDATE jogador Set nome = ?, dataNasc = ?, apelido = ? 
                    WHERE jogador.id == ?
                """, (jogador.nome, jogador.dataNasc, jogador.apelido, jogador.id))
            conn.commit()
    
    def consultar(self, termo_busca):
        if isinstance(termo_busca, int):
            #A consulta deve ser pelo id
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id,nome,dataNasc,apelido FROM jogador where id = ?
                """,[termo_busca])
                resultado = cursor.fetchone()
                if resultado:
                    jogador = Jogador(resultado[0], resultado[1], 
                    resultado[2], resultado[3])
                    return jogador
                else:
                    return None
        elif isinstance(termo_busca, str):
            with self.__conexao as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, nome, dataNasc, apelido FROM jogador WHERE nome like ?
                """, ["%" + termo_busca + "%"])
                resultados = cursor.fetchall()
                if resultados:
                    listaJogadores = []
                    for resultado in resultados:
                        jogador = Jogador(resultado[0], resultado[1], 
                        resultado[2], resultado[3])
                        listaJogadores.append(jogador)
                    return listaJogadores
                else:
                    return []
        else:
            return None


