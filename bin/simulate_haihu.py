#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################################################
haihu_files=["../../etc/data/hounan2015/hounan2015.txt"]
codec = "cp932"
#########################################################

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../lib/utils")
from log import Log as l
log = l.getLogger()


import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../lib/haihu")
log.debug(os.path.dirname(os.path.abspath(__file__)) + "/../lib/haihu")
import tenhou
t = tenhou.Tenhou()

for haihu in haihu_files:
	output = t.simulate_logfile(haihu, codec, output_codec=codec,output_format=["player", "tsumo", "player_machi", "player_tehai"], output_file_suffix="csv")













