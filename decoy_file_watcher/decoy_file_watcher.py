import os
import time

SEÑUELO = "decoy.txt"

# Crea el archivo señuelo si no existe
if not os.path.exists(SEÑUELO):
    with open(SEÑUELO, "w") as f:
        f.write("Este es un archivo señuelo.")

print(f"Vigilando acceso a {SEÑUELO}...")

last_access = os.stat(SEÑUELO).st_atime

try:
    while True:
        time.sleep(1)
        current_access = os.stat(SEÑUELO).st_atime
        if current_access != last_access:
            print(f"¡Archivo {SEÑUELO} accedido!")
            last_access = current_access
except KeyboardInterrupt:
    print("\nVigilancia finalizada por el usuario.")