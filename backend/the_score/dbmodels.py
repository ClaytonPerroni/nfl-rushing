from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class RushingStats(Base):
  __tablename__ = "rushing_stats"

  id = Column(Integer, primary_key=True, index=True)
  player_id = Column(Integer, ForeignKey('player.id'))

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

class Player(Base):
  __tablename__ = "player"

  id = Column(Integer, primary_key=True, index=True)
  player = Column(String)
  team_id = Column(String, ForeignKey('team.short_name'))
  position_id = Column(String, ForeignKey('position.short_name'))

class Team(Base):
  __tablename__ = "team"

  short_name = Column(String, primary_key=True, index=True)

class Position(Base):
  __tablename__ = "position"

  short_name = Column(String, primary_key=True, index=True)
