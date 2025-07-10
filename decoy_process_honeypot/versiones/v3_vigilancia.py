import psutil
import subprocess
import time
import sys
from datetime import datetime

DECOY_NAME = "fake_lsass"
LOG_FILE = "honeypot_log.txt"

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
        print(f"[{timestamp}] {message}")

        print("[*] Lanzando proceso señuelo...")

        decoy_process = subprocess.Popen([sys.executable, "-c", "import time; time.slee(600)"],
                                         
            stdout=subprocess.DEVNULL,
            
            stderr=subprocess.DEVNULL)
        
        log_event(f"Proceso señuelo '{DECOY_NAME}' lanzado con PID {decoy_process.pid}")
        time.sleep(2)

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                 if proc.pic == decoy_process.pid:
                    print(f" Encontrado señuelo - PID: {proc.pid}")
                    print(f"   Linea de comando: {proc.info['cmdline']}")
            except (psutil.NoSurchProcess, psutil.AccessDenied):
                    continue
            
            print("\n[*] Iniciando vigilancia del proceso señuelo...\n")

            try:
                 while True:
                      if decoy_process.poll() is not None:
                           log_event(" El proceso señuelo ha sido finalizado.")
                      break
                      time.sleep(2)
            except KeyboardInterrupt: log_event(" Monitorización interrumpida manualmente.")
decoy_process.terminate()
log_event("Porceso señuelo termiando por el usuario.")
            