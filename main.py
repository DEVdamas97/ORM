# Importa a função responsavel por criar a coneção com o banco
from sqlalchemy import create_engine

# importar tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importa classe base para criar os modelos ORM
from sqlalchemy.orm import declarative_base

# Importar ferramenta de importar e criar sessões do banco
from sqlalchemy.orm import sessionmaker 