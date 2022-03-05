"""populate 10000 rows

Revision ID: c83affcaea8a
Revises: b61bcf749196
Create Date: 2022-03-04 17:44:48.478986

"""
from alembic import op
import sqlalchemy as sa
from generated import generated
import os

# revision identifiers, used by Alembic.
revision = 'c83affcaea8a'
down_revision = 'b61bcf749196'
branch_labels = None
depends_on = None


def upgrade():
  if not os.getenv('10K_ROWS'):
    for player in generated:

      command = 'insert into rushing_stats ("player","team","pos","att","att_g","yds","avg","yds_g","td","lng","first","first_percent","twenty_plus","forty_plus","fum") \
        values \
          (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'\
            .format(
              str(player['player']).replace("'","''"),player['team'],player['pos'],player['att'],player['att_g'],int(str(player['yds']).replace(',','')),player['avg'],player['yds_g'],
              player['td'],player['lng'],player['first'],player['first_percent'],player['twenty_plus'],player['forty_plus'],player['fum'],
            )
      op.execute(command)


def downgrade():
  if not os.getenv('10K_ROWS'):
    for player in generated:
      command = 'delete from rushing_stats where player=\'{}\' and  team=\'{}\' and pos=\'{}\''.format(str(player['player']).replace("'","''"), player['team'], player['pos'])
      op.execute(command)
