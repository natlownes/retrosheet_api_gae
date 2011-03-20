from optparse import OptionParser
import csv
import manage
from djangoappengine.settings_base import *

from api.models import Team

import google
#import google.appengine.api.namespace_manager
#google.appengine.api.namespace_manager.set_namespace('retrosheetapi')
#print google.appengine.api.namespace_manager.get_namespace()

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
    debut_date = row[3]

    player = Player(last_name = last_name, first_name = first_name, key = key, debut_date = debut_date)
    player.save()

