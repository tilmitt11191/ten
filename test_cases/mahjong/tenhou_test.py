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
	
	
	def test_get_final_tehai_from_sample3txt(self):
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
		self.assertEqual(correct_tehai, t.players[0].get_tehai(type="array"))
		
		self.assertEqual("2", t.players[1].id)
		self.assertEqual("南", t.players[1].seki)
		correct_tehai = ['2m', '2m', '3m', '6p', '7p', '1s', '2s', '3s', '4s', '4s', '6s', '北', '発']
		self.assertEqual(correct_tehai, t.players[1].get_tehai(type="array"))

	def test_simulate_sample1txt(self):
		self.log.info("test_simulate_sample1txt start.")
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
		with codecs.open('sample1.txt', 'w', 'cp932') as f:
			f.write(sample)
		from tenhou import Tenhou as tenhou
		t = tenhou()
		t.simulate_logfile("sample1.txt", "cp932", output_codec="cp932", output_format=["player", "tsumo", "player_machi", "player_tehai"], output_file_suffix="csv")
		self.log.info("test_simulate_sample1txt finished.")


	def test_simulate_sample12xt(self):
		self.log.info("test_simulate_sample2txt start.")

		sample2 = \
			"===== 天鳳 L0000 鳳南喰赤 開始 2015/12/31 http://tenhou.net/0/?log=2015123123gm-00a9-0000-e7914a2e&tw=0 =====\n"\
			"  東1局 1本場(リーチ2)  ガミゴン -1300 ネームレス７ 3300\n"\
			"    30符1000点1飜ロン 断幺九1\n"\
			"    [1東]5m6m8m5p7p9p3s4s5s6s9s東発\n"\
			"    [2南]6m9m9m1p1p6p7p1s6s9s9s北中\n"\
			"    [3西]2m3m3m5M7m4p5p9p4s4s南西北\n"\
			"    [4北]1m3m4m5m2p2p5p4s7s西北白中\n"\
			"    [表ドラ]6p [裏ドラ]\n"\
			"    * 1G8s 1d発 2G白 2d北 3G9s 3d南 4G1m 4d西 1G西 1D西 2G8s 2d1s 3G1m 3d西\n"\
			"    * 4G4p 4d北 1G3m 1d9s 2G2p 2d中 3G8s 3d北 4G8p 4d中 1G3p 1d東 2G5s 2d白\n"\
			"    * 3G東 3d9p 4G2m 4d白 1G6p 1d9p 2G1s 2D1s 3G白 3D白 4G南 4D南 1G2s 1d8s\n"\
			"    * 2G8p 2d6m 3G東 3d8s 4G7s 4d1m 1G8m 1d3m 2G6m 2D6m 3C5M7m 3d3m 4G6m 4d4s\n"\
			"    * 1G8m 1d3p 2G7p 2d8s 3G発 3d9s 4G南 4D南 1G6p 1d6p 2G1s 2D1s 3G4m 3D4m\n"\
			"    * 4G2m 4D2m 1G7p 1D7p 2G2m 2D2m 3G9p 3D9p 4G中 4D中 1G西 1D西 2G白 2D白\n"\
			"    * 3G2s 3D2s 4G7m 4d1m 1G1m 1D1m 2G8p 2d9s 3G7s 3D7s 4N7s7s 4d8p 1G3p 1D3p\n"\
			"    * 4A\n\n"

		import codecs
		with codecs.open('sample2.txt', 'w', 'cp932') as f:
			f.write(sample2)

		from tenhou import Tenhou as tenhou
		t = tenhou()
		t.simulate_logfile("sample2.txt", "cp932", output_codec="cp932", output_format=["player", "tsumo", "player_machi", "player_tehai"], output_file_suffix="csv")
		self.log.info("test_simulate_sample1txt finished.")

	def test_simulate_sample14xt(self):
		self.log.info("test_simulate_sample4txt start.")

		from tenhou import Tenhou as tenhou
		t = tenhou()
		t.simulate_logfile("sample4.txt", "cp932", output_codec="cp932", output_format=["player", "tsumo", "player_machi", "player_tehai"], output_file_suffix="csv")
		self.log.info("test_simulate_sample4txt finished.")

	def test_simulate_sample15xt(self):
		self.log.info("test_simulate_sample5txt start.")

		from tenhou import Tenhou as tenhou
		t = tenhou()
		t.simulate_logfile("sample5.txt", "cp932", output_codec="cp932", output_format=["player", "tsumo", "player_machi", "player_tehai"], output_file_suffix="csv")
		self.log.info("test_simulate_sample5txt finished.")

	def test_simulate_sample16xt(self):
		self.log.info("test_simulate_sample5txt start.")

		from tenhou import Tenhou as tenhou
		t = tenhou()
		t.simulate_logfile("sample6.txt", "cp932", output_codec="cp932", output_format=["player", "tsumo", "player_machi", "player_tehai"], output_file_suffix="csv")
		self.log.info("test_simulate_sample6txt finished.")
	
	

"""
2017-03-20 23:08:43,570 - ERROR - tehai !=13[12]
2017-03-20 23:08:43,570 - ERROR - tehai[1m2m3m5M7m4p5p4s4s東東発]
2017-03-20 23:08:43,619 - ERROR - tehai !=13[12]
2017-03-20 23:08:43,619 - ERROR - tehai[1m2m3m5M7m4p5p4s4s東東発]
2017-03-20 23:08:43,758 - ERROR - tehai !=13[12]
2017-03-20 23:08:43,759 - ERROR - tehai[1m2m3m5M7m4p5p4s4s東東発]
2017-03-20 23:08:43,821 - ERROR - tehai !=13[12]
2017-03-20 23:08:43,822 - ERROR - tehai[1m2m3m5M7m4p5p4s4s東東発]
2017-03-20 23:08:43,861 - ERROR - tehai !=13[12]
2017-03-20 23:08:43,862 - ERROR - tehai[1m2m3m5M7m4p5p4s4s東東発]
2017-03-20 23:08:44,366 - ERROR - tehai !=13[12]
2017-03-20 23:08:44,367 - ERROR - tehai[4m6m6m7m8m4p5p2s4s5s6s7s]
2017-03-20 23:08:44,415 - ERROR - tehai !=13[12]
2017-03-20 23:08:44,416 - ERROR - tehai[4m6m6m6m7m8m4p5p4s5s6s7s]
2017-03-20 23:08:44,528 - ERROR - tehai !=13[12]
2017-03-20 23:08:44,535 - ERROR - tehai[4m6m6m6m7m8m4p5p4s5s6s7s]
2017-03-20 23:08:45,868 - ERROR - tehai !=13[12]
2017-03-20 23:08:45,868 - ERROR - tehai[6m7m4p4p3s3s3s4s4s4s5S5s]

===== 天鳳 L0000 鳳南喰赤 開始 2015/12/31 http://tenhou.net/0/?log=2015123123gm-00a9-0000-ccc346e2&tw=0 =====
* 1G5p 1d南 2G北 2d1p 3G4p 3d9p 4G中 4d東 1G3s 1d北 2G2m 2d東 3G1p 3d北
* 4G北 4D北 1G1s 1D1s 2G3m 2d北 3G9m 3D9m 4G2p 4d9s 1G南 1D南 2G東 2D東
* 3G3p 3d白 4G5m 4d1m 1G西 1D西 2N西西 2d5s 3G2p 3d4p 4G中 4d9p 1G4s 1d1s
* 2G5m 2d7p 3G8p 3D8p 4G2s 4d8m 1G6s 1D6s 2G東 2d8s 3G白 3D白 4G9p 4D9p
* 1G発 1D発 2G9p 2D9p 3G8s 3R 3d7s 4G2s 4d1s 1G西 1D西 2G8m 2d東 3G7p
* 3D7p 4G8m 4d8p 1G9m 1R 1d4s 2G6s 2d9s 3G1m 3D1m 4G5p 4d7s 1G発 1D発
* 2G6s 2d6s 3G4s 3D4s 4G3m 4d6s 1G8p 1D8p 2G5s 2d6s 3G白 3D白 4G4m 4d2p
* 1G1p 1D1p 2G4m 2d5s 3G3s 3D3s 4G3s 4D3s 1G2m 1D2m 2G4p 2d2m 3G3m 3D3m
* 4G9m 4d3m 1G南 1D南 2G5M 2d2m 3G6p 3D6p 1A

* 1G3m 1d西 2G1m 2d西 3G7s 3d4m 4G白 4d南 1G中 1d1p 2G9m 2d南 3G4s 3d9p
* 4G7p 4d1s 1G北 1d9s 2G6p 2D6p 3G4s 3d東 4G9s 4d白 1G6p 1d9p 2G6p 2D6p
* 3G4s 3d4p 4G8m 4d北 1G5p 1d8p 2G2p 2d5s 3G7s 3d7m 4G発 4D発 1G発 1d北


* 4G9s 4d9m 1G東 1d1s 2G4s 2D4s 3G6p 3d3s 4G4p 4d3s 1G4m 1d東 2G7m 2D7m
* 3G白 3d6p 4G3p 4d6s 1G4p 1d6p 2G発 2D発 3G8p 3D8p 4G9m 4D9m 1G7p 1d6s
* 2C4s5s 2d2m 3G2s 3d白 4G南 4d7s 1G5p 1d7p 2G南 2D南 3G西 3D西 4G2p 4d南


#* 1G3s 1K白 1G8p 1D8p 2G南 2d5s 3G3m 3d8s 4G2p 4D2p 1G1m 1d8m 2G4m 2d9m

2017-03-25 15:16:09,697 - DEBUG - line[西1局 0本場(リーチ0)  ヤコブコーエン 13000 寸ちゃん -12000]
2017-03-25 15:16:09,697 - DEBUG - line[満貫ロン 断幺九1 ドラ1 赤ドラ3]
2017-03-25 15:16:09,697 - DEBUG - line[[1東]6m7m8m3p3p5P5p2s7s8s南白中]
2017-03-25 15:16:09,698 - DEBUG - haipai start.
2017-03-25 15:16:09,698 - INFO - create_player([1東]6m7m8m3p3p5P5p2s7s8s南白中) start.





2017-03-25 15:16:12,484 - DEBUG - line[[表ドラ]3s [裏ドラ]]
2017-03-25 15:16:12,484 - DEBUG - line[* 1G1p 1d南 2G4s 2d北 3G4s 3d西 4G6p 4d発 1G9s 1d中 2G南 2D南 3G1m 3D1m]
2017-03-25 15:16:12,484 - DEBUG - action start.
2017-03-25 15:16:12,484 - DEBUG - action * start.
2017-03-25 15:16:12,484 - DEBUG - action 1G1p start.
2017-03-25 15:16:12,484 - DEBUG - action means tsumo
2017-03-25 15:16:12,484 - DEBUG - player[1] drew 1p
2017-03-25 15:16:12,484 - DEBUG - tehai:1m1m2m2m3m3m1p1p3p4p5p3s4s
2017-03-25 15:16:12,484 - INFO - player[1]_tsumo[1p] start.
2017-03-25 15:16:12,485 - DEBUG - player.id[1], id[1]
2017-03-25 15:16:12,485 - INFO - player.tsumo[1p] start.
2017-03-25 15:16:12,485 - DEBUG - result.size[5]
2017-03-25 15:16:12,485 - DEBUG - action 1d南 start.
2017-03-25 15:16:12,485 - DEBUG - action means tedashi
2017-03-25 15:16:12,485 - INFO - player[1]_discard[南] start.
2017-03-25 15:16:12,486 - DEBUG - player.id[1], id[1]
2017-03-25 15:16:12,486 - INFO - player.discard[南] start.
2017-03-25 15:16:12,486 - ERROR - mottenai hai wo suteta
2017-03-25 15:16:12,486 - ERROR - discard[ 南, tehai[1m1m2m2m3m3m1p1p1p3p4p5p3s4s]
2017-03-25 15:16:12,486 - DEBUG - result.size[5]
2017-03-25 15:16:12,486 - INFO - calc_machi[1m1m2m2m3m3m1p1p1p3p4p5p3s4s]start


"""

if __name__ == '__main__':
	unittest.main()
