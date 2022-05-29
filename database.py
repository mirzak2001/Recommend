from importlib.metadata import metadata
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
from traitlets import default


import tables


engine = create_engine('sqlite:///sqlalchemy.sqlite', connect_args = {'check_same_thread': False} )
#, connect_args = {'check_same_thread': False}
Session = sessionmaker(
    engine, 
    autocommit = False,
    autoflush = False,

)

def new_session() -> Session:
    session = Session()
    try :
        yield session
    finally:
        session.close()

"""

To import csv to the Database

from tables import Base
Base.metadata.create_all(engine)


session = Session()
with open("walmart_fin.csv", encoding='UTF-8') as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data = [row for row in reader][1:]
print (data[0])
for i in data:
    record1 = tables.Category(**{
                    'id' : i[1],
                    'Title' : i[4],})
    record2 = tables.Product(**{
                    'id' : i[1],
                    'Title' : i[2],
                    'Description' : i[3],
                    'Category' : i[4] })
    session.add(record1)
    session.commit()
    session.add(record2)
    session.commit()

session.close()

"""