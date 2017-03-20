#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tenhou:
	
	players = [] #array of Player. initialize at start of kyoku.
	
	def __init__(self):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger()
		self.log.info("Tenhou.__init__ finished.")

		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/mahjong")

	def get_tsumo_from(self, src_filename, codec):
		self.log.info("get_tsumo_from({src_filename}, {codec}) start.".format(**locals()))
		
		self.status = "" #∈{start, drew, discarded}
		self.ivent=""
		output = []

		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		
		import codecs
		f = codecs.open(src_filename, "r",encoding=codec)
		line = f.readline()

		while line:
			#u2162, u2463
			#line = line.replace("\u2463", "?").strip()
			#line = line.replace("[\u2460-\u2469]", "?").strip()
			line = line.strip()
			self.log.debug("line[{line}]".format(**locals()))
			import re
			
			if line[0:1] in {"東", "南"}:
				self.log.debug("start of kyoku")
				self.status = "start"
				output.append(line)
				self.log.debug("self.players = []")
				self.players = []

			elif re.match("\[\d", line[0:2]):
				self.log.debug("haipai")
				self.create_player(line)
			
			elif not line:
				self.log.debug("end of kyoku")
				self.status = "discarded"
				self.end_of_kyoku(output, "../../data/tsumo/" + os.path.basename(src_filename)+"_tsumo", codec)

			elif line[0:1] == "*":
				self.log.debug("haihu")
				self.parse_actions_from(line, output)

			line = f.readline()
		f.close()

		self.log.info("get_tsumo_from({src_filename}) finished.return {output}".format(**locals()))
		return output
		
		
		
	def parse_actions_from(self, line, output):
		self.log.info("parse_actions_from({line}) start.".format(**locals()))
		line = line.replace("*", "").strip()
		haihu = line.split(" ")
		for action in haihu:
			self.log.debug("action[{action}]".format(**locals()))
			if action.count("G"): 
				self.log.debug("action means tsumo")
				if self.status in {"start", "discarded"}:
					player, tsumo = action.split("G")
					self.log.debug("player[{player}] drew {tsumo}".format(**locals()))
					self.player_tsumo(player, tsumo)
					output.append("{player},{tsumo}".format(**locals()))
					self.status = "drew"
				self.log.debug("output.size[" + str(len(output)) + "]")
			elif action.count("R"):
				self.log.debug("action means reach")
				self.ivent += ",reach"
			elif action.count("A"):
				self.log.debug("action means agari")
				self.status = "discarded"
			elif action.count("N"):
				self.log.debug("action means naki")
				player, tsumo = action.split("N")
				self.player_tsumo(player, hai)
			elif action.count("D"):
				self.log.debug("action means tsumogiri")
				player, hai = action.split("D")
				self.player_discard(player, hai)
				if self.status == "drew":
					self.status = "discarded"
					self.log.debug("output.size[" + str(len(output)) + "]")
					output[len(output)-1] += ",tsumogiri{self.ivent}".format(**locals())
					self.ivent = ""
			elif action.count("d"):
				self.log.debug("action means tedashi")
				player, hai = action.split("d")
				self.player_discard(player, hai)
				if self.status == "drew":
					self.status = "discarded"
					self.log.debug("output.size[" + str(len(output)) + "]")
					output[len(output)-1] += ",tedashi{self.ivent}".format(**locals())
					self.ivent = ""
		self.log.info("parse_actions_from({line}) finished.".format(**locals()))
		
		
	def convert_strtehai_to_arr(self, tehai_str):
		self.log.info("convert_strtehai_to_arr(" + tehai_str + ")")
		tmp = tehai_str.replace("m", "m,")\
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
		tehai_arr = tmp.split(",")
		self.log.debug("return array["+str(len(tehai_arr))+"]:"+str(tehai_arr))
		if len(tehai_arr) !=13:
			self.log.warning("number of tehai is not 13!!")
			self.log.warning("return array["+str(len(tehai_arr))+"]:"+str(tehai_arr))

		return tehai_arr
	
	
	
	def create_player(self, line):
		self.log.info("create_player({line}) start.".format(**locals()))
		id = line[1]
		seki = line[2]
		tehai = line[4:]
		
		import player
		player = player.Player()
		player.id = id
		player.seki = seki
		player.init_hand_with(self.convert_strtehai_to_arr(tehai))

		self.players.append(player)
	
	
	def player_tsumo(self, id, hai):
		self.log.info("player[{id}]_tsumo[{hai}] start.".format(**locals()))
		for player in self.players:
			self.log.debug("player.id[{player.id}], id[{id}]".format(**locals()))
			if player.id == id:
				player.tsumo(hai)
				break
		

	
	def player_discard(self, id, hai):
		self.log.info("player[{id}]_discard[{hai}] start.".format(**locals()))
		for player in self.players:
			self.log.debug("player.id[{player.id}], id[{id}]".format(**locals()))
			if player.id == id:
				player.discard(hai)
				break


	def end_of_kyoku(self, output, output_filename, codec):
		self.log.info("end of kyoku start.".format(**locals()))
		import sys,os
		import file_manager
		file_manager = file_manager.File_manager()
		output = file_manager.add_array_to_file(output, output_filename, codec=codec)
		for player in self.players:
			self.log.debug("{player.id}:{player.seki}[".format(**locals()) + player.get_tehai("str") + "]")

	
