import socket

async def check_open_ports(port, ip) -> list:
        print(f"[+] Check open ports :")

        for ports in port:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, ports))
                sock.close()

                if result == 0:
                    print(f"✔️ {ports}")
                else:
                    print(f"❌ {ports}")

            except Exception as e:
                print(f"Error in {ports} port : {e}")