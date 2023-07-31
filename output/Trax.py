from lib.colors import *
from lib.map_creator import *
from modules.ipinfo import *
from modules.proton import *
from modules.ipapi import *
from modules.ipwhois import *
from modules.pastebin import *
from lib.pinger import ping
from lib.check_ports import check_open_ports
import re

async def ip(ip):
    regex = r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    ports=[8080, 80, 443] # you can modify the list with the ports you want to check

    if re.match(regex, ip):
        print("[+] 🤗 Regular expression valid !\n")

        await ping(ip)
        open_ports = await check_open_ports(ports, ip)
        open_ports
        protonvpn = await vpnchecker(ip)
        ipinfo = await look(ip)
        ipwhois = await lok(ip)
        org = await resolv_org(ip)
        ipapi = await lookup(ip)
        print(f"""
{YELLOW}🛠️ Modules{WHITE}
{"-"*55}
{protonvpn}""")
        await pastebin_dump(ip)

        print(f"""\r{ipapi}
{ipwhois}
{org}
{ipinfo}
""")
        await Creator.point_placer(ip)

    else:
        print("[-] ☹️ Regular expression not valid !")
        exit()
