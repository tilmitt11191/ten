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
	

	def simulate_logfile(self, script_filename, src_codec, output_filename = "", output_file_suffix="csv", output_codec="utf-8", output_format=["player", "tsumo"]):
		self.log.info("simulate_logfile start. script_filename[" + script_filename + "], codec[" + src_codec +"], output_format" + str(output_format) + "")
		
		
		file_manager = self.initialize_before_simulate(script_filename, output_filename, output_file_suffix, output_codec)
		
		if output_format == []:
			return 0
		
		script = self.read_script_file(script_filename, src_codec)
		line = script.readline()

		result = []
		status = "" #∈{start, drew, discarded}
		self.sutehai = ""
		event=""
		while line:
			line = line.strip()
			self.log.debug("line[" + line + "]")
			import re
			
			if line[0:1] == "=":
				print(line)
				result = self.start_of_game_line(line, result)
			elif line[0:1] in {"東", "南", "西", "北"}:
				result, status, event = self.start_of_kyoku_line(line, result)

			elif re.match("\[\d", line[0:2]):
				result = self.haipai_line(line, result)

			elif line[0:1] == "*":
				result, status, event = self.action_line(line, result, status, event)

			elif not line:
				result = self.end_of_kyoku_line(result, file_manager)

			line = script.readline()

		script.close()
		
		
	
	def initialize_before_simulate(self, script_filename, output_filename, output_file_suffix, output_codec):
		self.log.debug("initialize_before_simulate start.")
		##initialize output file
		import file_manager
		fm = file_manager.File_manager()
		import os
		if output_filename == "":
			fm.initialize_output_file("../../data/sim/" + os.path.basename(script_filename)+"_sim", suffix=output_file_suffix, output_codec=output_codec)
		else:
			fm.initialize_output_file(output_filename, suffix=output_file_suffix)
		return fm
		

		
	def start_of_game_line(self, line, result):
		self.log.debug("start_of_game start.")
		result.append(line)
		return result
		
	def start_of_kyoku_line(self, line, result):
		self.log.debug("start_of_kyoku start.")
		result.append(line)
		self.players = []
		self.log.debug("self.players = []. len[" + str(len(self.players)) + "]")
		status = "start"
		event = ""
		return result, status, event

	def haipai_line(self, line, result):
		self.log.debug("haipai start.")
		self.create_player(line)
		machi = self.get_machi_str(int(line[1]))
		result.append(line[1] + ",,," + machi + "," + self.players[int(line[1])-1].get_tehai(type="str"))
		return result
	
	def get_machi_str(self, player_number):
		self.players[player_number-1].calc_machi()
		return self.players[player_number-1].get_machi(type="str")
		

	
	def action_line(self, line, result, status, event):
		self.log.debug("action start.")
		actions = line.split(" ")
		for action in actions:
			self.log.debug("action " + action + " start.")
			if action == "*":
				pass
			elif action.count("G"): 
				self.log.debug("action means tsumo")
				if status in {"start", "discarded"}:
					player, tsumo = action.split("G")
					self.log.debug("player[{player}] drew {tsumo}".format(**locals()))
					self.log.debug("tehai:"+self.players[int(player)-1].get_tehai(type="str"))
					self.player_tsumo(player, tsumo)
					result.append("{player},{tsumo}".format(**locals()))
					status = "drew"
				self.log.debug("result.size[" + str(len(result)) + "]")
			elif action.count("R"):
				self.log.debug("action means reach")
				event += "reach"
			elif action.count("A"):
				self.log.debug("action means agari")
				status = "discarded"
			elif action.count("K"):
				player, hai = action.split("K")
				if status == "discarded":
					self.log.debug("action means minkan")
					self.player_naki(player, hai)
				elif status == "drew":
					self.log.debug("action means ankan or kakan")
					status = "discarded"
				self.player_discard(player, hai)
			elif action.count("N"):
				self.log.debug("action means pon")
				player, hai = action.split("N")
				self.player_naki(player, hai)
			elif action.count("C"):
				player, hai = action.split("C")
				self.player_chi(player, self.sutehai)
			elif action.count("D"):
				self.log.debug("action means tsumogiri")
				player, hai = action.split("D")
				self.player_discard(player, hai)
				self.sutehai = hai
				if status == "drew":
					status = "discarded"
					self.log.debug("result.size[" + str(len(result)) + "]")
					result[len(result)-1] += ",tsumogiri{event}".format(**locals())
					event = ""
					machi = self.get_machi_str(int(player))
					result[len(result)-1] += "," + machi + "," + self.players[int(player)-1].get_tehai(type="str")
			elif action.count("d"):
				self.log.debug("action means tedashi")
				player, hai = action.split("d")
				self.player_discard(player, hai)
				self.sutehai = hai
				if status == "drew":
					status = "discarded"
					self.log.debug("result.size[" + str(len(result)) + "]")
					result[len(result)-1] += ",tedashi{event}".format(**locals())
					event = ""
					machi = self.get_machi_str(int(player))
					result[len(result)-1] += "," + machi + "," + self.players[int(player)-1].get_tehai(type="str")
			else:
				self.log.error("action[" + action + "] not defined.")
		
		return result, status, event
		
	def end_of_kyoku_line(self, result, file_manager):
		self.log.debug("end_of_kyoku start.")
		for player in self.players:
			self.log.debug(player.id + ":" + player.get_tehai(type="str"))
	
		result = file_manager.add_array_to_file(result)
		return result







		
	def get_tsumo_from(self, src_filename, codec):
		self.log.info("get_tsumo_from({src_filename}, {codec}) start.".format(**locals()))
		
		self.status = "" #∈{start, drew, discarded}
		self.event=""
		output = []

		f = self.read_script_file(src_filename, codec)
		line = f.readline()

		while line:
			#u2162, u2463
			#line = line.replace("\u2463", "?").strip()
			#line = line.replace("[\u2460-\u2469]", "?").strip()
			line = line.strip()
			self.log.debug("line[{line}]".format(**locals()))
			import re
			
			if line[0:1] in {"東", "南", "西", "北"}:
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
				import os
				self.AAAAend_of_kyoku(output, "../../data/tsumo/" + os.path.basename(src_filename)+"_tsumo", codec)

			elif line[0:1] == "*":
				self.log.debug("haihu")
				self.AAAAparse_actions_from(line, output)

			line = f.readline()
		f.close()

		self.log.info("get_tsumo_from({src_filename}) finished.return {output}".format(**locals()))
		return output
		
		
		
	def AAAAparse_actions_from(self, line, output):
		self.log.info("AAAAparse_actions_from({line}) start.".format(**locals()))
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
				self.event += ",reach"
			elif action.count("A"):
				self.log.debug("action means agari")
				self.status = "discarded"
			elif action.count("N"):
				self.log.debug("action means naki")
				player, tsumo = action.split("N")
				self.player_naki(player, hai)
			elif action.count("D"):
				self.log.debug("action means tsumogiri")
				player, hai = action.split("D")
				self.player_discard(player, hai)
				if self.status == "drew":
					self.status = "discarded"
					self.log.debug("output.size[" + str(len(output)) + "]")
					output[len(output)-1] += ",tsumogiri{self.event}".format(**locals())
					self.event = ""
			elif action.count("d"):
				self.log.debug("action means tedashi")
				player, hai = action.split("d")
				self.player_discard(player, hai)
				if self.status == "drew":
					self.status = "discarded"
					self.log.debug("output.size[" + str(len(output)) + "]")
					output[len(output)-1] += ",tedashi{self.event}".format(**locals())
					self.event = ""
		self.log.info("AAAAparse_actions_from({line}) finished.".format(**locals()))
		
		
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
		player.init_hand_with(tehai, type="str")
		self.players.append(player)
	
	
	
	def player_tsumo(self, id, hai):
		self.log.info("player[{id}]_tsumo[{hai}] start.".format(**locals()))
		for player in self.players:
			self.log.debug("player.id[{player.id}], id[{id}]".format(**locals()))
			if player.id == id:
				player.tsumo(hai)
				break
		
	def player_naki(self, id, hai):
		self.log.info("player[{id}]_naki[{hai}] start.".format(**locals()))
		##北北->北
		tmp = hai.replace("m", "m,")\
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
		tmp_arr = tmp.split(",")
		hai = tmp_arr[0]
		
		for player in self.players:
			self.log.debug("player.id[{player.id}], id[{id}]".format(**locals()))
			if player.id == id:
				player.tsumo(hai)
				break
		
	def player_chi(self, id, sutehai):
		self.log.info("player[{id}]_chi[{sutehai}] start.".format(**locals()))
		for player in self.players:
			self.log.debug("player.id[{player.id}], id[{id}]".format(**locals()))
			if player.id == id:
				player.tsumo(sutehai)
				break

	def player_discard(self, id, hai):
		self.log.info("player[{id}]_discard[{hai}] start.".format(**locals()))
		for player in self.players:
			self.log.debug("player.id[{player.id}], id[{id}]".format(**locals()))
			if player.id == id:
				player.discard(hai)
				break


	def AAAAend_of_kyoku(self, output, output_filename, codec):
		self.log.info("end of kyoku start.".format(**locals()))
		import sys,os
		import file_manager
		file_manager = file_manager.File_manager()
		output = file_manager.AAAAadd_array_to_file(output, output_filename, codec=codec)
		for player in self.players:
			self.log.debug("{player.id}:{player.seki}[".format(**locals()) + player.get_tehai("str") + "]")

	

	def read_script_file(self, script_filename, codec):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		
		import codecs
		return codecs.open(script_filename, "r",encoding=codec)
