import subprocess

ip = input("Introduce la IP o dominio a escanear:")
print(f"Escaneando puertos abiertos en {ip}...")

result = subprocess.run(["nmap", "-sS", "-Pn", ip], capture_output=True, text=True)
print(result.stdout)

# This script uses nmap to perform a SYN scan on the specified IP or domain.