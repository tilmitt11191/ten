#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
class A:
	def fact(self, n, a = 1):
		print("fact[" + str(n) + ", " + str(a) + "]")
		if n == 0:
			print("n == 0 return a")
			return a
		print("self.fact(n - 1, n * a)")
		self.fact(n - 1, n * a)
a=A()
print(a.fact(3))
"""

"""
TABLE = {1:"1m",2:"2m",3:"3m",4:"4m",5:"5M",6:"5m",7:"6m",8:"7m",9:"8m",10:"9m",\
	21:"1p",22:"2p",23:"3p",24:"4p",25:"5P",26:"5p",27:"6p",28:"7p",29:"8p",30:"9p",\
	40:"1s",42:"2s",43:"3s",44:"4s",45:"5S",46:"5s",47:"6s",48:"7s",49:"8s",50:"9s",\
	101:"東", 102:"南", 103:"西", 104:"北", 105:"白", 106:"発", 107:"中"}

TABLE_INV = {v:k for k, v in TABLE.items()}
print(str(TABLE_INV))
"""

"""
import logging

logger = logging.getLogger("logger")    #logger名loggerを取得
logger.setLevel(logging.DEBUG)  #loggerとしてはDEBUGで

#handler1を作成
handler1 = logging.StreamHandler()
handler1.setFormatter(logging.Formatter(
    "H1, %(asctime)s %(levelname)8s %(message)s"))

#handler2を作成
handler2 = logging.StreamHandler()
handler2.setLevel(logging.WARN)     #handler2はLevel.WARN以上
handler2.setFormatter(logging.Formatter(
    "H2, %(asctime)s %(levelname)8s %(message)s"))

#loggerに2つのハンドラを設定
logger.addHandler(handler1)
logger.addHandler(handler2)

#出力処理
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
"""


"""
import logging, logging.handlers
rfh = logging.handlers.RotatingFileHandler(
	filename="../../var/log/log2",
	maxBytes=1000000000, 
	backupCount=10
)
rfh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
		
class A:
	def __init__(self):
		pass
		
	@classmethod
	def classmethod(cls):
		loggerA = logging.getLogger()
		loggerA.setLevel(logging.DEBUG)
		loggerA.addHandler(rfh)
		loggerA.info("Aコメ")
		return loggerA


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(rfh)
logger.setLevel(logging.DEBUG)
logger.addHandler(rfh)
logger.addHandler(rfh)
logger.addHandler(rfh)
logger.info("1コメ")

logger2 = logging.getLogger()
logger2.setLevel(logging.INFO)
logger2.addHandler(rfh)
logger2.info("2コメ")

A()
loggerAC = A.classmethod()
loggerAC.info("AC")

logger3 = logging.getLogger()
logger3.setLevel(logging.DEBUG)
logger3.addHandler(rfh)
logger3.info("3コメ")
logger.info("1-2")
"""



"""
class Mahjong
	def convert_tehai
		#array=>str
	def reconvert_tehai
		#str=>array
	def get_machihai(str)

class Player
	tehai[]
	matchi[]
	def tsumo
	def discard
	def get_machihai
		machi = Mahjong.get_machihai(tehai)
		return Mahjong.reconvert_tehai(machi)
"""

"""
#import codecs
#c = codecs.StreamReaderWriter()
f = open("../../etc/config.yml", "r")
print(f.__methods__)
f.close
"""
