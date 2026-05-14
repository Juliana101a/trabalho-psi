import json
import os


def guardar_dados(ficheiro, dados):
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_dados(ficheiro):
    if not os.path.exists(ficheiro):
        return {}

    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}










