#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
class File_manager_test(unittest.TestCase):
	def setUp(self):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger()
		
		
	def test_getconf(self):
		self.log.info("test_getconf")
		from file_manager import File_manager as f
		self.assertEqual("DEBUG", f.getconf("loglevel"))

	def test_renew_output_filename(self):
		from file_manager import File_manager as f
		f = f()
		f.set_output_filename("../../data/tsumo/sample0.txt_tsumo")
		f.renew_output_filename()
		#self.assertEqual("DEBUG", f.getconf("loglevel"))

	
if __name__ == '__main__':
	unittest.main()
