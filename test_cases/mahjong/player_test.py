#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
class File_manager_test(unittest.TestCase):
	def setUp(self):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger()
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/mahjong")
		
		
	"""	
	def test_initialize(self):
		self.log.info("test_initialize start")
		from player import Player as p
		p = p()
		#TABLE_INV = {v:k for k, v in p.TABLE.items()}
		#print(str(TABLE_INV))
		self.log.info("test_initialize finished.")
	

	def test_init_hand_with(self):
		self.log.info("test_init_hand_with start.")
		#haipai = "1m1m1m2m3m4m5m6m7m8m9m9m9m"
		haipai = ['2m', '5m', '6m', '8m', '7p', '8p', '9p', '5S', '9s', '9s', '南', '白', '中']
		from player import Player as p
		p = p()
		p.init_hand_with(haipai)
		self.log.debug(str(p.tehai))
		self.log.debug("p.tehai:" + str(p.tehai))
		self.log.debug("correct:" + str([0,0,1,0,0,1,1,0,1,0, 0,0,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,0,0,1, 0,1,0,0,1,0,1]))
		self.assertEqual([0,0,1,0,0,1,1,0,1,0, 0,0,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,0,0,2, 0,1,0,0,1,0,1], p.tehai)
		self.assertEqual(['2m', '5m', '6m', '8m', '7p', '8p', '9p', '5S', '9s', '9s', '南', '白', '中'], p.get_tehai(type="array"))
		self.assertEqual("2m5m6m8m7p8p9p5S9s9s南白中", p.get_tehai("str"))

		haipai = ['1m', '3m', '7s', '5m', '東', '8m', '1p', '5P', '6p', '西', '7p', '3s', '8s']
		p.init_hand_with(haipai)
		self.assertEqual("1m3m5m8m1p5P6p7p3s7s8s東西", p.get_tehai("str"))
		

	def test_tsumo_discard(self):
		self.log.info("test_tsumo start.")
		haipai = ['1m', '3m', '7s', '5m', '東', '8m', '1p', '5P', '6p', '西', '7p', '3s', '8s']
		tsumo = "南"
		from player import Player as p
		p = p()
		p.init_hand_with(haipai)
		p.tsumo(tsumo)
		self.assertEqual("1m3m5m8m1p5P6p7p3s7s8s東南西", p.get_tehai("str"))
		
		p.discard("南")
		self.assertEqual("1m3m5m8m1p5P6p7p3s7s8s東西", p.get_tehai("str"))
	
	def test_check_agari(self):
		self.log.info("test_check_agari start.")
		haipai = "1m3m2p3p4p5P6p7p6s7s8s東東"
		from player import Player as p
		p = p()
		p.init_hand_with(haipai, type="str")
		
		machi = p.calc_machi()
		print(machi)

		#p.tsumo("2m")
		#agari, mentsu = p.check_agari()
		#self.assertTrue(agari)
		#self.assertEqual(['1m2m3m', 1, '2p3p4p', 12, '5p6p7p', 15, '6s7s8s', 26, '東東', 30], mentsu)
		
		#p.tsumo("2m")
		#agari, mentsu = p.check_agari()
		#self.assertFalse(agari)
		#self.assertEqual([], mentsu)
		
		#1:東[1m3m2p3p4p5P6p7p6s7s8s東東]
		#[0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
		# 1, 0, 1, 1, 1, 0, 1, 1, 0, 0,
		#  0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
		#   2, 0, 0, 0, 0, 0, 0]
		#2:南[2m2m2m3m4m5p5p6p7p8p5s6s7s]
		#3:西[5m6m7m6p6p7p8p9p9p9p9p5S6s]
		#4:北[1p1p1p3p3p2s5s8s8s8s北北北]
	"""

	def test_check_machi(self):
		self.log.info("test_check_machi start.")
		from player import Player as p
		p = p()
		#"""
		haipai = "1m3m2p3p4p5P6p7p6s7s8s東東"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([2], machi)

		haipai = "2m2m2m3m4m5p5p6p7p8p5s6s7s"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([2,5,15], machi)

		haipai = "5m6m7m6p6p7p8p9p9p9p9p5S6s"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([24,27], machi)
		
		haipai = "1p1p1p3p3p2s5s8s8s8s北北北"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([], machi)

		haipai = "1m1m1m2m3m4m5m6m7m8m9m9m9m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], machi)
		
		haipai = "1m9m1s9s1p9p東南西北白発中"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual(p.YAOCHU, machi)
		
		haipai = "9m9m1s9s1p9p東南西北白発中"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([1], machi)

		haipai = "2p2p3p3p4p4p5p5p6p6p7p7p8p"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([12,15,18], machi)
		#"""

		haipai = "2m2m2m3m4m白白白発発発中中"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([2,5,36], machi)
		
		#print(machi)
		#for hai in machi:
		#print(p.TABLE[hai])
	
	"""
	def test_nanimachi(self):
		self.log.info("test_nanimachi start.")
		from player import Player as p
		p = p()

		haipai = "1m1m1m2m1p2p3p1s2s3s南南南"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([2,3], machi)

		haipai = "2p3p3p3p6p6p7p7p8p8p3m3m3m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([11,12,14], machi)
		
		haipai = "2p3p4p5p6p8p8p8p9p9p3m3m3m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([11,14,17], machi)
		
		haipai = "2p3p4p4p4p5p6p8p8p8p3m3m3m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([11,14,17], machi)
	
		haipai = "2p3p4p5p6p7p7p9p9p9p3m3m3m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([11,14,17, 18], machi)
		
		haipai = "2p2p3p3p4p4p5p5p8p8p3m3m3m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([12,15,18], machi)
		
		haipai = "1p2p2p2p3p3p3p3m3m3m5m5m5m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([11,12,13], machi)

		haipai = "2p2p2p3p4p5p6p3m3m3m5m5m5m"
		print(haipai)
		p.init_hand_with(haipai, type="str")
		machi = p.calc_machi()
		self.assertEqual([11,13,14,16,17], machi)
	"""

	"""
	def test_set_machi_of_kokushi(self):
		self.log.info("test_set_machi_of_kokushi start.")
		from player import Player as p
		p = p()
		
		machi = []
		haipai = "1m9m1s9s1p9p東南西北白発中"
		p.init_hand_with(haipai, type="str")
		machi = p.set_machi_of_kokushi(machi)
		self.assertEqual(p.YAOCHU, machi)

		machi = []
		haipai = "9m9m1s9s1p9p東南西北白発中"
		p.init_hand_with(haipai, type="str")
		machi = p.set_machi_of_kokushi(machi)
		self.assertEqual([1], machi)


		#print(machi)
		#for hai in machi:
		#	print(p.TABLE[hai])
	
		self.log.info("test_set_machi_of_kokushi finished.")
	"""
	"""
	def test_set_machi_of_chitoitsu(self):
		self.log.info("test_set_machi_of_chitoitsu start.")
		from player import Player as p
		p = p()
		
		machi = []
		haipai = "2p2p3p3p4p4p5p5p6p6p7p7p8p"
		p.init_hand_with(haipai, type="str")
		machi = p.set_machi_of_chitoitsu(machi)
		self.assertEqual([18], machi)

		machi = []
		haipai = "1m1m1m2m3m4m5m6m7m8m9m9m9m"
		p.init_hand_with(haipai, type="str")
		machi = p.set_machi_of_chitoitsu(machi)
		self.assertEqual([], machi)
	"""

	#def test_set_machi_of_chitoitsu(self):
	#	self.log.info("test_set_machi_of_chitoitsu start.")
	#	self.log.info("test_set_machi_of_chitoitsu finished.")

	#1m2m3m5M7m4p5p4s4s東東発

try:
	if __name__ == '__main__':
		unittest.main()
except Exception as e:
	#import traceback
	#traceback.print_exc()
	import sys, os
	sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
	import sys,os
	from log import Log as l
	log = l.getLogger()
	log.error("error")
	log.error(str(type(e)))
	log.error(str(e.args))
	log.error(e.message)
