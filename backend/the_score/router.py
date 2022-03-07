from io import StringIO
import csv
from typing import Dict
from .models import SortingDirectionEnum, SortingEnum
from fastapi import APIRouter, Depends, Query 
from fastapi.responses import PlainTextResponse, StreamingResponse
import math
from sqlalchemy.orm import Session
from sqlalchemy import Integer, desc, cast, func
from database import getDb
from .dbmodels import Player, Position, RushingStats, Team

router = APIRouter(
    prefix='/rushing-stats',
    responses={404: {'description': 'Not found'}},
)

@router.get('/')
async def get_players(
    page_size: int = 10, 
    page: int = Query(1, ge=1), 
    query: str = None, 
    order_by: SortingEnum = None, 
    order_direction: SortingDirectionEnum = SortingDirectionEnum.desc, 
    db: Session = Depends(getDb)
  ):

  q = filter_and_sort(query, order_by, order_direction, db)

  count = q.count()
  # pagination
  q = q.limit(page_size).offset(page_size*(page-1))

  # response formatting
  results = q.all()
  pages = math.ceil(count/page_size)
  return {
    'page': page,
    'page_size': page_size,
    'pages': pages,
    'results': results
  }




@router.get('/csv')
async def get_players(
    query: str = None, 
    order_by: SortingEnum = None, 
    order_direction: SortingDirectionEnum = SortingDirectionEnum.desc, 
    db: Session = Depends(getDb)
  ):

  q = filter_and_sort(query, order_by, order_direction, db)
  
  csvfile = create_rushing_stats_csvfile(q)

  return StreamingResponse(csvfile, media_type="text/csv", headers={'Content-Disposition': 'filename=results.csv'})



## Helpers

def create_rushing_stats_csvfile(q):
  headers = ["Player","Team","Pos","Att","Att/G","Yds","Avg","Yds/G","TD","Lng","1st","1st%","20+","40+","FUM"]

  rows = []
  for player in q.all():
    rows.append({
      "Player": player.player,
      "Team": player.team,
      "Pos": player.pos,
      "Att": player.att,
      "Att/G": player.att_g,
      "Yds": player.yds,
      "Avg": player.avg,
      "Yds/G": player.yds_g,
      "TD": player.td,
      "Lng": player.lng,
      "1st": player.first,
      "1st%": player.first_percent,
      "20+": player.twenty_plus,
      "40+": player.forty_plus,
      "FUM": player.fum,
    })
  csvfile = StringIO()
  writer = csv.DictWriter(csvfile, headers)
  writer.writeheader()
  for row in rows:
      writer.writerow(
          dict((k, v) for k, v in row.items())
      )
  csvfile.seek(0)
  return csvfile

def filter_and_sort(search_string, order_by, order_direction, db: Session):
  q = db.query(
    RushingStats.att,
    RushingStats.att_g,
    RushingStats.yds,
    RushingStats.avg,
    RushingStats.yds_g,
    RushingStats.td,
    RushingStats.lng,
    RushingStats.first,
    RushingStats.first_percent,
    RushingStats.twenty_plus,
    RushingStats.forty_plus,
    RushingStats.fum,
    Player.player, 
    Team.short_name.label('team'), 
    Position.short_name.label('pos')) \
    .join(
      Player, RushingStats.player_id==Player.id) \
    .join(
      Team, Player.team_id==Team.short_name) \
    .join(
      Position, Player.position_id==Position.short_name
  )
  # player name query
  if search_string:
    q = player_name_search_query(q, search_string)

  # sorting
  sort_field = get_rushing_stats_field_by_enum(order_by)
  # special sorting for longest rush because it's a complex string
  if order_by == 'lng':
    q = sort_query_by_lng(q, sort_field, order_direction)
  else:
    q = sort_query_by(q, sort_field, order_direction)
  return q


def player_name_search_query(query_string, search_text):
  return query_string.filter(Player.player.ilike('%' + str(search_text) + '%'))

def sort_query_by_lng(query_string, sort_field, order):
    if order == SortingDirectionEnum.asc:
      return query_string.order_by(cast(func.replace(sort_field, 'T',''), Integer))
    else:
      return query_string.order_by(desc(cast(func.replace(sort_field, 'T',''), Integer)))

def sort_query_by(query_string, sort_field, order):
  if order == SortingDirectionEnum.asc:
    query_string = query_string.order_by(sort_field)
  else:
    query_string = query_string.order_by(desc(sort_field))
  return query_string

def get_rushing_stats_field_by_enum(field):
  if field == SortingEnum.td:
    return RushingStats.td
  elif field == SortingEnum.lng:
    return RushingStats.lng
  #what to do for default, yds for now
  else:
    return RushingStats.yds

