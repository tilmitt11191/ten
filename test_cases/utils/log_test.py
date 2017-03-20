#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
class Log_test(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_if_else(self):
		#self.log.info("test_if_else")
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger(logfile="../../var/log/log.test2", conffile="../../etc/config.yml")
		self.log.info("test_if_else")


	def test_rotate(self):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger(logfile="../../var/log/log.test2")
		self.log.info("test_rotate")
		self.log.debug("debug comment")
		

if __name__ == '__main__':
	unittest.main()
