from datetime import datetime, timedelta
import csv

from requests import session


from database import Session, new_session

import tables
from models import (CreateUser, User as ModelUser, Token,)
from database import new_session
from kMeans import k_means


def new_experiment (user : ModelUser):
    start = datetime.utcnow()
    session = Session()

    k_means()

    with open("walmart_fin.csv", encoding='UTF-8') as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        data = [row for row in reader][1:]
    for i in data:
        rec1 = tables.Recommendation(**{'experiment_id' : session.query(tables.Experiment).count() + 1,
        'product_id' : i[1], 'cluster' : i[5]})
        session.add(rec1)
        session.commit()
    end = datetime.utcnow()
    rec2 = tables.Experiment(**{'User' : user.id, 
    'StartDateTime': start, 'EndDateTime' : end })
    session.add(rec2)
    session.commit()

    session.close()

