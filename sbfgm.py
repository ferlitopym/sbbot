# -*- coding: utf-8 -*-
import linepy
from linepy import *
from akad.ttypes import *
from datetime import datetime
import pytz, pafy, null, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
from time import sleep
from zalgo_text import zalgo
from threading import Thread,Event
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
from tmp.Instagram import InstagramScraper
from Naked.toolshed.shell import execute_js 
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest

HEF = LINE("akungmailkalian.com","sandi gmailmu")
#HEF.log("Auth Token : " + str(HEF.authToken))
#HEF.log("Timeline Token : " + str(HEF.tl.channelAccessToken))
#HEFientMid = HEF.profile.mid
#HEFientMID = HEF.profile.mid

print("Need Help?? Join Our Community\nhttps://hansengianto.gq/square.html")

HEFMID = HEF.profile.mid
HEFStart = time.time()
HEFPoll = OEPoll(HEF)
#=======================================
read = {"readMember": {}, "readPoint": {}}
settings = {"changeGroupPicture": [], "changePictureProfile": False}
#=======================================
def restartBot():
    print ("[H E F TeamBots] BOT RESETTED")
    python = sys.executable
    os.exeHEF(python, python, *sys.argv)

def logError(text):
    HEF.log("[ ERROR ] {}".format(str(text)))

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def getMidMentionV2(content, text):
    try:
        if 'MENTION' in content.keys()!= None:
            names = re.findall(r'@(\w+)', text)
            mention = ast.literal_eval(content['MENTION'])
            mentionees = mention['MENTIONEES']
            hasil = []
            for isi in mentionees:
                if isi not in hasil:
                    hasil.append(isi["M"])
            return hasil
        else:
            return []
    except:
        pass

def menuHelp():
    cmdlist = [
        "profile",
        "group",
        "broadcast",
        "tagall",
        "ciduk on/off",
        "ciduk",
        "speed",
        "runtime",
        "restart",
        "logout"
    ]
    isi  = "「 H E F SB Lite Free 」"
    isi += "\nType: Help"
    for waw in cmdlist:
        isi += "\n➣ "+waw.title()
    isi += "\n\n⌬ Selfbot Ver 0.1"
    isi += "\nⒸ HNTeam 2020"
    return isi

def menuProfile():
    cmdlist = [
        "me",
        "myprofile",
        "mymid",
        "myname",
        "mybio",
        "mypicture",
        "myvideo",
        "mycover",
        "mid @",
        "name @",
        "bio @",
        "picture @",
        "cover @",
        "updatename [name]",
        "updatebio [bio]",
        "updatedp"
    ]
    isi  = "「 H E F SB Lite Free 」"
    isi += "\nType: Profile"
    for waw in cmdlist:
        isi += "\n➣ "+waw.title()
    isi += "\n\n⌬ Selfbot Ver 0.1"
    isi += "\nⒸ HNTeam 2020"
    return isi

def menuGroup():
    cmdlist = [
        "groupname [name]",
        "groupdp",
        "openqr",
        "HEFoseqr",
        "grouplist",
        "groupinfo",
    ]
    isi  = "「 H E F SB Lite Free 」"
    isi += "\nType: Group"
    for waw in cmdlist:
        isi += "\n➣ "+waw.title()
    isi += "\n\n⌬ Selfbot Ver 0.1"
    isi += "\nⒸ HNTeam 2020"
    return isi

def menuBroadcast():
    cmdlist = [
        "gbroadcast [message]",
        "fbroadcast [message]"
    ]
    isi  = "「 H E F SB Lite Free 」"
    isi += "\nType: Broadcast"
    for waw in cmdlist:
        isi += "\n➣ "+waw.title()
    isi += "\n\n⌬ Selfbot Ver 0.1"
    isi += "\nⒸ HNTeam 2020"
    return isi

def HEFBot(op):
    try:
            if op.type == 25:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                cmd = text.lower()
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != HEF.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        #===============
                        # MENU COMMAND
                        #===============

                        elif cmd == "help":
                            helpMessage = menuHelp()
                            HEF.sendReplyMessage(to, helpMessage)

                        elif cmd == "profile":
                            helpMessage = menuProfile()
                            HEF.sendReplyMessage(to, helpMessage)

                        elif cmd == "group":
                            helpMessage = menuGroup()
                            HEF.sendReplyMessage(to, helpMessage)

                        elif cmd == "broadcast":
                            helpMessage = menuBroadcast()
                            HEF.sendReplyMessage(to, helpMessage)

                        elif cmd == 'tagall':
                            group = HEF.getGroup(to)
                            midMembers = [contact.mid for contact in group.members]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "╭━「 INFO PENTING 」"
                                dataMid = []
                                for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                    dataMid.append(dataMention.mid)
                                    no += 1
                                    ret_ += "\n┃ {}. @!".format(str(no))
                                ret_ += "\n╰━「 Total {} Members 」".format(str(len(dataMid)))
                                #if dataMid != []:
                                HEF.sendMentionV2(to, ret_, dataMid, isUnicode=True)

                        elif cmd == "ciduk on":
                            if to in read['readPoint']:
                                try:
                                    del read['readPoint'][to]
                                    del read['readMember'][to]
                                except:
                                    pass
                                read['readPoint'][to] = msg_id
                                read['readMember'][to] = []
                                HEF.sendReplyMessage(to, "Lurking telah diaktifkan")
                            else:
                                try:
                                    del read['readPoint'][to]
                                    del read['readMember'][to]
                                except:
                                    pass
                                read['readPoint'][to] = msg_id
                                read['readMember'][to] = []
                                HEF.sendReplyMessage(to, "Set reading point. Type ciduk to see reader")

                        elif cmd == "ciduk off":
                            if to not in read['readPoint']:
                                HEF.sendReplyMessage(to,"Lurking telah dinonaktifkan")
                            else:
                                try:
                                    del read['readPoint'][to]
                                    del read['readMember'][to]
                                except:
                                    pass
                                HEF.sendReplyMessage(to, "Delete reading point")

                        elif cmd == "ciduk":
                            if to in read['readPoint']:
                                if read["readMember"][to] == []:
                                    return HEF.sendReplyMessage(to, "Tidak Ada Sider")
                                else:
                                    midMembers = read["readMember"][to]
                                    midSelect = len(midMembers)//20
                                    for mentionMembers in range(midSelect+1):
                                        no = 0
                                        ret_ = "╭━「 Reader 」"
                                        dataMid = []
                                        for dataMention in midMembers[mentionMembers*100 : (mentionMembers+1)*100]:
                                            dataMid.append(dataMention)
                                            no += 1
                                            ret_ += "\n┃ {}. @!".format(str(no))
                                        ret_ += "\n╰━「 Total {} Members 」".format(str(len(dataMid)))
                                        if dataMid != []:
                                            HEF.sendMentionV2(to, result, read["readMember"][to])
                                    read['readMember'][to] = []

                        elif cmd == "speed":
                            HEF.sendReplyMessage(to, "Counting...")
                            start = time.time()
                            time.sleep(0.006)
                            elapsed_time = time.time() - start
                            HEF.sendReplyMessage(to, "Result: {} Seconds".format(str(elapsed_time)))

                        elif cmd == "runtime":
                            timeNow = time.time()
                            runtime = timeNow - HEFStart
                            runtime = timeChange(runtime)
                            HEF.sendReplyMessage(to, "Active Time: {}".format(str(runtime)))

                        elif cmd == "restart":
                            HEF.sendReplyMessage(to, "Success restart selfbot")
                            restartBot()

                        elif cmd == "logout":
                            HEF.sendReplyMessage(to, "Success disable selfbot")
                            sys.exit("[H E F TeamBots] BOT SHUTDOWN")
                            return

                        #===============
                        # PROFILE COMMAND
                        #===============
                        
                        elif cmd == "me":
                            HEF.sendReplyMessage(to, "This Is You")
                            HEF.sendContact(to, sender)

                        elif cmd == "myprofile":
                            contact = HEF.getContact(sender)
                            cover = HEF.getProfileCoverURL(sender)
                            result = "「 Display Name 」"
                            result += "\n{}".format(contact.displayName)
                            result += "\n\n「 MID 」"
                            result += "\n{}".format(contact.mid)
                            result += "\n\n「 Status Message 」"
                            result += "\n{}".format(contact.statusMessage)
                            if contact.pictureStatus != None:
                                HEF.sendImageWithURL(to, "https://obs.line-scdn.net/{}".format(contact.pictureStatus))
                            HEF.sendMentionV2(to, result, [sender])

                        elif cmd == 'my grup':
                            groups = HEF.groups
                            ret_ = "GRUP JOIN"
                            no = 0 + 1
                            for gid in groups:
                                group = HEF.getGroup(gid)
                                ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                no += 1
                            ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                            HEF.sendReplyMessage(kirim, str(ret_))

                        elif cmd == 'announce':
                            try:
                                gett = HEF.getChatRoomAnnouncements(kirim)
                                for a in gett:
                                    aa = HEF.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    HEF.sendReplyMessage(kirim, 'Pemberitahuan Grup\n\nLink: ' + str(cc) + '\nPenulis: ' + str(aa) + '\nTeksnya: ' + str(textt))
                                    break
                            except Exception as e:
                                HEF.sendReplyMessage(kirim, "Pemberitahuan Grup Tidak Ditemukan")

                        elif cmd == "mymid":
                            contact = HEF.getContact(sender)
                            HEF.sendReplyMessage(to, sender)

                        elif cmd == "myname":
                            contact = HEF.getContact(sender)
                            HEF.sendReplyMessage(to, contact.displayName)

                        elif cmd == "mybio":
                            contact = HEF.getContact(sender)
                            HEF.sendReplyMessage(to, contact.statusMessage)

                        elif cmd == "mypicture":
                            contact = HEF.getContact(sender)
                            HEF.sendImageWithURL(to, "https://obs.line-scdn.net/{}".format(contact.pictureStatus))

                        elif cmd == "myvideo":
                            contact = HEF.getContact(sender)
                            if contact.videoProfile == None:
                                return HEF.sendReplyMessage(to, "Anda tidak memiliki video profile")
                            else:HEF.sendVideoWithURL(to, "https://obs.line-scdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd == "mycover":
                            cover = HEF.getProfileCoverURL(sender)
                            HEF.sendImageWithURL(to, str(cover))

                        # STEAL PROFILE

                        elif cmd.startswith("mid "):
                            ls = getMidMentionV2(msg.contentMetadata, text)
                            for ls in lists:
                                HEF.sendReplyMessage(to, ls)

                        elif cmd.startswith("name "):
                            ls = getMidMentionV2(msg.contentMetadata, text)
                            for ls in lists:
                                contact = HEF.getContact(ls)
                                HEF.sendReplyMessage(to, contact.displayName)

                        elif cmd.startswith("bio "):
                            ls = getMidMentionV2(msg.contentMetadata, text)
                            for ls in lists:
                                contact = HEF.getContact(ls)
                                HEF.sendMentionV2(to, "@!: {}".format(contact.statusMessage), [ls])

                        elif cmd.startswith("picture "):
                            ls = getMidMentionV2(msg.contentMetadata, text)
                            for ls in lists:
                                contact = HEF.getContact(ls)
                                HEF.sendImageWithURL(to, "https://obs.line-scdn.net/{}".format(contact.pictureStatus))

                        elif cmd.startswith("cover "):
                            ls = getMidMentionV2(msg.contentMetadata, text)
                            for ls in lists:
                                cover = HEF.getProfileCoverURL(ls)
                                HEF.sendImageWithURL(to, str(cover))

                        elif cmd == 'gcreator':
                            try:
                                group = HEF.getGroup(kirim)
                                GS = group.creator.mid
                                HEF.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                HEF.sendMentionV2(kirim,GS,"Group Creator","")
                                contact = HEF.getContact(GS.mid)
                            except:
                                W = group.members[0].mid
                                HEF.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                HEF.sendMentionV2(kirim,W,"Group Creator","")

                        # UPDATE PROFILE

                        elif cmd.startswith("updatename "):
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            if len(name) <= 20:
                                profile = HEF.getProfile()
                                profile.displayName = name
                                HEF.updateProfile(profile)
                                HEF.sendReplyMessage(to, "Berhasil mengubah nama menjadi : {}".format(name))

                        elif cmd.startswith("updatebio "):
                            sep = text.split(" ")
                            bio = text.replace(sep[0] + " ","")
                            if len(bio) <= 500:
                                profile = HEF.getProfile()
                                profile.displayName = bio
                                HEF.updateProfile(profile)
                                HEF.sendReplyMessage(to, "Berhasil mengubah bio menjadi : {}".format(bio))

                        elif cmd == "updatedp":
                            settings["changePictureProfile"] = True
                            HEF.sendReplyMessage(to, "Silahkan kirim gambarnya")

                        #===============
                        # GROUP COMMAND
                        #===============

                        elif cmd.startswith("cekcuaca: "):
                            weather = cmd.replace("cekcuaca: ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                HEF = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(weather)))
                                data = HEF.text
                                data = json.loads(data)
                                if "result" not in data:
                                    ret_ = "Cheking Weather\n"
                                    ret_ += "\nSuhu : " + data[1].replace("Suhu : ","")
                                     ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","")
                                    ret_ += "\nTekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                    ret_ += "\nKecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                    ret_ += "\n\nSearching Weather Success"
                                else:
                                    ret_ = "Checking Weather Error or Not Found Location"
                                HEF.sendReplyMessage(kirim, str(ret_))

                        elif cmd.startswith("groupname "):
                            if msg.toType == 2:
                                sep = text.split(" ")
                                groupname = text.replace(sep[0] + " ","")
                                if len(groupname) <= 20:
                                    group = HEF.getGroup(to)
                                    group.name = groupname
                                    HEF.updateGroup(group)
                                    HEF.sendReplyMessage(to, "Berhasil mengubah nama group menjadi : {}".format(groupname))

                        elif cmd == "groupdp":
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                HEF.sendReplyMessage(to, "Silahkan kirim gambarnya")

                        elif cmd == "openqr":
                            if msg.toType == 2:
                                group = HEF.getGroup(to)
                                group.preventedJoinByTicket = False
                                HEF.updateGroup(group)
                                groupUrl = HEF.reissueGroupTicket(to)
                                HEF.sendReplyMessage(to, "Berhasil membuka QR Group\n\nGroupURL : line://ti/g/{}".format(groupUrl))

                        elif cmd == "HEFoseqr":
                            if msg.toType == 2:
                                group = HEF.getGroup(to)
                                group.preventedJoinByTicket = True
                                HEF.updateGroup(group)
                                HEF.sendReplyMessage(to, "Berhasil menutup QR Group")

                        elif cmd == "grouplist":
                            groups = HEF.getGroupIdsJoined()
                            ret_ = "╭─[ Group List ]"
                            no = 0
                            for gid in groups:
                                group = HEF.getGroup(gid)
                                no += 1
                                ret_ += "\n➣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            ret_ += "\n╰─[ Total {} Groups ]".format(str(len(groups)))
                            HEF.sendReplyMessage(to, str(ret_))

                        elif cmd == "groupinfo":
                            group = HEF.getGroup(to)
                            try:
                                try:
                                    groupCreator = group.creator.mid
                                except:
                                    groupCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    groupPending = "0"
                                else:
                                    groupPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    groupQr = "Tertutup"
                                    groupTicket = "Tidak ada"
                                else:
                                    groupQr = "Terbuka"
                                    groupTicket = "https://line.me/R/ti/g/{}".format(str(HEF.reissueGroupTicket(group.id)))
                                ret_ = "「 Group Info 」"
                                ret_ += "\n➣ Name : {}".format(group.name)
                                ret_ += "\n➣ ID : {}".format(group.id)
                                ret_ += "\n➣ Member : {}".format(str(len(group.members)))
                                ret_ += "\n➣ Pending : {}".format(groupPending)
                                ret_ += "\n➣ Group Qr : {}".format(groupQr)
                                ret_ += "\n➣ Group Ticket : {}".format(groupTicket)
                                HEF.sendImageWithURL(to, "https://obs.line-scdn.net/{}".format(group.pictureStatus))
                                HEF.sendReplyMessage(to, str(ret_))
                                HEF.sendContact(to, groupCreator)
                            except Exception as e:
                                print(e)

                        #===============
                        # BROADCAST COMMAND
                        #===============

                        elif cmd.startswith("gbroadcast "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = HEF.getGroupIdsJoined()
                            for group in groups:
                                try:HEF.sendReplyMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                                except:pass
                                time.sleep(3)
                            HEF.sendReplyMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))

                        elif cmd.startswith("fbroadcast "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = HEF.getAllContactIds()
                            for group in groups:
                                try:HEF.sendReplyMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                                except:pass
                                time.sleep(3)
                            HEF.sendReplyMessage(to, "Berhasil broadcast ke {} friend".format(str(len(groups))))

#============================================================================

                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = HEF.downloadObjectMsg(msg_id, saveAs="tmp/{}-cpp.bin".format(time.time()))
                            settings["changePictureProfile"] = False
                            HEF.updateProfilePicture(path)
                            HEF.sendReplyMessage(to, "Berhasil mengubah foto profile")
                            HEF.deleteFile(path)

                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = HEF.downloadObjectMsg(msg_id, saveAs="tmp/{}-cgp.bin".format(time.time()))
                                settings["changeGroupPicture"].remove(to)
                                HEF.updateGroupPicture(to, path)
                                HEF.sendReplyMessage(to, "Berhasil mengubah foto group")
                                HEF.deleteFile(path)

            if op.type == 55:
                if op.param1 in read["readPoint"]:
                    if op.param2 not in read["readMember"][op.param1]:
                        read["readMember"][op.param1].append(op.param2)

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        logError(error)

def run():
    while True:
        ops = HEFPoll.singleTrace(count=50)
        if ops != None:
            for op in ops:
                try:
                    HEFBot(op)
                except Exception as error:
                    logError(error)
                HEFPoll.setRevision(op.revision)

if __name__ == "__main__":
    run()
