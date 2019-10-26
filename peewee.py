from pony.orm import *


db = Database()
class MyEntity(db.Entity):
    attr1 = Required(str)


db.bind(provider='postgres', user='postgres', password='1234', host='localhost', database='Teste2')



class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')

class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)


#Gera o mapping e cria as tabelas geradas acima
db.generate_mapping(create_tables=True)
