"""create teams and pos

Revision ID: 06cb10a49d14
Revises: d05beaf3ede4
Create Date: 2022-03-06 19:18:43.946738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06cb10a49d14'
down_revision = 'd05beaf3ede4'
branch_labels = None
depends_on = None

teams=['JAX', 'MIN', 'BAL', 'CLE', 'DAL', 'NO', 'BUF', 'GB', 'KC', 'CIN', 'SD', 'PHI', 'CAR', 'IND', 'NYG', 'SEA', 'PIT', 'NYJ', 'LA', 'DET', 'HOU', 'CHI', 'SF', 'ATL', 'MIA', 'TEN', 'DEN', 'NE', 'ARI', 'WAS', 'OAK', 'TB']
positions=['RB', 'QB', 'WR', 'FB', 'P', 'TE', 'NT', 'DB', 'K', 'SS']

def upgrade():
  for team in teams:
    command = 'insert into team ("short_name") values (\'{}\')'.format(team)
    op.execute(command)
  for pos in positions:
    command = 'insert into position ("short_name") values (\'{}\')'.format(pos)
    op.execute(command)


def downgrade():
  for team in teams:
    command = 'delete from team where short_name = \'{}\''.format(team)
    op.execute(command)
  for pos in positions:
    command = 'delete from position where short_name = \'{}\''.format(pos)
    op.execute(command)
