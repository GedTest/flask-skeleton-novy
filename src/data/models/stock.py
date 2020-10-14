from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime, Float

from ..database import db
from ..mixins import CRUDModel

class Stock(CRUDModel):
    __tablename__ = 'stock'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    firma = Column(String(60), index=True)
    firma_zkratka = Column(String(10), index=True)
    jmenovita_hodnota = Column(Float, index=False)
    cena = Column(Float, default=False)
    datum_insertu= Column(DateTime)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.datum_insertu = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    #@staticmethod
    #def vypis_spolecny_radek():
    #    return db.session.query(Stock.firma,func.avg(Stock.posledni_cena).label("Prumerna_cena")).group_by("firma")
