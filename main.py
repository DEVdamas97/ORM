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
engine = create_engine("sqlite:///estoque.db", echo=False)

# Criar Tabelas no Banco se ainda não existirem

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Sessão Ativo - pense como um carrinho de compras
session = Session()

# Criar objetos de produtos

# Create 

produto1 = Produto("Notebook", 5500, 6, True)
produto2 = Produto("Teclado", 500, 100, True)
produto3 = Produto("Mouse", 150, 55, True)

# Adicionar os produtos na sessão (carrinho)

# session.add(produto1)
# session.add(produto2)
# session.add(produto3)

# Confirmar a inserção no db

# Salvar no db

# session.commit()

# Listar 

# Buscar todos os Produtos do banco 

produtos = session.query(Produto).all()

# for p in produtos:
#     print(f"Produto: {p.id}, Nome: {p.nome}, preco: {p.preco}, estoque: {p.estoque}, ativo: {p.ativo} ")

# UPDATE (atualizar)

# Buscar o produto com id = 1 

# produto_id = session.query(Produto).filter(Produto.id == 1).first()

# print(produto_id)

# produto_estoque = session.query(Produto).filter(Produto.estoque  > 10).all()
# for p in produto_estoque:
#     print(produto_estoque[1].estoque)

# produto_id_2 = session.query(Produto).filter_by(id = 1).first()

# print(produto_id_2)

# Podemos usar o ORDER BY no db

# produtos_organizados = session.query(Produto).order_by(Produto.estoque).all()
# produtos_organizados = session.query(Produto).desc(Produto.estoque).all()

# Podemos listar limitando a quantidade de resultados

# produtos_mais_caros = session.query(Produto).order_by(Produto.preco.desc()).limit(3).all()

# for p in produtos_mais_caros:
#     print(f"Nome: {p.nome}\nQuantidade: {p.preco}\n\n")

# Update Atualizar

notebook = session.query(Produto).filter_by(id=1).first()

notebook.preco = 6000

# Confirmar esssa alteração

session.commit()

for p in produtos:
    print(f"Produto: {p.id}, Nome: {p.nome}, preco: {p.preco}, estoque: {p.estoque}, ativo: {p.ativo}\n")


# Remover o Produto

produto_remover = session.query(Produto).filter_by(id=2).first()

session.delete(produto_remover)

# Confirmar remoção

session.commit()

print("Produto removido com sucesso!")