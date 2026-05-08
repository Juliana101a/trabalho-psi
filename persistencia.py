import json
import os


def guardar_dados(nome_ficheiro, dados):
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_dados(nome_ficheiro):
    if not os.path.exists(nome_ficheiro):
        return {}

    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        return json.load(f)


