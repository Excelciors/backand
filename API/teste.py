
conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
cur = conn.cursor()
cur.execute("insert into evento(nome,local_evento,numero_atividades) values (%s,%s,%s,%s,%s,0,0)"%(arq['Jorge'], arq['Facef'], arq[25]
keys = ['nome_aluno','id_aluno','nome_curso']

result = cur.fetchall()

values = []
for i in result[0]:
values.append(i)


result = OrderedDict(zip(keys,values))


return jsonify(result)