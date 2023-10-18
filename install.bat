@echo off

color 0A     
echo Installation requirements                                                                           
                                                                                                                                                                         
pip install httpx==0.24.1
pip install argparse==1.4.0
pip install folium
pip install scrape-search-engine==0.2.2
pip install requests==2.31.0
pip install bs4

if %errorlevel% equ 0 (
    echo [+] Installation successful
) else (
    echo [-] Installation failed
)
pause
