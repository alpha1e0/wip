#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


#=================================================searchengine test===========================================
#from plugin.lib.searchengine import Query

#['site','title','url','filetype','link','kw']

#query = Query(filetype="xls") | Query(site="huawei.com")
#query = Query(title="torrent")
#query = Query(filetype="xls")
#print query.genKeyword("bing")
#query = Query(kw="siw")
#re = query.doSearch(engine="bing", size=5)
#print re
#for line in re:
#	print line[0]
#	print line[1]
#	print line[2]


#=================================================nmap test===========================================
#from subprocess import Popen, PIPE, STDOUT

#from plugin.lib.nmapwrapper import Nmap

#result = Nmap.scan("nmap -n 192.168.1.1/24")

#for l in result: print l

#=================================================dnsresolver test============================================
#from plugin.lib.dnsresolve import DnsResolver

#dns = DnsResolver()
#re = dns.getRecords("ns","www.baidu.com")
#re = dns.resolveAll("baidu.com")
#re = dns.getZoneRecords("thinksns.com")
#print re

#sudo install_name_tool -change libmysqlclient.18.dylib /usr/local/mysql/lib/libmysqlclient.18.dylib /Users/apple/.python-eggs/MySQL_python-1.2.5-py2.7-macosx-10.9-intel.egg-tmp/_mysql.so

#=================================================sqlite test============================================

#from model.model import Project, Host, Vul, Comment, Database

#Database.reset()
##Project.delete(7)
#Project.insert(name='dd',url='dd.com',ip='1.1.1.1',level=3,description="ddfuck",whois='ddfuck')#

#print Project.queryraw()
#print dir(Project)

#Project.create()
#Host.create()
#Vul.create()
#Comment.create()
#Database.create()


#=================================================plugin framework test============================================
import config

from plugin.lib.taskmanager import TaskManager
from plugin.lib.plugin import Plugin
from plugin.datasave import DataSave
from plugin.dnsbrute import DnsBrute
from plugin.googlehacking import GoogleHacking
from plugin.serviceidentify import ServiceIdentify
from plugin.subnetscan import SubnetScan
from plugin.zonetrans import ZoneTrans

from model.model import Host

from multiprocessing import Queue


config.RTD.log = config.Log()
config.RTD.taskManager = TaskManager()

class plu(Plugin):
	def __init__(self, namestr):
		self.namestr = namestr
		super(plu,self).__init__()
	def handle(self, data):
		print self.namestr + "get: " + data.description
		data.description = self.namestr + "handle"
		self.put(data)

class end(Plugin):
	def __init__(self, namestr):
		self.namestr = namestr
		super(end,self).__init__()
	def handle(self, data):
		print self.namestr + "get: " + data.description

host = Host()
host.description = "init host"

aa = plu('aa')
bb = plu('bb')
cc = plu('cc')
dd = plu('dd')
ee = plu('ee')
zz = end('zz')

p = zz
#print zz.namestr
#print p._addList
#print p._orList

#print config.RTD.taskManager.inQueue
#print config.RTD.taskManager.outQueue
#print aa.inQueue
#print aa.outQueue
#print zz.inQueue
#print zz.outQueue

inqueue = Queue()

config.RTD.taskManager._inQueue = inqueue
config.RTD.taskManager._outQueue = Queue()

config.RTD.taskManager.start()
print "here1"
#config.RTD.taskManager.startTask(p, [host,])
inqueue.put(p)
print "here2"
#plugin = 

