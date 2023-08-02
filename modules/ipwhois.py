import random, json
from helpers.utils import Requests
from lib.colors import *

async def url(ip):
        with open("useragents.txt", "r") as user_file:
                user = user_file.read().split('\n')

        url = "http://ipwho.is/{}".format(ip)

        response = await Requests(url, headers={"User-Agent": random.choice(user)}).sender()

        return json.loads(response.text)

async def lok(ip):
        read = await url(ip)

        output = f"""{CYAN}\rIpWhois{WHITE}\r
└──Continent := {read['continent']}
   └──Country := {read['country']}
      └──Region ~= {read['region']}
         └──City ~= {read['city']}
         
[{GREEN}+{WHITE}] I.S.P. := {read['connection']['isp']}
"""
        return output, read['city']


async def resolv_org(ip):
        read = await url(ip)
        
        domain = read['connection']['domain']
        org = str(domain).split(".")[0]
        
        if org:
                output = f"✔️ {org.upper()}\n"
        else:
                return ""

        return output
