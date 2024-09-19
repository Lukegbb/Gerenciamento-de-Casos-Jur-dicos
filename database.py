import sqlite3
from models import Caso

def conectar_banco():
    return sqlite3.connect('casos_juridicos.db')

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Criação da tabela de casos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS casos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero TEXT NOT NULL,
        cliente TEXT NOT NULL,
        data_abertura TEXT NOT NULL,
        status TEXT NOT NULL,
        descricao TEXT,
        advogado TEXT NOT NULL
    )
    ''')
    
    conexao.commit()
    conexao.close()

def adicionar_caso(caso: Caso):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''
    INSERT INTO casos (numero, cliente, data_abertura, status, descricao, advogado)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (caso.numero, caso.cliente, caso.data_abertura, caso.status, caso.descricao, caso.advogado))
    
    conexao.commit()
    conexao.close()

def buscar_casos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM casos')
    casos = cursor.fetchall()
    
    conexao.close()
    return casos

def deletar_caso(caso_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('DELETE FROM casos WHERE id = ?', (caso_id,))
    conexao.commit()
    conexao.close()
