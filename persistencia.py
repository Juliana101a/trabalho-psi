import json
import os


def guardar_dados(ficheiro, dados):
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_dados(ficheiro):
    if not os.path.exists(ficheiro):
        return {}

    with open(ficheiro, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()
        return json.loads(conteudo) if conteudo else {}

