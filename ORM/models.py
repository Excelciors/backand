### models.py ###
import sys
sys.path.append('../')


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import Table, Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import config


Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'tb_usuarios'
    id_usuario = Column(Integer, primary_key=True)
    nome_usuario = Column(String)
    data_nasc = Column(Date)
    senha = Column(String)
    email = Column(String)
    id_permissao = Column(Integer, ForeignKey('tb_permissoes.id_permissao'))
    id_survey = Column(Integer, ForeignKey('tb_surveys.id_survey'))

class Permissoes(Base):
    __tablename__ = 'tb_permissoes'
    id_permissao = Column(Integer, primary_key=True)
    tipo = Column(String)

class Surveys(Base):
    __tablename__ = 'tb_surveys'
    id_survey = Column(Integer, primary_key=True)
    interesse_exatas = Column(Integer)
    interesse_humanas = Column(Integer)
    interesse_biologicas = Column(Integer)


class Interesses(Base):
    __tablename__ = 'tb_interesses'
    id_usuario = Column(Integer, ForeignKey('tb_usuarios.id_usuario'), primary_key=True)
    id_survey = Column(Integer, ForeignKey('tb_topicos.id_topicos'), primary_key=True)
    tempo_visualizacao = Column(Date)
    favorito = Column(Boolean)
    cliques = Column(Integer)

class Topicos(Base):
    __tablename__ = 'tb_topicos'
    id_topicos = Column(Integer, primary_key=True)
    nome_topico = Column(String)
    classificacao = Column(String)

class Conteudos(Base):
    __tablename__ = 'tb_conteudos'
    id_conteudo = Column(Integer, primary_key=True)
    id_topicos = Column(Integer, ForeignKey('tb_topicos.id_topicos'))
    nome_conteudo = Column(String)
    conteudo = Column(Text)
    
class Curiosidades(Base):
    __tablename__ = 'tb_curiosidades'
    id_curiosidade = Column(Integer, primary_key=True)
    curiosidade = Column(String)
    link_aprofundamento = Column(String)
    id_conteudo = Column(Integer, ForeignKey('tb_conteudos.id_conteudo'))


from sqlalchemy import create_engine

engine = create_engine(config.DATABASE_URI)


Base.metadata.create_all(engine)