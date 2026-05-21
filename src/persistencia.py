
import json
import os
import logging

logging.basicConfig(
    filename="sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def carregar_dados(ficheiro):
    try:
        if not os.path.exists(ficheiro):
            return {}
        with open(ficheiro, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Erro carregar {ficheiro}: {e}")
        return {}

def guardar_dados(ficheiro, dados):
    try:
        with open(ficheiro, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Erro guardar {ficheiro}: {e}")




