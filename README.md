# certenum
Certenum es una herramienta de línea de comandos escrita en Python que te permite consultar certificados de dominio y mostrar información específica de ellos. Puedes utilizar Certenum para obtener datos clave de certificados de dominio, como tiempos de validez, información del emisor, nombres de dominio y números de serie.
# Características
Consulta certificados de dominio en línea.
Muestra información detallada de los certificados.
Personaliza la información que deseas ver utilizando parametros de línea de comandos.
Interfaz de línea de comandos sencilla y fácil de usar.
# Instalacion
```
git clone https://github.com/Entidad-4766/certenum.git && cd certenum && chmod +x certenum.py
```
Despues instalamos los requirements
```
pip install -r requirements.txt
```
# Uso Básico
De esta manera mostrata toda la informacion del certificado.
``` 
  python certenum.py -a dominio.com
```
# Opciones de Visualización
Con los parametros podras ver de manera espesifica el output. Usa el parametro `-h` para ver los demas parametros.
```
python certenum.py -h                 
usage: certenum.py [-h] [-t] [-i] [-c] [-n] [-s] [-a] domain

Consulta certificados de dominio y muestra información específica.

positional arguments:
  domain        Nombre de dominio a consultar

options:
  -h, --help    show this help message and exit
  -t, --times   Mostrar tiempos del certificado
  -i, --issuer  Mostrar información del emisor
  -c, --common  Mostrar common_name del certificado
  -n, --name    Mostrar nombres del dominio
  -s, --serial  Mostrar serial_number del certificado
  -a, --all     Mostrar toda la información
```
# Ejemplos de uso
En este ejemplo veremos solo los nombres de dominio y los tiempos del certificado y una parte del output
```
python certenum.py -t -n example.com
Tiempos de Certificado:
entry_timestamp: 2023-03-17T16:26:38.016
not_before: 2023-01-13T00:00:00
not_after: 2024-02-13T23:59:59
Nombres del Dominio:
example.com
www.example.com
```
