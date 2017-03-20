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


if __name__ == '__main__':
	unittest.main()
