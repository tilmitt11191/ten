#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tenhou:
	def __init__(self):
		import yaml
		conf = yaml.load(open("../../etc/config.yml", "r"))
		logfile = conf["logdir"] + conf["logfile"]
		loglevel = conf["loglevel"]
	
		import logging
		logging.basicConfig(filename=logfile, level=eval("logging."+loglevel))	
		
	def get_tsumo_from(filename):
		logging.debug("get_tsumo_from start.")
		logging.debug("get_tsumo_from finished.")
		
		