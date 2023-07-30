@echo off

color 0A     
echo Installation requirements                                                                           
                                                                                                                                                                         
pip install httpx==0.24.1
pip install argparse==1.4.0
pip install folium

if %errorlevel% equ 0 (
    echo [+] Installation successful
) else (
    echo [-] Installation failed
)
pause