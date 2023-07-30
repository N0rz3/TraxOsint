import argparse
from helpers.banner import *
from output.Trax import *

async def parser():
    """
    Menu format : cli 

    - this function serves to used commands with argparse
    - (asynchrone function)
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "ip",
        nargs="?",
        type=str,
        default=None,
        help="gives all the information TraxOsint is able to find"
    )


    args = parser.parse_args()

    if args.ip:
        print(main_banner)
        Ip = args.ip
        await ip(Ip)

    else:
        print(menu_banner)