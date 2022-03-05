"""populate first table

Revision ID: b61bcf749196
Revises: bf72a90d96c0
Create Date: 2022-03-03 13:08:23.727951

"""
# if having issues running in container try
# export PYTHONPATH=/app/
from alembic import op
import sqlalchemy as sa
from stub_data import stub

# revision identifiers, used by Alembic.
revision = 'b61bcf749196'
down_revision = 'bf72a90d96c0'
branch_labels = None
depends_on = None


def upgrade():
    for player in stub:

      command = 'insert into rushing_stats ("player","team","pos","att","att_g","yds","avg","yds_g","td","lng","first","first_percent","twenty_plus","forty_plus","fum") \
        values \
          (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'\
            .format(
              str(player['Player']).replace("'","''"),player['Team'],player['Pos'],player['Att'],player['Att/G'],int(str(player['Yds']).replace(',','')),player['Avg'],player['Yds/G'],
              player['TD'],player['Lng'],player['1st'],player['1st%'],player['20+'],player['40+'],player['FUM'],
            )
      op.execute(command)


def downgrade():
    for player in stub:
      command = 'delete from rushing_stats where player=\'{}\' and  team=\'{}\' and pos=\'{}\''.format(str(player['Player']).replace("'","''"), player['Team'], player['Pos'])
      op.execute(command)
