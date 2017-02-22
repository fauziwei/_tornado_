# coding: utf-8
import uuid
import logging
import hashlib
import datetime
from sqlalchemy import Column, Table, String, \
	DateTime, Integer, ForeignKey, MetaData, create_engine
from sqlalchemy.orm  import mapper, sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base


database = 'sqlite.db'
engine = create_engine('sqlite:///%s' % database, encoding='utf8', poolclass=NullPool, echo=False)

metadata = MetaData(engine)
Base = declarative_base()


class Db:
	def __init__(self):
		self.Session = sessionmaker()
		self.Session.configure(bind=engine)

	@property
	def session(self):
		return self.Session()


class Role(Base):
	__tablename__ = 'role'
	__table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci'}
	id = Column('id', String(36), primary_key=True)
	name = Column('name', String(128), index=True)


class User(Base):
	__tablename__ = 'user'
	__table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci'}
	id = Column('id', String(36), primary_key=True)
	email = Column('email', String(255), index=True)
	password = Column('password', String(255), index=True)
	role = Column('role', String(128), ForeignKey('role.name'), index=True)
	create = Column('create', DateTime())


Base.metadata.create_all(engine)


# mapping
# role_table = Table('role', metadata, autoload=True)
# user_table = Table('user', metadata, autoload=True)
# mapper(Role, role_table)
# mapper(User, user_table)


'''Initial create administrator.'''

session = Db().Session()
role = session.query(Role).filter_by(name='administrator').first()
if not role:
	role = Role()
	role.id = str(uuid.uuid4())
	role.name = 'administrator'
	session.add(role)

session.commit()


'''Initial create user admin.'''
user = session.query(User).filter_by(email='admin').first()
if not user:
	user = User()
	user.id = str(uuid.uuid4())
	user.email = 'admin'
	user.password = hashlib.sha1('admin').hexdigest()
	user.role = 'administrator'
	user.create = datetime.datetime.now()
	session.add(user)

session.commit()

'''Initial create user fauzi.'''
user = session.query(User).filter_by(email='fauzi').first()
if not user:
	user = User()
	user.id = str(uuid.uuid4())
	user.email = 'fauzi'
	user.password = hashlib.sha1('fauzi').hexdigest()
	user.role = 'administrator'
	user.create = datetime.datetime.now()
	session.add(user)

session.commit()


session.close()
