from optparse import OptionParser
import csv
import manage
import time
import datetime
from djangoappengine.settings_base import *

from api.models.player import Player
from api.models.team import Team
from api.models.game import Game
from api.models.lineup import Lineup
from api.models.lineup_entry import LineupEntry

import google

implemented_importers = {
  'team': 'http://www.retrosheet.org/TeamIDs.htm',
  'player': 'http://www.retrosheet.org/retroID.htm',
  'gamelog': 'http://www.retrosheet.org/gamelogs/index.html'
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


def split_seq(seq,size):
  """ Split up seq in pieces of size """
  return [seq[i:i+size] for i in range(0, len(seq), size)]

def lineup_data_for(rs_array):
  lineup_data = split_seq(rs_array, 3)
  data = []
  for i in range(len(lineup_data)):
    lineup_row = lineup_data[i]
    print lineup_row
    rs_id = lineup_row[0]
    player_name = lineup_row[1] # not that we'll use it
    defensive_position = int(lineup_row[2])
    batting_position = i + 1
    data.append({'rs_id': rs_id, 'defensive_position': defensive_position, 'batting_position': batting_position})
  return data

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
    winning_pitcher = Player.objects.filter(retrosheet_id = row[93])[0]
    losing_pitcher = Player.objects.filter(retrosheet_id = row[95])[0]

    game = Game(attendance = attendance, date = game_date, day_of_week = day_of_week, winning_pitcher = winning_pitcher, losing_pitcher = losing_pitcher)

    game.save()

    away_team = Team.objects.filter(team_abbreviation=row[3], league=row[4])[0]
    away_team_game_number = int(row[5])
    away_team_runs_scored = int(row[9])
    away_team_starting_pitcher = Player.objects.filter(retrosheet_id = row[101])[0]
    away_participant = game.gameparticipant_set.create(team = away_team, game_number_for_season = away_team_game_number, team_location_status = 'away', runs_scored_count = away_team_runs_scored, starting_pitcher = away_team_starting_pitcher)

    home_team = Team.objects.filter(team_abbreviation=row[6], league=row[7])[0]
    home_team_game_number = int(row[8])
    home_team_runs_scored = int(row[10])
    home_team_starting_pitcher = Player.objects.filter(retrosheet_id = row[103])[0]
    home_participant = game.gameparticipant_set.create(team = home_team, game_number_for_season = home_team_game_number, team_location_status = 'home', runs_scored_count = home_team_runs_scored, starting_pitcher = home_team_starting_pitcher)




    # away starting lineup
    away_lineup = Lineup(team = away_team, date = game_date, game_participant = away_participant) 
    away_lineup.save()

    away_dicts = lineup_data_for(row[105:132])
    for d in away_dicts:
      player = Player.objects.filter(retrosheet_id = d['rs_id'])[0]
      lineup_entry = LineupEntry(player = player, lineup = away_lineup, is_starter = True, batting_position = d['batting_position'], defensive_position = d['defensive_position'])
      lineup_entry.save()

    # home starting lineup
    home_lineup = Lineup(team = home_team, date = game_date, game_participant = home_participant) 
    home_lineup.save()
    home_dicts = lineup_data_for(row[132:159])

    for d in home_dicts:
      player = Player.objects.filter(retrosheet_id = d['rs_id'])[0]
      lineup_entry = LineupEntry(player = player, lineup = home_lineup, is_starter = True, batting_position = d['batting_position'], defensive_position = d['defensive_position'])
      lineup_entry.save()
