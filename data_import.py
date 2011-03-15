from optparse import OptionParser
import csv
import manage


parser = OptionParser()
parser.add_option('-f', '--file', dest='csv_file_path', help='csv file to import', metavar='FILE')
(options, args) = parser.parse_args()

file_contents = open(options.csv_file_path)
rows = csv.reader(file_contents, delimiter=',')

for row in rows:
  print row


