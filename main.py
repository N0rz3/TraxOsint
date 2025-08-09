import asyncio, sys

def check_version():
    version = sys.version_info

    if (version < (3, 10)):
        print("[-] Traxosint only works with Python 3.10+.")
        exit("[+] Go install the most recent version of python -> https://www.python.org/downloads/")

    import lib.cli

    asyncio.run(lib.cli.parser())
