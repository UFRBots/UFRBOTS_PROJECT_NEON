import json

# Vai processar nosso json (caso seja passado) e retornar um dicionário.

def get_config(config_file=None):
    if config_file: 
        config = json.loads(open(config_file, 'r').read())
    else:
        config = json.loads(open('config.json', 'r').read())

    return config
