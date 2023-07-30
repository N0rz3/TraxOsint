from .objects import TempPrint
import os

async def ping(ip):
    response = os.system(f'ping -n 1 {ip} > nul' if os.name == "nt" else f'ping -c 1 {ip} > /dev/null 2>&1') 

    TempPrint("[+] 📤 Test if the ip address responds...").TPrint()

    if response == 0:
        print("[+] 🔥 The ip adress responds !\n")
    else:
        print("[-] 🌧️ The ip adress not responds.\n")
