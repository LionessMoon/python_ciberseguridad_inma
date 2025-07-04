# decoy_file_watcher.py

Este script detecta accesos a un archivo señuelo ('decoy.txt')
en tiempo real. Es útil para practicar técnicas de defensa en 
ciberseguridad.

## ¿Cómo funciona?

- Monitorea constantemente un archivo trampa.
- Si alguen accede, modifica o simplemente lo abre, el script 
muestra una alerta en la terminal.

## Ejecución

```bash
python3 decoy_file_watcher.py

