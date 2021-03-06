#!/usr/bin/env python33

import sys
import importlib
import os
#specify which version of the board used here
#from femb_config import FEMB_CONFIG

#from setup_gui import *
#from setup_config import config

config_type = os.environ["CONFIG_TYPE"]
mod = "femb_config_" + config_type
config = importlib.import_module(mod)

femb_config = config.FEMB_CONFIG()

print "BEGIN CHANNEL SELECT"

if config_type == 'sbnd':

	if len(sys.argv) != 4 :
		print 'Invalid # of arguments, usage python select_channel <ASIC #> <channel #> <HS>'
		sys.exit(0)

	asicVal = int( sys.argv[1] )
	if (asicVal < 0) or (asicVal > 7):
		print 'Invalid ASIC number'
		sys.exit(0)

	channelVal = int( sys.argv[2] )
	if (channelVal < 0) or (channelVal > 15):
		print 'Invalid channel number'
		sys.exit(0)

	hsVal = int( sys.argv[3] )
	if (hsVal < 0) or (hsVal > 1):
		print 'Invalid HS'
		sys.exit(0)

	print "ASIC value is", asicVal
	print "Channel value is", channelVal
	print "HS value is",hsVal
	femb_config.selectChannel(asicVal,channelVal,hsVal)

else:

	if len(sys.argv) != 3 :
		print 'Invalid # of arguments, usage python select_channel <ASIC #> <channel #>'
		sys.exit(0)

	asicVal = int( sys.argv[1] )
	if (asicVal < 0) or (asicVal > 7):
		print 'Invalid ASIC number'
		sys.exit(0)

	channelVal = int( sys.argv[2] )
	if (channelVal < 0) or (channelVal > 15):
		print 'Invalid channel number'
		sys.exit(0)

	print "ASIC value is", asicVal
	print "Channel value is", channelVal
	femb_config.selectChannel(asicVal,channelVal)

print "END CHANNEL SELECT"
