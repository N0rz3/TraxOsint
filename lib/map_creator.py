import folium, os
from .colors import *
from modules.ipinfo import coordinates
from .objects import TempPrint

PATH = os.path.abspath("result/world_map.html")

class Creator:
    @staticmethod
    async def create_map(latitude, longitude):
        map_world = folium.Map(location=[latitude, longitude], zoom_start=5)

        folium.Marker(location=[latitude, longitude], popup="Point").add_to(map_world)

        return map_world

    @staticmethod
    async def point_placer(ip):
        try:
            latitude, longitude = await coordinates(ip)

            map_with_point = await Creator.create_map(latitude, longitude)

            map_with_point.save(PATH)

            TempPrint("[+] 🗺️ Creation of the map...").TPrint()

            print(f"[🟢] Map created at path : {PATH}")

        except Exception as e:
            print(f"[🔴] Error while creating the map. ({e})")