#!/usr/bin/python
import time
import datetime
import numpy
import random

log_lines = 100000

users = ["hive","hdfs","user1","user2","user3","user4","user5","user6","user7","user8","user9","user10","app1","app2","app3","app4","yarn"]
ips = ["123.221.14.56","16.180.70.237","10.182.189.79","218.193.16.244","198.122.118.164","114.214.178.92","233.192.62.103","244.157.45.12","81.73.150.239","237.43.24.118"]
cmds = ["setTimes","setPermission","listStatus","safemode_get","mkdirs","fsck","delete","contentSummary","setOwner","create","open","modifyAclEntries","rename","rollEditLog","getfileinfo","setStoragePolicy","listEncryptionZones"]
paths = ["/app-logs","/apps","/ats","/atsv2","/hdp","/mapred","/mr-history","/ranger","/services","/tmp","/user","/warehouse","/user/ambari-qa","/user/druid","/user/hbase","/user/hive","/user/yarn-ats","/apps/druid","/apps/hbase","/warehouse/tablespace","/hdp/apps"]

#    if uri.find("apps")>0:
#        uri += str(random.randint(1000,10000))

f = open('/hadoop/hdfs-audit.log','w',buffering=1)

flag = True
while (flag):
  ip = random.choice(ips)
  dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
  cmd = numpy.random.choice(cmds,p=[0.01,0.01,0.07,0.01,0.07,0.01,0.09,0.12,0.02,0.14,0.17,0.03,0.07,0.02,0.14,0.01,0.01])
  user = numpy.random.choice(users,p=[0.14,0.14,0.07,0.01,0.07,0.01,0.09,0.12,0.02,0.01,0.17,0.03,0.07,0.02,0.01,0.01,0.01])
  path = random.choice(paths)
#  print('%s INFO FSNamesystem.audit: allowed=true   ugi=%s  (auth:SIMPLE)  ip=%s  cmd=%s  src=%s   dst=null   perm=null  proto=rpc' % (dt,user,ip,cmd,path))
  f.write('%s INFO FSNamesystem.audit: allowed=true   ugi=%s  (auth:SIMPLE)  ip=%s  cmd=%s  src=%s   dst=null   perm=null  proto=rpc \n' % (dt,user,ip,cmd,path))

  log_lines = log_lines - 1
  flag = False if log_lines == 0 else True
  time.sleep(1)

