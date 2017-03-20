#!/usr/bin/python
# -*- coding: utf-8 -*-

class Player:

	TABLE = {0:"5M",1:"1m",2:"2m",3:"3m",4:"4m",5:"5m",6:"6m",7:"7m",8:"8m",9:"9m",
			10:"5P",11:"1p",12:"2p",13:"3p",14:"4p",15:"5p",16:"6p",17:"7p",18:"8p",19:"9p",
			20:"5S",21:"1s",22:"2s",23:"3s",24:"4s",25:"5s",26:"6s",27:"7s",28:"8s",29:"9s",
			30:"東", 31:"南", 32:"西", 33:"北", 34:"白", 35:"発", 36:"中"}

	TABLE_INV = {'8m': 8, '北': 33, '8s': 28, '2m': 2, '3s': 23, '6s': 26, '中': 36, '4s': 24, '5m': 5, '7p': 17, '東': 30, '7m': 7, '2p': 12, '発': 35, '5s': 25, '4p': 14, '南': 31, '3m': 3, '7s': 27, '5S': 20, '4m': 4, '2s': 22, '5P': 10, '3p': 13, '白': 34, '5M': 0, '9p': 19, '9m': 9, '9s': 29, '6p': 16, '1p': 11, '6m': 6, '1m': 1, '1s': 21, '5p': 15, '西': 32, '8p': 18}
	
	NARABI = [1,2,3,4,0,5,6,7,8,9,
		11,12,13,14,10,15,16,17,18,19,
		21,22,23,24,20,25,26,27,28,29,
		30,31,32,33,34,35,36]
		
	YAOCHU = [1,9,11,19,21,29,30,31,32,33,34,35,36]

	def __init__(self):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger()
		self.log.info("Player.__init__")
		
		self.tehai = [0]*37
		self.machi = []
		self.seki = ""
		self.id = "" #[1-4]

	def init_hand_with(self, haipai, type="str"):
		self.log.info("init_hand_with("+str(haipai)+ ", " + type +")")
		self.tehai = [0]*37
		if type == "str":
			tmp = haipai.replace("m", "m,")\
			.replace("p", "p,")\
			.replace("s", "s,")\
			.replace("M", "M,")\
			.replace("P", "P,")\
			.replace("S", "S,")\
			.replace("東", "東,")\
			.replace("南", "南,")\
			.replace("西", "西,")\
			.replace("北", "北,")\
			.replace("白", "白,")\
			.replace("発", "発,")\
			.replace("中", "中,")
			tmp = tmp[:-1]
			haipai_arr = tmp.split(",")
			self.init_hand_with(haipai_arr, type="array")

		elif type == "array":
			for hai in haipai:
				self.tehai[Player.TABLE_INV[hai]] += 1
		self.machi = []
		
	def haipai(self, haipai, haipai_type):
		self.log.info("player.haipai start.")
		
	def tsumo(self, hai):
		self.log.info("player.tsumo[{hai}] start.".format(**locals()))
		self.tehai[Player.TABLE_INV[hai]] += 1
		
	def discard(self, hai):
		self.log.info("player.discard[{hai}] start.".format(**locals()))
		if self.tehai[Player.TABLE_INV[hai]] < 1:
			self.log.error("mottenai hai wo suteta")
		else:
			self.tehai[Player.TABLE_INV[hai]] -= 1
		
	def get_tehai(self, type="str"):
		if type == "str":
			result = ""
		elif type == "array":
			result = []
		for hai_inv in self.NARABI:
			hai = Player.TABLE[hai_inv]
			number_of_hai = self.tehai[hai_inv]
			#self.log.debug("hai[" + hai + "]*number[" + str(number_of_hai) + "]")
			if number_of_hai > 0:
				if type == "str":
					result += (hai)*number_of_hai
				elif type == "array":
					result.extend([hai]*number_of_hai)
		return result
	
	
	def count_tehai(self):
		count = 0
		for num_of_hai in self.tehai:
			count += num_of_hai
		return count

	
	def print_tehai(self):
		from pprint import pprint
		pprint(self.tehai)
	def print_machi(self):
		from pprint import pprint
		pprint(machi)
		
	#def get_machihai
		#machi = Mahjong.get_machihai(tehai)
		#return Mahjong.reconvert_tehai(machi)
		
	
	
	
	def pick_up_mentsu(self, mentsu, machi, pointer_mentsu):
		for i in range(37):
			self.log.debug("pick_up_mentsu[" + str(i) + "][" + self.get_tehai(type="str") +"], mentsu[" + str(mentsu) + "]")
			if i >= 36:
			#if i >= 38:
				if mentsu[9] != 0:
					##AGARI!
					self.log.debug("mentsu[9]!=0.break.")
					return 1, mentsu
				self.log.debug("i>=38. pick_up_mentsu finished.")
				return 1, mentsu

			if self.tehai[i] < 1:
				continue
			
			self.log.info("pointer_mentsu[{pointer_mentsu}]".format(**locals()))
			
			##pick up ANKO
			if self.tehai[i] >= 3:
				self.tehai[i] -= 3
				hai = Player.TABLE[i]*3
				mentsu[pointer_mentsu] = hai
				mentsu[pointer_mentsu + 1] = i
				pointer_mentsu +=2
				self.log.debug("recursive call ANKO start")
				agari, mentsu = self.pick_up_mentsu(mentsu, machi, pointer_mentsu) ##recursive call
				self.log.debug("recursive call ANKO finished.")
				if agari: return(agari, mentsu)
				pointer_mentsu -=2
				mentsu[pointer_mentsu] = 0
				mentsu[pointer_mentsu + 1] = 0
				self.tehai[i] +=3
				
			##pick up SYUNTSU
			if self.tehai[i] and self.tehai[i+1] and self.tehai[i+2] and i < 30:
				self.tehai[i] -= 1
				self.tehai[i+1] -= 1
				self.tehai[i+2] -= 1
				hai = Player.TABLE[i] + Player.TABLE[i+1] + Player.TABLE[i+2]
				self.log.debug("pick up SYUNTSU[" + hai + "]")
				mentsu[pointer_mentsu] = hai
				mentsu[pointer_mentsu + 1] = i
				pointer_mentsu +=2
				self.log.debug("recursive call SYUNTSU start")
				agari, mentsu = self.pick_up_mentsu(mentsu, machi, pointer_mentsu) ##recursive call
				self.log.debug("recursive call SYUNTSU finished.")
				if agari: return(agari, mentsu)

				pointer_mentsu -=2
				mentsu[pointer_mentsu] = 0
				mentsu[pointer_mentsu + 1] = 0
				self.tehai[i] += 1
				self.tehai[i+1] += 1
				self.tehai[i+2] += 1
			##pick up JANTOU
			if self.tehai[i] >= 2:
				self.tehai[i] -= 2
				hai = Player.TABLE[i]*2
				mentsu[pointer_mentsu] = hai
				mentsu[pointer_mentsu + 1] = i
				pointer_mentsu +=2
				self.log.debug("recursive call JANTOU start")
				agari, mentsu = self.pick_up_mentsu(mentsu, machi, pointer_mentsu) ##recursive call
				self.log.debug("recursive call JANTOU finished.")
				if agari: return(agari, mentsu)
				pointer_mentsu -=2
				mentsu[pointer_mentsu] = 0
				mentsu[pointer_mentsu + 1] = 0
				self.tehai[i] +=2
		self.log.debug("for loop finished.")
	
	
	
	def check_agari(self):
		self.log.info("check_agari[" + self.get_tehai(type="str") + "]start")
		if self.count_tehai() != 14:
			self.log.error("tehai !=14[" + str(self.count_tehai()) +"]")
			return 0, []
		
		agari = 0 #flag
		mentsu = [0]*10
		machi = []
		pointer_mentsu = 0
		
		red_manzu = 0
		if self.tehai[0]:
			red_manzu = self.tehai[0]
			self.tehai[5] += self.tehai[0]
			self.tehai[0] = 0
		red_souzu = 0
		if self.tehai[10]:
			self.tehai[15] += self.tehai[10]
			red_souzu = self.tehai[10]
			self.tehai[10] = 0
		red_pinzu = 0
		if self.tehai[20]:
			self.tehai[25] += self.tehai[20]
			red_pinzu = self.tehai[20]
			self.tehai[20] = 0
		
		agari, mentsu = self.pick_up_mentsu(mentsu, machi, pointer_mentsu)
		self.log.debug("pick_up_mentsu finished. mentsu returned.")
		
		if red_manzu:
			self.tehai[5] -= red_manzu
			self.tehai[0] = red_manzu
		if red_souzu:
			self.tehai[15] -= red_souzu
			self.tehai[10] = red_souzu
		if red_pinzu:
			self.tehai[25] -= red_pinzu
			self.tehai[20] = red_pinzu
		
		return(agari, mentsu)
		
		

	def calc_machi(self):
		self.log.info("calc_machi[" + self.get_tehai(type="str") + "]start")
		if self.tehai != 13:
			self.log.error("tehai !=13[" + str(len(self.tehai)))

		agari = 0 #flag
		mentsu = [0]*10
		machi = []
		pointer_mentsu = 0
		
		red_manzu = 0
		if self.tehai[0]:
			red_manzu = self.tehai[0]
			self.tehai[5] += self.tehai[0]
			self.tehai[0] = 0
		red_souzu = 0
		if self.tehai[10]:
			self.tehai[15] += self.tehai[10]
			red_souzu = self.tehai[10]
			self.tehai[10] = 0
		red_pinzu = 0
		if self.tehai[20]:
			self.tehai[25] += self.tehai[20]
			red_pinzu = self.tehai[20]
			self.tehai[20] = 0
		
		machi = self.get_machi_from_tehai(mentsu, machi, pointer_mentsu)
		self.log.debug("get_machi_from_tehai finished. machi returned.")
		self.machi = machi
		if red_manzu:
			self.tehai[5] -= red_manzu
			self.tehai[0] = red_manzu
		if red_souzu:
			self.tehai[15] -= red_souzu
			self.tehai[10] = red_souzu
		if red_pinzu:
			self.tehai[25] -= red_pinzu
			self.tehai[20] = red_pinzu
		
		return machi





	def get_machi_from_tehai(self, mentsu, machi, pointer_mentsu):
		tempai = 0
		if self.count_tehai() == 13:
			self.set_machi_of_kokushi(machi)
			self.set_machi_of_chitoitsu(machi)
		
		for i in range(38):
			self.log.debug("get_machi_from_tehai[" + str(i) + "], tehai[" + self.get_tehai(type="str") +"], mentsu[" + str(mentsu) + "]")
			if i >= 37:
			#if i >= 38:
				if self.count_tehai() <= 2:
					##TEMPAI!
					self.log.debug("count_tehai <= 2.tehai[" + self.get_tehai(type="str") + "]")
					machi = self.get_machi_of_mentsu_kouho(machi)
					#return tempai, machi
				self.log.debug("i>=38. get_machi_from_tehai finished. return machi"+str(machi))
				return machi

			if self.tehai[i] < 1:
				continue
			##pick up ANKO
			if self.tehai[i] >= 3:
				self.tehai[i] -= 3
				hai = Player.TABLE[i]*3
				mentsu[pointer_mentsu] = "ANKO"
				mentsu[pointer_mentsu + 1] = hai
				pointer_mentsu +=2
				self.log.debug("recursive call ANKO start")
				machi = self.get_machi_from_tehai(mentsu, machi, pointer_mentsu) ##recursive call
				self.log.debug("recursive call ANKO finished.")
				#if tempai: return(tempai, machi)
				pointer_mentsu -=2
				mentsu[pointer_mentsu] = 0
				mentsu[pointer_mentsu + 1] = 0
				self.tehai[i] +=3
				
			##pick up SYUNTSU
			if i < 30 and self.tehai[i] and self.tehai[i+1] and self.tehai[i+2]:
				self.tehai[i] -= 1
				self.tehai[i+1] -= 1
				self.tehai[i+2] -= 1
				hai = Player.TABLE[i] + Player.TABLE[i+1] + Player.TABLE[i+2]
				self.log.debug("pick up SYUNTSU[" + hai + "]")
				mentsu[pointer_mentsu] = "SYUNTSU"
				mentsu[pointer_mentsu + 1] = hai
				pointer_mentsu +=2
				self.log.debug("recursive call SYUNTSU start")
				machi = self.get_machi_from_tehai(mentsu, machi, pointer_mentsu) ##recursive call
				self.log.debug("recursive call SYUNTSU finished.")
				#if tempai: return(tempai, machi)

				pointer_mentsu -=2
				mentsu[pointer_mentsu] = 0
				mentsu[pointer_mentsu + 1] = 0
				self.tehai[i] += 1
				self.tehai[i+1] += 1
				self.tehai[i+2] += 1
			##pick up JANTOU
			if not "JANTOU" in mentsu and self.tehai[i] >= 2:
				self.tehai[i] -= 2
				hai = Player.TABLE[i]*2
				mentsu[pointer_mentsu] = "JANTOU"
				mentsu[pointer_mentsu + 1] = hai
				pointer_mentsu +=2
				self.log.debug("recursive call JANTOU start")
				machi = self.get_machi_from_tehai(mentsu, machi, pointer_mentsu) ##recursive call
				self.log.debug("recursive call JANTOU finished.")
				#if tempai: return(tempai, machi)
				pointer_mentsu -=2
				mentsu[pointer_mentsu] = 0
				mentsu[pointer_mentsu + 1] = 0
				self.tehai[i] +=2
		self.log.debug("for loop finished.")


		return machi

	def set_machi_of_kokushi(self, machi):
		self.log.debug("set_machi_of_kokushi start. tehai" + str(self.tehai))
		##3枚以上の牌があれば聴牌ではない
		if 3 in self.tehai or 4 in self.tehai:
			self.log.debug("set_machi_of_kokushi finished. 3or4 in tehai")
			return machi

		##么九牌の中で全部1枚ずつか1種0枚1種2枚他1枚なら聴牌
		##前者は么九牌が待ち、後者は0枚の牌が待ち。
		hai_of_0 = 0
		number_of_2 = 0
		for hai in self.YAOCHU:
			if self.tehai[hai] == 0:
				if hai_of_0 != 0: #0枚の牌が2種目なので聴牌ではない
					self.log.debug("set_machi_of_kokushi finished. 2 kind of hai are 0")
					return machi
				hai_of_0 = hai
			elif self.tehai[hai] == 2:
				if number_of_2 != 0: #2枚の牌が2種目なので聴牌ではない
					self.log.debug("set_machi_of_kokushi finished. 2 kind of hai are 2")
					return machi
				number_of_2 += 1

		if hai_of_0 == 0:
			self.log.debug("set_machi_of_kokushi add all yaochu")
			for hai in self.YAOCHU:
				machi = self.add_hai_to_machi(machi, hai)
		elif number_of_2 == 1:
			self.log.debug("set_machi_of_kokushi add lacked hai")
			machi = self.add_hai_to_machi(machi, hai_of_0)

		return machi

	
	def set_machi_of_chitoitsu(self,machi):
		self.log.debug("set_machi_of_chitoitsu start. tehai" + str(self.tehai))
		##3枚以上の牌があれば聴牌ではない
		if 3 in self.tehai or 4 in self.tehai:
			self.log.debug("set_machi_of_chitoitsu finished. 3or4 in tehai")
			return machi
		
		#1枚の牌1種と2枚の牌6種なら聴牌で1種の牌が待ち。
		hai_of_1 = 0
		number_of_2 = 0
		for hai in range(37):
			if self.tehai[hai] == 1:
				if hai_of_1 != 0: #0枚の牌が2種目なので聴牌ではない
					self.log.debug("set_machi_of_chitoitsu finished. 2 kind of hai are 1")
				hai_of_1 = hai
			elif self.tehai[hai] == 2:
				number_of_2 += 1
		
		if number_of_2 == 6:
			machi = self.add_hai_to_machi(machi, hai_of_1)
		
		return machi


	def get_machi_of_mentsu_kouho(self, machi):
		self.log.debug("get_machi_of_mentsu_kouho(" + str(machi) + ", " + self.get_tehai(type="str") + ")")
		if self.count_tehai() == 1:
			self.log.debug("kouho of JANTOU")
			machi = self.set_machi_of_jantou_kouho(machi, self.tehai.index(1))

		elif self.count_tehai() == 2:
			self.log.debug("kouho of mentsu")
			for i in range(37):
				if self.tehai[i] < 1:
					continue
				if self.is_anko_kouho(i):
					self.log.debug(Player.TABLE[i] + " is kouho of ANKO")
					machi = self.set_machi_of_anko_kouho(machi, i)
				elif self.is_syuntsu_kouho(i):
					self.log.debug(Player.TABLE[i] + " is kouho of SYUNTSU")
					self.set_machi_of_syuntsu_kouho(machi, i)


		else:
			self.log.error("kouho ERROR at get_machi_of_mentsu_kouho")
			
		self.log.debug("get_machi_of_mentsu_kouho(" + str(machi) + ", " + self.get_tehai(type="str") + ") finished. return " + str(machi))
		return machi


	def set_machi_of_jantou_kouho(self, machi, i):
		if self.tehai[i] == 1:
			machi = self.add_hai_to_machi(machi, i)
		return machi

	def set_machi_of_anko_kouho(self, machi, i):
		if self.tehai[i] == 2:
			machi = self.add_hai_to_machi(machi, i)
		return machi

	def set_machi_of_syuntsu_kouho(self, machi, i):
		if self.tehai[i] and self.tehai[i+1]:
			self.log.debug("ryanmen")
			if i-1 < 30 and i-1 > 0 and i-1 !=10 and i-1 !=20:
				machi = self.add_hai_to_machi(machi, i-1)
			if i+2 < 30 and i+2 > 0 and i+2 !=10 and i+2 !=20:
				machi = self.add_hai_to_machi(machi, i+2)
		elif self.tehai[i] and self.tehai[i+2]:
			self.log.debug("kanchan")
			machi = self.add_hai_to_machi(machi, i+1)
		
		return machi
	
	def add_hai_to_machi(self, machi, hai):
		self.log.debug("add " + Player.TABLE[hai] + " to machi" + str(machi))
		if hai in machi:
			self.log.debug(str(hai) + " is already in machi. nothing to do")
		else:
			self.log.debug(str(hai) + " is not in machi. add.")
			import bisect
			bisect.insort(machi, hai)
		
		return machi


	def is_anko_kouho(self, i):
		self.log.debug("is_anko_kouho start")
		return (self.tehai[i] >= 2)


	def is_syuntsu_kouho(self, i):
		if i >= 30 or i == 0 or 8 <= i <= 10 or 18<=i<=20 or 28<=i<=30: #jihai, akahai
			self.log.debug("i["+str(i)+"] is jihai or akahai")
			return 0
		else:
			if self.tehai[i] and self.tehai[i+1]:
				return 1
			elif self.tehai[i] and self.tehai[i+2]:
				return 1
			else:
				return 0
		return 0
		

	def is_mentsu(self):
		for i in range(37):
			if self.tehai[i] < 1:
				continue

		if self.tehai[i] >= 3:
			self.log.debug("tehai is ANKO")
		elif self.tehai[i] and self.tehai[i+1] and self.tehai[i+2] and i < 30:
			self.log.debug("tehai is SYUNTSU")







