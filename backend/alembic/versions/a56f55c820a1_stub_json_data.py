"""stub-json data

Revision ID: a56f55c820a1
Revises: 06cb10a49d14
Create Date: 2022-03-06 19:41:31.382562

"""
from alembic import op
import sqlalchemy as sa
from stub_data import stub

# revision identifiers, used by Alembic.
revision = 'a56f55c820a1'
down_revision = '06cb10a49d14'
branch_labels = None
depends_on = None


def upgrade():
    for player in stub:
      # create player
      command = 'insert into player ("player", "position_id", "team_id") values (\'{}\',\'{}\',\'{}\')'.format(
        str(player['Player']).replace("'","''"),
        player['Pos'],
        player['Team']
      )
      op.execute(command)

      # create rushing data
      command = 'insert into rushing_stats ("player_id","att","att_g","yds","avg","yds_g","td","lng","first","first_percent","twenty_plus","forty_plus","fum") \
        values \
          ((select id from player where player = \'{}\' limit 1),\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'\
            .format(
              str(player['Player']).replace("'","''"),player['Att'],player['Att/G'],int(str(player['Yds']).replace(',','')),player['Avg'],player['Yds/G'],
              player['TD'],player['Lng'],player['1st'],player['1st%'],player['20+'],player['40+'],player['FUM'],
            )
      op.execute(command)


def downgrade():
    for player in stub:
      command = 'delete from player where player=\'{}\' and  position_id=\'{}\' and team_id=\'{}\''.format(
        str(player['Player']).replace("'","''"), 
        '(select short_name from position where short_name = "{}")'.format(player['Pos']),
        '(select short_name from team where short_name = "{}")'.format(player['Team'])
        )
      op.execute(command)
      command = 'delete from rushing_stats where player=\'{}\' and  team=\'{}\' and pos=\'{}\''.format(str(player['Player']).replace("'","''"), player['Team'], player['Pos'])
      op.execute(command)
