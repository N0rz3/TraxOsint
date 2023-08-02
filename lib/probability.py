from modules.ipapi import lookup
from modules.ipinfo import look
from modules.ipwhois import lok
from .colors import *
from .objects import TempPrint

# /**Probabilities**\
#
# - fully async (asynchrone)
#
# Explanation:
#   - If an api says that the place is New York and the other 2 say the same, the city will be displayed with "++" (very likely).
#   - When an api gives a city, this is noted and is compared with the other results to deduce the probabilities with "+" or "-".
#
#   Legend:        _______________________
#                  | ++ | Very likely     |
#                  | +  | Likely          |
#                  | -  | Not very likely |
#                  |_;)_|_________________|

class prob:
    def __init__(self, ip) -> None:
        self.ip = ip

    async def loader(self):
        ipapi_data, ipapi_city = await lookup(self.ip)
        ipinfo_data, ipinfo_city, latlong = await look(self.ip)
        ipwhois_data, ipwhois_city = await lok(self.ip)

        return str(ipapi_city).upper(), str(ipinfo_city).upper(), str(ipwhois_city).upper()

    async def probability(self):
        PROBABLE = GREEN + "+" + WHITE
        PROBABLE_ = GREEN + "++" + WHITE
        _PROBABLE = RED + "-" + WHITE

        ipapi_city, ipinfo_city, ipwhois_city = await self.loader()

        async def compare_cities(city1, city2, city3):
            if city1 == city2 == city3:
                return PROBABLE_ + city1.lower()
            elif city1 != city2 == city3:
                return PROBABLE + city1.lower()
            else:
                return _PROBABLE + city1.lower()

        TempPrint("\n[+] 🤓 Calculation of the probabilities of cities +-x...", 4).TPrint()

        output = f"""\r[~] Place probabilities based on API results:
{await compare_cities(ipapi_city, ipinfo_city, ipwhois_city)}
{await compare_cities(ipinfo_city, ipapi_city, ipwhois_city)}
{await compare_cities(ipwhois_city, ipapi_city, ipinfo_city)}
"""
        print(output)