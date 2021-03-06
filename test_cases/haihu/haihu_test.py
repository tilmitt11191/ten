#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from pprint import pprint

class TestTenhouHaihu(unittest.TestCase):
	def setUp(self):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger()
		
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/haihu")
		self.log.debug("sys.path.append(" + os.path.dirname(os.path.abspath(__file__)) + "/../../lib/haihu)")

		
	def test_get_tsumo_from_sample1txt(self):
		self.log.info("test_get_tsumo_from_sample1txt start.")

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
			"    * 3G2p 3D2p 4G2s 4d4m 1G4m 1D4m\n\n"\
			"  東1局 1本場(リーチ2)  ガミゴン -1300 ネームレス７ 3300"
			
		correct_result = ["東1局 0本場(リーチ0)  ガミゴン 1000 愛内里菜 1000 ranu- 1000 ネームレス７ -3000", "1,南,tsumogiri", "2,7s,tedashi", "1,東,tedashi", "2,4p,tedashi", "3,1p,tedashi", "4,5m,tsumogiri", "1,4p,tedashi", "2,5M,tedashi", "3,2p,tedashi", "4,8p,tedashi", "1,6s,tedashi", "2,5p,tedashi", "3,6s,tedashi", "4,5s,tsumogiri", "1,2p,tedashi", "2,5s,tedashi", "3,9p,tedashi", "4,3p,tedashi", "1,西,tsumogiri", "2,7p,tsumogiri", "3,6p,tedashi", "4,1p,tedashi", "1,中,tsumogiri", "2,3m,tsumogiri", "3,9m,tsumogiri", "4,9m,tsumogiri", "1,9s,tsumogiri", "2,9m,tsumogiri", "3,発,tsumogiri", "4,2s,tsumogiri", "1,南,tsumogiri", "2,2p,tsumogiri", "3,7m,tedashi", "4,8s,tedashi","1,3p,tedashi,reach", "2,2m,tedashi", "3,7m,tedashi", "4,2s,tedashi", "1,4p,tsumogiri", "2,5p,tedashi", "3,6p,tedashi", "4,中,tsumogiri", "1,発,tsumogiri", "2,6m,tedashi", "3,1m,tsumogiri", "4,9s,tedashi", "1,白,tsumogiri", "2,8m,tsumogiri", "3,6m,tsumogiri", "4,白,tedashi", "1,4s,tsumogiri", "2,8p,tedashi", "3,9p,tedashi", "1,4m,tsumogiri", "2,中,tsumogiri", "3,9m,tsumogiri", "4,西,tsumogiri", "1,7m,tsumogiri", "2,1m,tedashi", "3,9p,tedashi,reach", "4,5s,tedashi", "1,白,tsumogiri", "2,南,tsumogiri", "3,1s,tsumogiri", "4,4m,tedashi", "1,6s,tsumogiri", "2,4m,tedashi", "3,2p,tsumogiri", "4,2s,tedashi", "1,4m,tsumogiri", "東1局 1本場(リーチ2)  ガミゴン -1300 ネームレス７ 3300"]
		    
		
		import codecs
		with codecs.open('sample.txt', 'w', 'shift-jis') as f:
			f.write(sample)

		import tenhou
		t = tenhou.Tenhou()
		output = t.get_tsumo_from("sample.txt", "shift-jis")
		
		#self.assertEqual(output, correct_result)
		self.log.info("test_get_tsumo_from_sample1txt finished.")
	


	def test_get_tsumo_from_sample2txt(self):
		self.log.info("test_get_tsumo_from_sample2txt start.")
		import tenhou
		t = tenhou.Tenhou()
		#output = t.get_tsumo_from("sample2.txt", "shift-jis")
		output = t.get_tsumo_from("sample2.txt", "cp932")
		self.log.info("test_get_tsumo_from_sample2txt finished.")
	

if __name__ == '__main__':
	unittest.main()













