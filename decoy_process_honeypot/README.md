# Proyecto Honeypot de Procesos - para aprender, practicar y compartir.

Hola, soy Inma
Despues de casi 10 años trabajando en otro sector, decidí dar un giro total a mi vida y meterme
en lo que realmente me gustaba, en el mundo de la "CIBERSEGURIDAD".
Este es uno de mis primeros proyectos prácticos, crreado paso a paso mientras aprendía a programar
en Python y entender cómo piensan los atacantes.

Si tú también estás empezando, este repositorio es para tu. Vas a ver cómo se construye algo útil,
sencillo y real sin ser experta ni usar herramientas raras.

## ¿Qué hace este proyecto?

Simula un "proceso trampa (honeypot)".
Es decir, un proceso con nombre llamativo (como 'Isass' o 'ssh') que puede atraer malware, scripts 
autómaticos o curioseos de atacantes.

El script_
- Lanza un proceso camuflado.
- Lo monitoriza constantemente.
- Si alguien lo cierra o lo mata, "genera una alerta" y lo guarda en un log.
- Todo con Python puro y fácil de entender.

## ¿Que incluye el repositorio?

| Versión    |   Descripción     |   Archivo       |
|--------------------------------------------------|
|   V1       | Script que lista  |'versiones/v1_   |
|            |procesos activos   |listado_procesos |
|            | del sistema       | .py'            |
|--------------------------------------------------|
|   V2       | Lanza un proceso  |'versiones/v2_   |
|            |señuelo con nombre |proceso_señuelo  |
|            |llamativo          | .py'            |
|--------------------------------------------------|
|   V3       | Vigila el proceso |'versiones/v3_   |
|            | y detecta si lo   |vigilancia.py    |
|            |matan. Guarda logs.|                 |
----------------------------------------------------

## Cómo usarlo

1. Asegurate de tener Python instalado.
2. Abre terminal en la carpeta del proyecto.
3. Ejecuta la versión que quieras:

  '''bash
  python versiones/v3_vigilancia.py

4. En otra terminal, mata el proceso manualmente(usa
el PID que aparece).

     *Linux:kill <PID>
     *Windows_ taskkill /PID <PID> /F
5. Revisa la consola y el archivo honeypot_log.txt  