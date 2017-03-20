#!/usr/bin/python
# -*- coding: utf-8 -*-

class File_manager:
	def __init__(self):
		import yaml
		with open("../../etc/config.yml", "r") as f:
			conf = yaml.load(f)

		logfile = conf["logdir"] + conf["logfile"]
		loglevel = conf["loglevel"]	
		import logging
		logging.basicConfig(filename=logfile, level=eval("logging."+loglevel))	
		self.log = logging.getLogger()
		
		self.num_of_max_line = conf["num_of_max_line"]

		self.output_file_number = 0


	@classmethod
	def getconf(cls, conf, conffile="../../etc/config.yml"):
		if(conffile==""):
			conffile="../../etc/config.yml"
		
		import yaml
		with open(conffile, "r") as f:
			confs = yaml.load(f)
		return confs[conf]
	
	
	def add_array_to_file(self, arr, file, suffix="csv", codec="shift-jis"):
		self.log.info("add_array_to_file start.")
		self.log.debug("file[{file}], suffix[{suffix}], num_of_max_line[{self.num_of_max_line}]".format(**locals()))
		self.log.debug("arr[arr]".format(**locals()))
		
		output_file_name = file + "_" + str(self.output_file_number) + "." + suffix

		import os.path
		if os.path.exists(output_file_name):
			self.log.debug("self.num_of_max_line:"+str(self.num_of_max_line))
			import codecs
			f = codecs.open(output_file_name, "r", codec)
			line_num=sum(1 for line in f)
			f.close()
		else:
			line_num = 0
		self.log.debug("line_num:" + str(line_num))

		while os.path.exists(output_file_name) and line_num > self.num_of_max_line:
			self.output_file_number += 1
			output_file_name = file + "_" + str(self.output_file_number) + "." + suffix
			self.log.debug("output_file_name[{output_file_name}]".format(**locals()))
		
		import codecs
		self.log.debug("write to [{output_file_name}]".format(**locals()))
		with codecs.open(output_file_name, 'a', codec) as f:
			for el in arr:
				f.write(el +"\n")

		self.log.info("add_array_to_file finished. return empty arr.")
		return []


























