from helpers.utils import *
from lib.colors import *
from helpers.utils import Requests
import json, random

async def url(ip):
        with open("useragents.txt", "r") as user_file:
                user = user_file.read().split('\n')

        url = "http://ip-api.com/json/{}".format(ip)

        response = await Requests(url, headers={"User-Agent": random.choice(user)}).sender()

        return json.loads(response.text)

async def lookup(ip):
        read = await url(ip)

        output = f"""\r{CYAN}Ip-api{WHITE}\r
└──Organization := {read['org']}
└──Country := {read['country']}
   └──Region ~= {read['regionName']}
      └──City ~= {read['city']}
"""
        return output, read['city']
