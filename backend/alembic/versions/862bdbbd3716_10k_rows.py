"""10K rows

Revision ID: 862bdbbd3716
Revises: a56f55c820a1
Create Date: 2022-03-06 22:04:29.332403

"""
import os
from alembic import op
import sqlalchemy as sa
from ten_k_rows import generated

# revision identifiers, used by Alembic.
revision = '862bdbbd3716'
down_revision = 'a56f55c820a1'
branch_labels = None
depends_on = None


def upgrade():
  if not os.getenv('10K_ROWS'):
    for player in generated:
      # create player
      command = 'insert into player ("player", "position_id", "team_id") values (\'{}\',\'{}\',\'{}\')'.format(
        str(player['player']).replace("'","''"),
        player['pos'],
        player['team']
      )
      op.execute(command)

      # create stats
      command = 'insert into rushing_stats ("player_id","att","att_g","yds","avg","yds_g","td","lng","first","first_percent","twenty_plus","forty_plus","fum") \
        values \
          ((select id from player where player = \'{}\' limit 1),\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'\
            .format(
              str(player['player']).replace("'","''"),player['att'],player['att_g'],int(str(player['yds']).replace(',','')),player['avg'],player['yds_g'],
              player['td'],player['lng'],player['first'],player['first_percent'],player['twenty_plus'],player['forty_plus'],player['fum'],
            )
      op.execute(command)


def downgrade():
  if not os.getenv('10K_ROWS'):
    for player in generated:
      command = 'delete from rushing_stats where player_id=(select id from player where player = \'{}\' limit 1)'.format(str(player['player']).replace("'","''"))
      op.execute(command)

