"""
Simple script to extract all the teams and positions in the data set
"""

from stub_data import stub


teams = {}
positions = {}

for player in stub:
  teams[player.get('Team')] = 1
  positions[player.get('Pos')] = 1

print(list(teams))
print(len(list(teams)))
print('\n\n')
print(list(positions))
print(len(list(positions)))