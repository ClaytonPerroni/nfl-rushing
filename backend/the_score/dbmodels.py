from sqlalchemy import Boolean, Column, Integer, String, Float

from .database import Base


class RushingStats(Base):
  __tablename__ = "rushing_stats"

  id = Column(Integer, primary_key=True, index=True)
  player = Column(String)
  team = Column(String)
  pos= Column(String)
  att = Column(Integer)
  att_g = Column(Float)
  yds=Column(Integer)
  avg=Column(Float)
  yds_g=Column(Float)
  td=Column(Integer)
  lng= Column(String)
  first=Column(Integer)
  first_percent=Column(Float)
  twenty_plus=Column(Integer)
  forty_plus=Column(Integer)
  fum=Column(Integer)
