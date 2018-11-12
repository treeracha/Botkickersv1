from linepy import *
from time import sleep
from datetime import datetime, timedelta
import time, asyncio, json, os, sys, traceback
#--
#Invite bot ke grup yg mau di ratain just for fun :v
#Onhack
cl = LINE()
print("=LOGIN SUCCES=")
oepoll = OEPoll(cl)
clID = cl.getProfile().mid
Me = [""] #Isiin mid lu
def bot(op):
     try:
         if op.type == 0:
            print("END")
            return
         if op.type == 13:
             cl.acceptGroupInvitation(op.param1)
             try:
                 G = cl.getGroup(op.param1)
                 targets = []
                 time.sleep(0.0001)
                 for member in G.members + G.invitee:
                      targets.append(member.mid)
                 for target in targets:
                     if target not in Me:
                       try:
    	                   cl.kickoutFromGroup(op.param1, [target])
                       except:
                           pass
                       try:
                           cl.cancelGroupInvitation(op.param1, [target])
                       except:
                           pass
             except:
             	pass
     except Exception as e:
        cl.log("Error : " + str(e))
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops:
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        cl.log("Error : " + str(e))