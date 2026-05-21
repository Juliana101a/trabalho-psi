
import json
import os

from logger import log_info, log_error


def carregar_dados(ficheiro):
    try:
        if not os.path.exists(ficheiro):
            log_info(f"Ficheiro {ficheiro} não existe")
            return {}

        with open(ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)

        log_info(f"Dados carregados de {ficheiro}")
        return dados

    except Exception as e:
        log_error(f"Erro ao carregar {ficheiro}: {e}")
        return {}


def guardar_dados(ficheiro, dados):
    try:
        with open(ficheiro, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        log_info(f"Dados guardados em {ficheiro}")

    except Exception as e:
        log_error(f"Erro ao guardar {ficheiro}: {e}")





