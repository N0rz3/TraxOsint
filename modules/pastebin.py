"""
original code => https://github.com/KanekiWeb/Email-Osint/blob/main/modules/PastebinDump.py
"""
from ScrapeSearchEngine.SearchEngine import Google
from lib.colors import *
from helpers.utils import *
from lib.objects import *

import asyncio

async def pastebin_check(i, ip: str, result_links: list):
    try:
        link = str(i).replace("https://pastebin.com/", "https://pastebin.com/raw/")
        r = Requests(link)
        data = await r.sender()

        if ip.lower() in data.text.lower() or ip in data.text or ip.upper() in data.text.upper():
            result_links.append(link)

    except:
        print("[!] Your IP address has been banned. Retry tomorrow or change your IP.".replace('!', RED + '!' + WHITE))

async def pastebin_dump(ip):
    reslt = 0

    search = ("site:pastebin.com \"{}\"".format(ip))
    try:
        googleText, googleLink = Google(search=search, userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        scraping_msg = TempPrint("[+] 😴 Dumping...")
        scraping_msg.TPrint()

        result_links = []
        linker = []

        tasks = []
        for i in googleLink:
            task = pastebin_check(i, ip, result_links)
            tasks.append(task)

        await asyncio.gather(*tasks)

        for link in result_links:
            reslt += 1
            linker.append("└──" + CYAN + link + WHITE)

        if reslt == 0:
            print(f"{RED}\nPastebin{WHITE} | ❌ | The ip address provided does not appear in any paste.\r")
        
        else:
            print(f"{CYAN}\nPastebin{WHITE}\r")
            for links in linker:
                print(links)

        print()

    except:
        print("[!] 🤔 Error.".replace('!', RED + '!' + WHITE))
