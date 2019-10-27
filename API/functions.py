import psycopg2
import config
import json
import sys
from collections import OrderedDict
from flask import jsonify


sys.path.append('../')




class inserts():
    def user(self, dados):
        conn = config.conn
        cur = config.cur


        result = cur.execute("""
            insert into tb_usuarios(nome_usuario, data_nasc, senha, email)
            values('%s','%s','%s','%s')
        """%(dados["nome_usuario"], dados["data_nasc"], dados["senha"], dados["email"]))
        conn.commit()

        # cur.close()
        # conn.close()
    
    def clas(self,dados):
        conn = config.conn
        cur = config.cur

        result = cur.execute("""
            insert into tb_topicos(nome_topico, classificacao)
            values('%s','%s')
        """%(dados["nome_topico"], dados["classificacao"]))
        conn.commit()

        return "sucesso"
    
    def contents(self,dados):
        conn = config.conn
        cur = config.cur

        result = cur.execute("""
            insert into tb_conteudos(id_topicos, conteudo, nome_conteudo)
            values('%s','%s','%s')
        """%(dados["id_topicos"], dados["conteudo"], dados["nome_conteudo"]))
        conn.commit()

        return "sucesso"
    
    def curiosity(self,dados):
        conn = config.conn
        cur = config.cur

        result = cur.execute("""
            insert into tb_curiosidades(curiosidade, link_aprofundamento, id_conteudo)
            values('%s','%s','%s')
        """%(dados["curiosidade"], dados["link_aprofundamento"], dados["id_conteudo"]))
        conn.commit()

        return "sucesso"

    def permissao(self,dados):
        conn = config.conn
        cur = config.cur

        result = cur.execute("""
            insert into tb_permissoes(tipo)
            values('%s')
        """%(dados["tipo"]))
        conn.commit()

        return "sucesso"

    


class selects():
    def allUsers(self):
        conn = config.conn
        cur = config.cur

        query = cur.execute("SELECT * FROM tb_usuarios")

        
        #result = cur.fetchall()

        result = json.dumps(cur.fetchall(), default=str)
        result = json.loads(result)

        #keys = ['id_usuario','nome_usuario','data_nasc','senha','email','id_permissao','id_survey']

        values = []
        for i in result:
            values.append(i)

        #result = OrderedDict(zip(keys,values))
        # cur.close()
        # conn.close()

        return jsonify(result)

    def user(self,id):
        conn = config.conn
        cur = config.cur

        query = cur.execute("SELECT * FROM tb_usuarios where id_usuario = %s"%id)

        keys = ['id_usuario','nome_usuario','data_nasc','senha','email','id_permissao','id_survey']
        
        result = json.dumps(cur.fetchall(), default=str)
        result = json.loads(result)

        values = []
        for i in result[0]:
            values.append(i)

        result = OrderedDict(zip(keys,values))
        # cur.close()
        # conn.close()

        return jsonify(result)
    
    def classes(self):

        conn = config.conn
        cur = config.cur

        query = cur.execute("SELECT * FROM tb_topicos ")

        
        #result = cur.fetchall()

        result = json.dumps(cur.fetchall(), default=str)
        result = json.loads(result)

        #keys = ['id_usuario','nome_usuario','data_nasc','senha','email','id_permissao','id_survey']

        values = []
        for i in result:
            values.append(i)

        #result = OrderedDict(zip(keys,values))
        # cur.close()
        # conn.close()

        return result

    def conteudo(self,id):

        conn = config.conn
        cur = config.cur

        query = cur.execute("SELECT * FROM tb_conteudos Where id_topicos = %s"%id)

        
        #result = cur.fetchall()

        result = json.dumps(cur.fetchall(), default=str)
        result = json.loads(result)

        keys = ['id_conteudo','id_topico','content','nome_conteudo']

        values = []
        for i in result[0]:
            values.append(i)

        result = OrderedDict(zip(keys,values))
        # cur.close()
        # conn.close()

        return result

    def topico(self):

        conn = config.conn
        cur = config.cur

        query = cur.execute("SELECT * FROM tb_topicos ")

        
        #result = cur.fetchall()

        result = json.dumps(cur.fetchall(), default=str)
        result = json.loads(result)

        #keys = ['id_usuario','nome_usuario','data_nasc','senha','email','id_permissao','id_survey']

        values = []
        for i in result:
            values.append(i)

        #result = OrderedDict(zip(keys,values))
        # cur.close()
        # conn.close()

        return result


    def curiosity(self,id):

        conn = config.conn
        cur = config.cur

        query = cur.execute("SELECT * FROM tb_curiosidades Where id_conteudo = %s"%id)

        
        #result = cur.fetchall()

        result = json.dumps(cur.fetchall(), default=str)
        result = json.loads(result)

        # keys = ['id_curiosidade','curiosidade','link_aprofundamento','id_conteudo']

        values = []
        for i in result:
            values.append(i)

        # result = OrderedDict(zip(keys,values))
        # cur.close()
        # conn.close()

        return result

    def permissao(self):
    
        conn = config.conn
        cur = config.cur

        query = cur.execute("SELECT * FROM tb_permissoes ")

        
        #result = cur.fetchall()

        result = json.dumps(cur.fetchall(), default=str)
        result = json.loads(result)

        #keys = ['id_usuario','nome_usuario','data_nasc','senha','email','id_permissao','id_survey']

        values = []
        for i in result:
            values.append(i)

        #result = OrderedDict(zip(keys,values))
        # cur.close()
        # conn.close()

        return result


class modify():
    def modifyUser(self, id, dados):
        conn = config.conn
        cur = config.cur

        query = cur.execute("""
            UPDATE tb_usuarios
            SET nome_usuario = '%s', email = '%s', senha = '%s', data_nasc = '%s'
            WHERE id_usuario = %s;
        """%(dados["nome_usuario"], dados["email"], dados["senha"], dados["data_nasc"], id))

        return "sucesso"