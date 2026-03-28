import os
from dotenv import load_dotenv


def main():
    # Cargamos las variables del .env
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("✅ Entorno configurado correctamente.")
    else:
        print("⚠️ Cuidado: No se encontró la API Key en el archivo .env")


if __name__ == "__main__":
    main()
