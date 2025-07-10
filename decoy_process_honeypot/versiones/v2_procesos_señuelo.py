import psutil
import subprocess
import time
import sys

# Nombre del proceso trampa (solo referencia visual)
DECOY_NAME = "fake_lsass"

print("[*] Lanzando proceso señuelo...")

# Creamos un proceso que duerme mucho tiempo
decoy_process = subprocess.Popen([sys.executable])