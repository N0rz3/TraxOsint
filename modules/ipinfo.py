from helpers.utils import *
from lib.colors import *
from helpers.utils import Requests
import json, random

async def url(ip):
        with open("useragents.txt", "r") as user_file:
                user = user_file.read().split('\n')

        url = "https://ipinfo.io/{}/json".format(ip)

        response = await Requests(url, headers={"User-Agent": random.choice(user)}).sender()

        return json.loads(response.text)

async def look(ip):
        track = await url(ip)
        coordinates = {track['loc']}
        lat = str(coordinates).split(",")[0].replace("{", "").replace("'", "")
        long = str(coordinates).split(",")[1].replace("}", "").replace("'", "")

        try:
                hostname = track['hostname']
        except:
                hostname = None
        try:
                org = track['org']
        except:
                org = None



        output = f"""{CYAN}\rIpinfo{WHITE}\r
└──Hostname := {hostname}
└──A.S. := {org}
└──Country := {track['country']}
   └──Region ~= {track['region']}
      └──City ~= {track['city']}
{"-"*55}

[🟢] Latitude ~= {lat}
[🟢] Longitude ~= {long}"""
        return output

async def coordinates(ip):
        track = await url(ip)

        coordinates = {track['loc']}
        lat = str(coordinates).split(",")[0].replace("{", "").replace("'", "")
        long = str(coordinates).split(",")[1].replace("}", "").replace("'", "")

        return lat, long