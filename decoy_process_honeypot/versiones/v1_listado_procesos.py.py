import psutil


print("[*] Listado procesos activos:\n")

for proc in psutil.process_iter(['pid', 'name']):
    try:
        print(f"PID: {proc.info['pid']}\tNombre: {proc.info['name']}")
    except (psutil.NoSuchProcess,psutil.AccessDenied):
        continue 