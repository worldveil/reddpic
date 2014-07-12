from reddpic import Reddpic
from reddpic.utilities import splitcommas
from optparse import OptionParser
import json

"""
Example:
	$ python reddpic.py \
		--terms tim,howard,GoT \
		--not brazil,columbia \
		--config ./settings.example.json
"""

# parse command line inputs
usage = "usage: %prog [options]"
parser = OptionParser(usage=usage, version="%prog 1.0")
parser.add_option("-c", "--config",
				  action="store",
                  dest="settings_path",
                  default="settings.example.json",
                  help='Location of settings JSON file')
parser.add_option('-t', '--terms',
                  type='string',
                  action='callback',
                  callback=splitcommas)
parser.add_option('-n', '--nots',
                  type='string',
                  action='callback',
                  callback=splitcommas)
options, args = parser.parse_args()

# load settings
configpath = options.settings_path
settings = json.load(open(configpath, 'rb'))

# create Reddpic object and output JSON to stdout
r = Reddpic(settings["credentials"]["username"], 
			settings["credentials"]["password"])
r.query(options.terms, options.nots, output=True)

