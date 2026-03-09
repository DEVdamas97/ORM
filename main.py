# Importa a função responsavel por criar a coneção com o banco
from sqlalchemy import create_engine

# importar tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importa classe base para criar os modelos ORM
from sqlalchemy.orm import declarative_base

# Importar ferramenta de importar e criar sessões do banco
from sqlalchemy.orm import sessionmaker

# Criar classe do ORM
Base = declarative_base()

# Classes = Tabelas
# Objetos = Linha Tabela
# Aributos = Coluna

# Classe Produto representa uma tabala no banco de dados

class Produto(Base):
    # Nome da Tabela no Banco
    __tablename__ = "produtos"

    #Coluna de ID
    # Integer > Numero Intero
    # Primary_key = True

    id = Column(Integer, primary_key= True)

    # Nome do Produto
    # Sttring : texto
     
    nome = Column(String(100))

    # Preco novo produto
    # float : numero decimal
    preco = Column(Float)

    # Quantidade Estoque
    estoque = Column(Integer)

    # Produto ativo ou não
    ativo = Column(Boolean)

    #Metodo construtor

    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    # Representação do objeto para imprimir
    def __repr__(self):
        return f"Produto: {self.id}, Nome: {self.nome}, preco: {self.preco}, estoque: {self.estoque}, ativo: {self.ativo} "
    
# Criar conexão com o sqlite

# echo=True = log do sql
engine = create_engine("sqlite:///estoque.db", echo=True)

# Criar Tabelas no Banco se ainda não existirem

Base.metadata.create_all(engine)