
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# absolute path to the database
engine_asynconf = create_engine(
    r'sqlite:///C:\Users\emili\PycharmProjects\asynconf_2023\asynconf.db')
Base_asynconf = declarative_base()
Base_asynconf.metadata.create_all(bind=engine_asynconf)
Session_asynconf = sessionmaker(bind=engine_asynconf)
asynconf = Session_asynconf()