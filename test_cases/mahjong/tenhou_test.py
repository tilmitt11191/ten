#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
class File_manager_test(unittest.TestCase):
	log = ""
	@classmethod
	def setUpClass(cls):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		l = l()
		cls.log = l.getLogger()
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/haihu")
		
		cls.log.info("\n\nFile_manager_test setUpClass finished.\n---------- start ---------")
	
	
	def setUp(self):
		pass
	
	"""	
	def test_player_tsumo(self):
		import tenhou
		t = tenhou.Tenhou()
		#line = "[1東]1m3m5m8m1p5P6p7p3s7s8s東西"
		line = "[1東]1m3m7s5m東8m1p5P6p西7p3s8s"
		t.create_player(line)
		line = "[2南]2m2m3m6p7p1s2s3s4s4s6s北発"
		t.create_player(line)
		line = "[3西]2m5m6m8m7p8p9p5S9s9s南白中"
		t.create_player(line)
		line = "[4北]7m8m1p3p1s7s8s8s東東西北北"
		t.create_player(line)
		t.player_tsumo("1", "南")
		self.assertEqual("1m3m5m8m1p5P6p7p3s7s8s東南西", t.players[0].get_tehai("str"))
		#['1m', '3m', '7s', '5m', '東', '8m', '1p', '5P', '6p', '西', '7p', '3s', '8s']
		#['1m', '1p', '3m', '3s', '5P', '5m', '6p', '7p', '7s', '8m', '8s', '東', '西']		
	"""
	
	
	
	
	
	def test_simlate_sample1txt(self):
		self.log.info("simlate_sample1txt start.")
		
		sample = \
			"===== 天鳳 L0000 鳳南喰赤 開始 2015/12/31 http://tenhou.net/0/?log=2015123123gm-00a9-0000-e7914a2e&tw=0 =====\n"\
			"  持点25000 [1]ガミゴン/七段/男 R2104 [2]愛内里菜/八段/女 R2139 [3]ranu-/八段/男 R2185 [4]ネームレス７/七段/女 R2053\n"\
			"  東1局 0本場(リーチ0)  ガミゴン 1000 愛内里菜 1000 ranu- 1000 ネームレス７ -3000\n"\
			"    流局\n"\
			"    [1東]1m3m5m8m1p5P6p7p3s7s8s東西\n"\
			"    [2南]2m2m3m6p7p1s2s3s4s4s6s北発\n"\
			"    [3西]2m5m6m8m7p8p9p5S9s9s南白中\n"\
			"    [4北]7m8m1p3p1s7s8s8s東東西北北\n"\
			"    [表ドラ]8p [裏ドラ]\n"\
			"    * 1G南 1D南 2G7s 2d北 4N北北 4d1s 1G東 1d西 2G4p 2d発 3G1p 3d南 4G5m 4D5m\n"\
			"    * 1G4p 1d1p 2G5M 2d4p 3G2p 3d白 4G8p 4d西 1G6s 1d8m 2G5p 2d4s 3G6s 3d8m\n"\
			"    * 4G5s 4D5s 1G2p 1d3s 2G5s 2d1s 3G9p 3d2m 4G3p 4d8p 1G西 1D西 2G7p 2D7p\n"\
			"    * 3G6p 3d中 4G1p 4d7m 1G中 1D中 2G3m 2D3m 3G9m 3D9m 4G9m 4D9m 1G9s 1D9s\n"\
			"    * 2G9m 2D9m 3G発 3D発 4G2s 4D2s 1G南 1D南 2G2p 2D2p 3G7m 3d9s 4G8s 4d7s\n"\
			"    * 1G3p 1R 1d5m 2G2m 2d5M 3G7m 3d9s 4G2s 4d8m 1G4p 1D4p 2G5p 2d3s 3G6p\n"\
			"    * 3d7m 4G中 4D中 1G発 1D発 2G6m 2d2s 3G1m 3D1m 4G9s 4d2s 1G白 1D白 2G8m\n"\
			"    * 2D8m 3G6m 3D6m 4G白 4d9s 1G4s 1D4s 2G8p 2d4s 3G9p 3d1p 4N1p1p 4d白 1G4m\n"\
			"    * 1D4m 2G中 2D中 3G9m 3D9m 4G西 4D西 1G7m 1D7m 2G1m 2d6m 3G9p 3R 3d2p\n"\
			"    * 4G5s 4d東 1G白 1D白 2G南 2D南 3G1s 3D1s 4G4m 4d東 1G6s 1D6s 2G4m 2d1m\n"\
			"    * 3G2p 3D2p 4G2s 4d4m 1G4m 1D4m\n\n"
		import codecs
		with codecs.open('sample3.txt', 'w', 'shift-jis') as f:
			f.write(sample)

		import tenhou
		t = tenhou.Tenhou()
		output = t.get_tsumo_from("sample3.txt", "shift-jis")

		
		#1:東[1m3m2p3p4p5P6p7p6s7s8s東東]
		#2:南[2m2m2m3m4m5p5p6p7p8p5s6s7s]
		#3:西[5m6m7m6p6p7p8p9p9p9p9p5S6s]
		#4:北[1p1p1p3p3p2s5s8s8s8s北北北]
		self.assertEqual(4, len(t.players))
		self.assertEqual("1m3m2p3p4p5P6p7p6s7s8s東東", t.players[0].get_tehai("str"))
		self.assertEqual("2m2m2m3m4m5p5p6p7p8p5s6s7s", t.players[1].get_tehai("str"))
		self.assertEqual("5m6m7m6p6p7p8p9p9p9p9p5S6s", t.players[2].get_tehai("str"))
		self.assertEqual("1p1p1p3p3p2s5s8s8s8s北北北", t.players[3].get_tehai("str"))

		self.log.info("simlate_sample1txt finished.")

	"""
	def test_init(self):
		self.log.info("test_init start.")
		import tenhou
		t = tenhou.Tenhou()

		
		self.log.info("test_init finished.")

	def test_convert_strtehai_to_arr(self):
		self.log.info("test_convert_strtehai_to_arr start.")
		
		import tenhou
		t = tenhou.Tenhou()
		tehai_str = "1m3m5m8m1p5P6p7p3s7s8s東西"
		tehai_arr = t.convert_strtehai_to_arr(tehai_str)
		#from pprint import pprint
		#pprint(tehai_arr)
		correct_tehai = ['1m', '3m', '5m', '8m', '1p', '5P', '6p', '7p', '3s', '7s', '8s', '東', '西']
		self.assertEqual(correct_tehai, tehai_arr)
	
	
	def test_create_player(self):
		self.log.info("test_create_player start.")
		
		import tenhou
		t = tenhou.Tenhou()
		line = "[1東]1m3m5m8m1p5P6p7p3s7s8s東西"
		t.create_player(line)
		line = "[2南]2m2m3m6p7p1s2s3s4s4s6s北発"
		t.create_player(line)

		self.assertEqual(2, len(t.players))
		
		self.assertEqual("1", t.players[0].id)
		self.assertEqual("東", t.players[0].seki)
		correct_tehai = ['1m', '3m', '5m', '8m', '1p', '5P', '6p', '7p', '3s', '7s', '8s', '東', '西']
		self.assertEqual(correct_tehai, t.players[0].tehai)
		
		self.assertEqual("2", t.players[1].id)
		self.assertEqual("南", t.players[1].seki)
		correct_tehai = ['2m', '2m', '3m', '6p', '7p', '1s', '2s', '3s', '4s', '4s', '6s', '北', '発']
		self.assertEqual(correct_tehai, t.players[1].tehai)
	"""










if __name__ == '__main__':
	unittest.main()
