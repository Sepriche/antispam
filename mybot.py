# -*- coding: utf-8 -*-
import sepriche
from sepriche import *
from sepri.ttypes import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from time import sleep
sepri = LINE('EFYRh0YcygPevzTAznU0.dJDcqR7GElvv2z8FUzJX8a.Pq1T1usUOgxw8De9n3WJinjYTtP0STJFMyBQbOZGUj8=')
sepri.log("Auth Token : " + str(sepri.authToken))
print ("=== LOGIN SUCCES ===\n =[Sepri bot siap digunakan]=\n =TEAM FUNKZHER BOT PROTECTION=")
oepoll = OEPoll(sepri)
mid = sepri.getProfile().mid
Bots = [mid]
Owner = ["u0e374242bee078b555d99f1fb998f1f0"]
msg_dict = {}
msg_dict1 = {}
sue = codecs.open("SCwait.json","r","utf-8")
SCwait = json.load(sue)
settings = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                sepri.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%ᶠᵇᵏJam:%ᶠᵇᵏMenit:%ᶠᵇᵏDetik')
def logError(text):
    sepri.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("SCdataERROR.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = sepri.getAllContactIds()
        gid = sepri.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%Jam:%Menit:%Detik')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :ᶠᵇᵏ࿐  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        sepri.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def command(text):
    pesan = text.lower()
    if pesan.startswith(SCwait["keyCmd"]):
        cmd = pesan.replace(SCwait["keyCmd"],"")
    else:
        cmd = "command"
    return cmd
def help():
    key = SCwait["keyCmd"]
    key = key.title()
    helpMessage = "=====[HELP]=====\n" + \
                  "◯ " + key + "Me\n" + \
                  "◯ " + key + "Autoblock on/off\n" + \
                  "◯ " + key + "Autoreject on/off\n" + \
                  "◯ " + key + "Autoleave on/off\n" + \
                  "◯ " + key + "Autojoin on/off\n" + \
                  "◯ " + key + "Invitelist\n" + \
                  "◯ " + key + "Reject\n" + \
                  "◯ " + key + "Rchat\n" + \
                  "======[FBK]====="
    return helpMessage
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 13:
            if mid in op.param3:
                if SCwait["autoReject"] == True:
                    if op.param2 not in Bots and op.param2 not in Owner:
                        sepri.rejectGroupInvitation(op.param1)
                    else:
                        sepri.rejectGroupInvitation(op.param1)
        if op.type == 13:
            if mid in op.param3:
                if SCwait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Owner:
                        sepri.acceptGroupInvitation(op.param1)
                    else:
                        sepri.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if mid in op.param3:
                if SCwait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in Owner:
                        sepri.acceptGroupInvitation(op.param1)
                        sepri.leaveGroup(op.param1)
                    else:
                        sepri.acceptGroupInvitation(op.param1)
                        sepri.leaveGroup(op.param1)
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if SCwait["autoBlock"] == True:
              if op.param2 not in Bots and op.param2 not in Owner:
                sepri.blockContact(op.param1)
                sepri.sendMessage(op.param1, "♪ᶠᵇᵏsorry autoblock gue aktif")
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        setKey = SCwait["keyCmd"].title()
                        if cmd == "help":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                               helpMessage = help()
                               sepri.sendMessage(msg.to, "✪fbk\n"+str(helpMessage))
                        elif cmd == "invitelist" or cmd == "listinvite":
                          if msg._from in Owner:
                            groups = sepri.getGroupIdsInvited()
                            ret_ = "====「 Invitation List 」"
                            no = 1
                            for gid in groups:
                                group = sepri.getGroup(gid)
                                ret_ += "\n│•{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no = (no+1)
                            ret_ += "\n│Total {} Pending".format(str(len(groups)))
                            ret_ += "\n├───「 Usage 」───"
                            ret_ += "\n├Accept 「Nomor」"
                            ret_ += "\n├Reject 「Nomor」"
                            ret_ += "\n====「 Funkzher Bot 」"
                            sepri.sendMessage(msg.to, str(ret_))
                        elif cmd == "reject":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                              ginvited = sepri.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      time.sleep(4)
                                      sepri.rejectGroupInvitation(gid)
                                  sepri.sendMessage(msg.to, "♪ᶠᵇᵏ Succes Reject {} Group Invite".format(str(len(ginvited))))
                              else:
                                  sepri.sendMessage(msg.to, "♪ᶠᵇᵏno thing")
                        elif cmd == "autoreject on":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoReject"] = True
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto Reject 」\nSuccessfully activated")
                        elif cmd == "autoreject off":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoReject"] = False
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto Reject 」\nDisable successfully")
                        elif cmd == "autoblock on":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoBlock"] = True
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto block 」\nSuccessfully activated")
                        elif cmd == "autoblock off":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoBlock"] = False
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto block 」\nDisable successfully")
                        elif cmd == "autojoin on":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoJoin"] = True
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto join 」\nSuccessfully activated")
                        elif cmd == "autojoin off":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoJoin"] = False
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto join 」\nDisable successfully")
                        elif cmd == "autoleave on":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoLeave"] = True
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto leave 」\nSuccessfully activated")
                        elif cmd == "autoleave off":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                SCwait["autoLeave"] = False
                                sepri.sendMessage(msg.to, "「 ♪ᶠᵇᵏ Status Auto leave 」\nDisable successfully")
                        elif text.lower() == "rchat":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                               try:
                                   sepri.removeAllMessages(op.param2)
                                   sepri.sendMessage(msg.to,"♪ᶠᵇᵏDone...")
                               except:
                                   sepri.removeAllMessages(op.param2)
                                   sepri.sendMessage(msg.to,"♪ᶠᵇᵏDone...")
                        elif cmd == "me":
                          if SCwait["selfbot"] == True:
    #                        if msg._from in Owner:
                                sepri.sendMessage(msg.to,"n...cret hahaha")                        
                        elif cmd == "status":
                          if SCwait["selfbot"] == True:
                            if msg._from in Owner:
                                md = " ==[STATUS BOT]==\n"
                                if SCwait["autoJoin"] == True: md+="[on] Auto Join\n"
                                else: md+="[off] Auto Join\n"
                                if SCwait["autoLeave"] == True: md+="[on] Auto Leave\n"
                                else: md+="[off] Auto Leave\n"
                                if SCwait["autoReject"] == True: md+="[on] Auto Reject\n"
                                else: md+="[off] Auto Reject\n"
                                if SCwait["autoBlock"] == True: md+="[on] Auto Block\n"
                                else: md+="[off] Auto Block\n"
                                sepri.sendMessage(msg.to, md+"\n=======[fbk]======= ")
    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
