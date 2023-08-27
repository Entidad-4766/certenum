import argparse
import requests
import json
from colorama import Fore, Style, init

init(autoreset=True)

def consultar_certificados_dominio(nombre_dominio):
    url = f'https://crt.sh/?q={nombre_dominio}&output=json'
    
    try:
        # Realiza la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Genera una excepción si la solicitud no tiene éxito
        data = response.json()  # Analiza la respuesta JSON como una lista
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

def mostrar_certificado(data, mostrar_tiempos=True, mostrar_emisor=True, mostrar_comun=True, mostrar_nombre=True, mostrar_serial=True, mostrar_todo=False):
    for item in data:
        if mostrar_tiempos:
	          # Para cambiar el color solo cambiar la palabra del color despues del Fore.
            print(Fore.GREEN + "Tiempos de Certificado:")
            print(Fore.YELLOW + f"entry_timestamp: " + Fore.WHITE + f"{item['entry_timestamp']}")
            print(Fore.YELLOW + f"not_before: " + Fore.WHITE + f"{item['not_before']}")
            print(Fore.YELLOW + f"not_after: " + Fore.WHITE + f"{item['not_after']}")

        if mostrar_emisor:
            print(Fore.GREEN + "Información del Emisor:")
            print(Fore.YELLOW + f"issuer_ca_id: " + Fore.WHITE + f"{item['issuer_ca_id']}")
            if mostrar_todo:
                print(Fore.YELLOW + f"issuer_name: " + Fore.WHITE + f"{item['issuer_name']}", end="\n\n")
            else:
                print(Fore.YELLOW + f"issuer_name: " + Fore.WHITE + f"{item['issuer_name']}")

        if mostrar_comun:
            print(Fore.YELLOW + f"common_name: " + Fore.WHITE + f"{item['common_name']}")

        if mostrar_nombre:
            print(Fore.GREEN + "Nombres del Dominio:")
            name_values = item['name_value'].split('\n')
            for name in name_values:
                print(Fore.YELLOW + name)

        if mostrar_serial:
            print(Fore.YELLOW + f"serial_number: " + Fore.WHITE + f"{item['serial_number']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consulta certificados de dominio y muestra información específica.")
    parser.add_argument("-t", "--times", action="store_true", help="Mostrar tiempos del certificado")
    parser.add_argument("-i", "--issuer", action="store_true", help="Mostrar información del emisor")
    parser.add_argument("-c", "--common", action="store_true", help="Mostrar common_name del certificado")
    parser.add_argument("-n", "--name", action="store_true", help="Mostrar nombres del dominio")
    parser.add_argument("-s", "--serial", action="store_true", help="Mostrar serial_number del certificado")
    parser.add_argument("-a", "--all", action="store_true", help="Mostrar toda la información")
    parser.add_argument("domain", help="Nombre de dominio a consultar")
    args = parser.parse_args()

    #Muestra todo el contenido
    if not any(vars(args).values()):
        args.all = True

    # Realiza la consulta y obtiene data
    data = consultar_certificados_dominio(args.domain)

    if data:
        # Llama a la función para mostrar la información según los parámetros
        mostrar_certificado(data, args.all or args.times, args.all or args.issuer, args.all or args.common, args.all or args.name, args.all or args.serial)
