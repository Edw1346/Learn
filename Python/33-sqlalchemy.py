import sqlalchemy

"""SQLAlchemy es una biblioteca de Python para interactuar con bases de datos relacionales. Se enfoca en flexibilidad, eficiencia 
y compatibilidad con múltiples motores SQL como MySQL, PostgreSQL y SQLite."""

#Tiene dos enfoques principales:
#Core (SQL Expression Language): Usa consultas SQL directas con Python.
#ORM (Object-Relational Mapping): Permite trabajar con bases de datos mediante clases y objetos.


#Ejemplo con SQLAlchemy Core
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
# Conectar a una base de datos SQLite
engine = create_engine("sqlite:///mi_base.db") 
# Definir una tabla 
metadata = MetaData()
usuarios = Table("usuarios", metadata, Column("id", Integer, primary_key=True), Column("nombre", String), )
 # Crear la tabla en la base de datos
metadata.create_all(engine) 

#Ejemplo con SQLAlchemy ORM
from sqlalchemy.orm import declarative_base, sessionmaker 
Base = declarative_base() 

class Usuario(Base):
    __tablename__ = "usuarios" 
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

# Crear la base de datos 
Base.metadata.create_all(engine) # Crear una sesión 
Session = sessionmaker(bind=engine) 
session = Session() # Insertar un usuario 
nuevo_usuario = Usuario(nombre="Carlos") 
session.add(nuevo_usuario) 
session.commit() 



"""Todas las funciones"""

#1. Funciones del módulo sqlalchemy (Funciones Generales)
#create_engine(url, **kwargs) Crea una conexión a la base de datos.
from sqlalchemy import create_engine 
engine = create_engine("sqlite:///mi_base.db") 

#inspect(engine_or_connection)
#Devuelve un objeto que permite inspeccionar la base de datos.
from sqlalchemy import inspect 
inspector = inspect(engine) 
print(inspector.get_table_names()) # Lista las tablas 

#text(sql_string)
#Permite ejecutar consultas SQL en crudo.
from sqlalchemy import text
with engine.connect() as conn: 
    result = conn.execute(text("SELECT * FROM usuarios")) 
    for row in result:
        print(row) 

#2. Funciones del módulo sqlalchemy.sql (Manipulación de SQL)
#select(*entities)
#Construye una consulta SQL de tipo SELECT.
from sqlalchemy import select
stmt = select(usuarios) 

#insert(table)
#Genera una consulta SQL INSERT.
from sqlalchemy import insert
stmt = insert(usuarios).values(nombre="Carlos") 

#update(table)
#Genera una consulta UPDATE.
from sqlalchemy import update
stmt = update(usuarios).where(usuarios.c.id == 1).values(nombre="Juan") 

#delete(table)
#Genera una consulta DELETE.
from sqlalchemy import delete
stmt = delete(usuarios).where(usuarios.c.id == 1) 

#and_(*clauses)
#Combina condiciones con AND.
from sqlalchemy import 
and_ stmt = select(usuarios).where(and_(usuarios.c.id == 1, usuarios.c.nombre == "Carlos")) 

#or_(*clauses)
#Combina condiciones con OR.
from sqlalchemy import
or_ stmt = select(usuarios).where(or_(usuarios.c.id == 1, usuarios.c.nombre == "Carlos")) 

#3. Funciones del módulo sqlalchemy.orm (ORM - Mapeo de Objetos a Tablas)
#declarative_base()
Crea una base para definir modelos ORM.
from sqlalchemy.orm import declarative_base 
Base = declarative_base() 

#sessionmaker(bind, **kwargs)
#Crea una sesión para interactuar con la base de datos.
from sqlalchemy.orm import sessionmaker 
Session = sessionmaker(bind=engine) 
session = Session() 

#relationship(argumento)
#Define relaciones entre modelos ORM.
from sqlalchemy.orm import relationship 
class Usuario(Base): 
    __tablename__ = "usuarios" 
    id = Column(Integer, primary_key=True)
    publicaciones = relationship("Publicacion", back_populates="usuario") 

#back_populates
#Define relaciones bidireccionales en el ORM.
class Publicacion(Base):
    __tablename__ = "publicaciones" 
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id")) 
    usuario = relationship("Usuario", back_populates="publicaciones") 

#query(Modelo)
#Consulta la base de datos con ORM.
usuarios = session.query(Usuario).filter_by(nombre="Carlos").all() 

#add(instance)
#Agrega un objeto a la base de datos.
nuevo_usuario = Usuario(nombre="Ana")
session.add(nuevo_usuario)
session.commit() 

#commit()
#Guarda los cambios en la base de datos.
session.commit() 

#rollback()
#Revierte los cambios no guardados.
session.rollback() 

#close()
#Cierra la sesión de la base de datos.
session.close() 



"""Clases"""

#1. Clases del módulo sqlalchemy (Generales)
#Engine
#Representa la conexión con la base de datos.
from sqlalchemy import create_engine
engine = create_engine("sqlite:///mi_base.db") 

#Inspector
#Permite inspeccionar la base de datos.
from sqlalchemy import inspect 
inspector = inspect(engine) 
print(inspector.get_table_names()) 


#2. Clases del módulo sqlalchemy.sql (Expresiones SQL)
#Select
#Representa una consulta SELECT.
from sqlalchemy import select
stmt = select(usuarios) 

#Insert
#Representa una consulta INSERT.
from sqlalchemy import insert
stmt = insert(usuarios).values(nombre="Carlos") 

#Update
#Representa una consulta UPDATE.
from sqlalchemy import update 
stmt = update(usuarios).where(usuarios.c.id == 1).values(nombre="Juan") 

#Delete
#Representa una consulta DELETE.
from sqlalchemy import delete 
stmt = delete(usuarios).where(usuarios.c.id == 1) 

#Table
#Define una tabla en SQLAlchemy Core.
from sqlalchemy import Table, Column, Integer, String, MetaData 
metadata = MetaData() 
usuarios = Table("usuarios", metadata, Column("id", Integer, primary_key=True), Column("nombre", String) ) 


#3. Clases del módulo sqlalchemy.orm (ORM - Mapeo de Objetos a Tablas)
#declarative_base
#Crea una base para definir modelos ORM.
from sqlalchemy.orm import declarative_base 
Base = declarative_base() 

#Session
#Representa una sesión para interactuar con la base de datos.
from sqlalchemy.orm import sessionmaker 
Session = sessionmaker(bind=engine) 
session = Session() 

#relationship
#Define relaciones entre modelos ORM.
from sqlalchemy.orm import relationship 
class Usuario(Base): 
    __tablename__ = "usuarios" 
    id = Column(Integer, primary_key=True) 
    publicaciones = relationship("Publicacion", back_populates="usuario") 

#query
#Realiza consultas en ORM.
usuarios = session.query(Usuario).filter_by(nombre="Carlos").all() 


#4. Clases del módulo sqlalchemy.exc (Manejo de Errores)
#SQLAlchemyError
#Clase base para todas las excepciones de SQLAlchemy.
from sqlalchemy.exc import SQLAlchemyError 
try: 
    session.execute("SELECT * FROM tabla_inexistente")
except SQLAlchemyError as e: 
    print(f"Error en SQLAlchemy: {e}") 

#IntegrityError
#Errores por violación de integridad.
from sqlalchemy.exc import IntegrityError
try: 
    session.commit()
except IntegrityError as e: 
    print(f"Error de integridad: {e}") session.rollback() 


"""Variables"""
#1. Variables en sqlalchemy (Generales)
#__version__
#Devuelve la versión de SQLAlchemy instalada.
import sqlalchemy
print(sqlalchemy.__version__) # Ejemplo: '2.0.25' 

#2. Variables en sqlalchemy.engine (Conexión y Configuración)
#DEFAULT_POOLSIZE
#Tamaño de conexión por defecto en un Engine.
from sqlalchemy.engine import DEFAULT_POOLSIZE
print(DEFAULT_POOLSIZE) # Generalmente es 5 

#3. Variables en sqlalchemy.orm (ORM - Configuración y Sesión)
#Session.registry
#Registra sesiones ORM activas.
from sqlalchemy.orm import sessionmaker 
Session = sessionmaker() 
print(Session.registry) # Muestra el registro de sesiones activas 

#Mapper.all_orm_descriptors
#Lista los atributos ORM de un modelo.
from sqlalchemy.orm import Mapper 
print(Mapper.all_orm_descriptors) 


#4. Variables en sqlalchemy.sql (Expresiones SQL y Tipos de Datos)
#null()
#Representa un valor NULL en SQL.
from sqlalchemy.sql import null
stmt = select(usuarios).where(usuarios.c.nombre == null()) 

#true() y false()
#Representan valores TRUE y FALSE en SQL.
from sqlalchemy.sql import true, false
stmt = select(usuarios).where(usuarios.c.activo == true()) 

#5. Variables en sqlalchemy.ext.declarative (ORM Avanzado)
#Base.metadata
#Representa los metadatos de la base de datos en el ORM.
from sqlalchemy.orm import declarative_base 
Base = declarative_base() 
print(Base.metadata.tables) # Muestra todas las tablas ORM registradas 

#DEFAULT_MAX_OVERFLOW
#Máximo de conexiones adicionales permitidas sobre pool_size.
from sqlalchemy.engine import DEFAULT_MAX_OVERFLOW 
print(DEFAULT_MAX_OVERFLOW) # Generalmente es 10 

#6. Constantes en sqlalchemy.dialects (Compatibilidad con Bases de Datos Específicas)
#sqlite.dialect
#Representa el dialecto SQLite en SQLAlchemy.
from sqlalchemy.dialects.sqlite import dialect 
print(dialect.name) # 'sqlite' 

#mysql.dialect
#Representa el dialecto MySQL en SQLAlchemy.
from sqlalchemy.dialects.mysql import dialect
print(dialect.name) # 'mysql' 


"""Excepciones"""
#1. Excepciones Base
#SQLAlchemyError
#Es la clase base para todas las excepciones de SQLAlchemy.
from sqlalchemy.exc import SQLAlchemyError 
try:
    session.execute("SELECT * FROM tabla_inexistente")
except SQLAlchemyError as e: 
    print(f"Error en SQLAlchemy: {e}") 

#2. Excepciones de Integridad
#IntegrityError
#Se lanza cuando se viola una restricción de integridad, como claves primarias duplicadas o claves foráneas inválidas.
from sqlalchemy.exc import IntegrityError 
try:
    session.commit() except IntegrityError as e:
    print(f"Error de integridad: {e}") session.rollback() 

#DataError
#Ocurre cuando los datos no coinciden con el tipo esperado en la base de datos.
from sqlalchemy.exc import DataError
try: 
    session.execute("INSERT INTO usuarios (edad) VALUES ('texto')") 
except DataError as e: 
    print(f"Error de datos: {e}") 

#3. Excepciones de Conexión y Base de Datos
#DatabaseError
#Error genérico de la base de datos.
from sqlalchemy.exc import DatabaseError 
try: 
    session.execute("DROP DATABASE base_inexistente") 
except DatabaseError as e:
    print(f"Error de base de datos: {e}") 

#OperationalError
#Se lanza cuando hay problemas operacionales, como pérdida de conexión o problemas con el servidor de la base de datos.
from sqlalchemy.exc import OperationalError
try: 
    engine.execute("SELECT * FROM usuarios")
except OperationalError as e: 
    print(f"Error operacional: {e}") 

#InterfaceError
#Ocurre cuando hay un problema con el controlador de la base de datos.
from sqlalchemy.exc import InterfaceError
try:
    engine = create_engine("mysql://usuario:clave@localhost/basedatos") 
    engine.connect() 
except InterfaceError as e: 
    print(f"Error de interfaz: {e}") 

#4. Excepciones de Transacciones
#InvalidRequestError
#Ocurre cuando se intenta ejecutar una operación no válida en una transacción.
from sqlalchemy.exc import InvalidRequestError
try: 
    session.commit() session.commit() # Esto podría generar un error
except InvalidRequestError as e: 
    print(f"Error de solicitud inválida: {e}") 

#StatementError
#Ocurre cuando se intenta ejecutar una consulta SQL malformada o con parámetros incorrectos.
from sqlalchemy.exc import StatementError 
try: 
    session.execute("SELECT * FROM usuarios WHERE edad = :edad", {"edad": "texto"}) 
except StatementError as e:
    print(f"Error en la consulta: {e}") 

#5. Excepciones de Mapeo ORM
#NoResultFound
#Ocurre cuando una consulta one() no devuelve resultados.
from sqlalchemy.orm.exc import NoResultFound 
try:
    usuario = session.query(Usuario).filter_by(id=999).one() 
except NoResultFound: 
    print("No se encontró el usuario") 

#MultipleResultsFound
#Se lanza cuando una consulta one() devuelve más de un resultado.
from sqlalchemy.orm.exc import MultipleResultsFound 
try: 
    usuario = session.query(Usuario).filter_by(nombre="Carlos").one() 
except MultipleResultsFound: 
    print("Se encontraron múltiples usuarios con ese nombre") 



"""SQLAlchemy tiene varios submódulos organizados según su funcionalidad"""

#1. sqlalchemy
#Este es el submódulo principal de SQLAlchemy, que incluye configuraciones y funciones esenciales como el manejo de motores de base de datos y la creación de sesiones.
engine = sqlalchemy.create_engine('sqlite:///mi_base.db') 

#2. sqlalchemy.engine
#Este submódulo se encarga del manejo de las conexiones, los motores y la ejecución de sentencias SQL.
#Clases y Funciones: create_engine(), Engine, Connection, Dialect, etc.
from sqlalchemy import create_engine
engine = create_engine("sqlite:///mi_base.db") 

#3. sqlalchemy.orm
#Submódulo utilizado para el mapeo de objetos en bases de datos (ORM), permitiendo mapear clases Python a tablas de bases de datos y proporcionando un conjunto de herramientas para interactuar con ellas.
#Clases y Funciones: Session, relationship(), declarative_base(), etc.
from sqlalchemy.orm import sessionmaker, declarative_base Base = declarative_base() 
Session = sessionmaker() # Crear una sesión
session = Session() 

#4. sqlalchemy.sql
#Este submódulo contiene componentes de SQL de bajo nivel, como expresiones SQL y tipos de datos que puedes utilizar para construir consultas SQL.
#Clases y Funciones: select(), insert(), update(), delete(), null(), true(), etc.
from sqlalchemy import select, Table, Column, Integer, String, MetaData 
metadata = MetaData() 
usuarios = Table('usuarios', metadata, Column('id', Integer, primary_key=True), Column('nombre', String)) 
stmt = select(usuarios) 

#5. sqlalchemy.ext
#Este submódulo ofrece extensiones para SQLAlchemy, como la carga diferida de relaciones, el uso de declarativos, la serialización de objetos y más.
#Submódulos: sqlalchemy.ext.declarative, sqlalchemy.ext.mutable, sqlalchemy.ext.compiler, etc.
from sqlalchemy.ext.declarative import declarative_base 
Base = declarative_base() 

#6. sqlalchemy.types
#Este submódulo contiene los tipos de datos que se utilizan para mapear las columnas de las tablas a tipos de datos de Python.
#Clases y Funciones: Integer, String, Boolean, Date, DateTime, etc.
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base 
Base = declarative_base() 
class Usuario(Base): 
    __tablename__ = 'usuarios' id = Column(Integer, primary_key=True) 
    nombre = Column(String) 

#7. sqlalchemy.dialects
#Este submódulo permite interactuar con bases de datos específicas, como PostgreSQL, MySQL, SQLite, etc. Define dialectos específicos para cada base de datos.
#Submódulos: sqlalchemy.dialects.postgresql, sqlalchemy.dialects.mysql, sqlalchemy.dialects.sqlite, etc.
from sqlalchemy.dialects.postgresql import JSON 
# Usar JSON en PostgreSQL
columna_json = Column(JSON) 

#8. sqlalchemy.exc
#Este submódulo contiene las excepciones relacionadas con SQLAlchemy, como errores de base de datos, de integridad, de mapeo, entre otros.
#Clases: SQLAlchemyError, IntegrityError, DatabaseError, etc.
from sqlalchemy.exc import IntegrityError
try: 
    session.commit() 
except IntegrityError as e:
    print(f"Error: {e}") 

#9. sqlalchemy.schema
#Este submódulo maneja los elementos relacionados con el esquema de la base de datos, como las tablas, columnas, índices y claves foráneas.
#Clases y Funciones: Table, Column, ForeignKey, Index, etc.
from sqlalchemy import Table, Column, Integer, String, MetaData 
metadata = MetaData() 
usuarios = Table('usuarios', metadata, Column('id', Integer, primary_key=True), Column('nombre', String)) 

10. sqlalchemy.util
#Este submódulo contiene varias utilidades y funciones internas que no se usan tan frecuentemente, pero que facilitan la creación y manejo de objetos dentro de SQLAlchemy.
#Funciones: iteritems(), count(), etc.
from sqlalchemy.util import iteritems
 # Uso de utilidades internas, como iteritems para iterar diccionarios 
for key, value in iteritems({"a": 1, "b": 2}): 
    print(key, value) 
