from optparse import OptionParser
import csv
import manage
import time
import datetime
from djangoappengine.settings_base import *

from api.models import Team
from api.models import Player

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

    try:
      debut_date = time.strptime(date_string, "%m/%d/%Y")
    except ValueError:
      # some are blank, some have fucked up characters.  magic date!...
      date_string = "01/01/1000"

    debut_date = time.strptime(date_string, "%m/%d/%Y")
    debut_date = datetime.date(debut_date.tm_year, debut_date.tm_mon, debut_date.tm_mday)
    player = Player(last_name = last_name, first_name = first_name, retrosheet_id = key, debut_date = debut_date)
    
    player.save()

