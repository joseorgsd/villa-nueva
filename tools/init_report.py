import platform
import datetime

def main():
    print("--- Informe de Inicialización ---")
    print(f"Fecha y Hora: {datetime.datetime.now()}")
    print(f"Sistema Operativo: {platform.system()} {platform.release()}")
    print(f"Directorio de Trabajo: C:\\Villa nueva")
    print("---------------------------------")
    print("¡Todo listo para empezar a trabajar!")

if __name__ == "__main__":
    main()
