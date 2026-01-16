class Planta:
    def __init__(self, nome_grupo, exemplos):
        self._nome_grupo = nome_grupo
        self._exemplos = exemplos

    def get_nome_grupo(self):
        return self._nome_grupo

    def get_exemplos(self):
        return self._exemplos