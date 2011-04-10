from optparse import OptionParser
import csv
import manage
import time
import datetime
from djangoappengine.settings_base import *

from api.models.player import Player
from api.models.team import Team
from api.models.game import Game

import google

implemented_importers = {
  'team': 'http://www.retrosheet.org/TeamIDs.htm',
  'player': 'http://www.retrosheet.org/retroID.htm'
}

parser = OptionParser()
parser.add_option('-f', '--file', dest='csv_file_path', help='csv file to import', metavar='FILE')
parser.add_option('-t', '--type', dest='retrosheet_file_type', help=('The Retrosheet file type.  Implemented are: ' + ','.join(implemented_importers.keys()) + '.'), metavar='RETROSHEET_TYPE') 
(options, args) = parser.parse_args()

import_type = options.retrosheet_file_type
file_contents = open(options.csv_file_path)

def date_or_none(date_string, date_format="%m/%d/%Y"):
  try:
    out_date = time.strptime(date_string, date_format)
    out_date = datetime.date(out_date.tm_year, out_date.tm_mon, out_date.tm_mday)
  except ValueError:
    out_date = None
  return out_date

rows = csv.reader(file_contents, delimiter=',')

if import_type == 'team':
  for row in rows:
    abbreviation = row[0]
    league = row[1]
    city = row[2]
    nickname = row[3]
    year_first_active = row[4]
    year_last_active = row[5]
    
    team = Team(team_abbreviation=abbreviation, league=league, city=city, nickname=nickname, year_first_active=year_first_active, year_last_active=year_last_active)
    team.save()

if import_type == 'player':
  for row in rows:
    last_name = row[0]
    first_name = row[1]
    key = row[2]
    date_string = row[3]

    debut_date = date_or_none(date_string)

    player = Player(last_name = last_name, first_name = first_name, retrosheet_id = key, debut_date = debut_date)
    player.save()

if import_type == 'gamelog':
  for row in rows:
    game_date = date_or_none(row[0], "%Y%m%d")
    attendance = int(row[17])
    day_of_week = row[2]
    duration_in_minutes = int(row[18])
    game = Game(attendance = attendance, date = game_date, day_of_week = day_of_week)


    away_team = Team.objects.filter(team_abbreviation=row[3], league=row[4])[0]
    away_team_game_number = int(row[5])
    away_team_runs_scored = int(row[9])

    home_team = Team.objects.filter(team_abbreviation=row[6], league=row[7])[0]
    home_team_game_number = int(row[8])
    home_team_runs_scored = int(row[10])
