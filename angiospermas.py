from planta import Planta


class Angiosperma(Planta):
    def __init__(self):
        exemplos = ["Catingueira", "Quaresmeira", "Açaízero"]
        super().__init__("Angiosperma", exemplos)

    def perguntas_especificas(self):
        return [
            "A planta produz flores visíveis em alguma época do ano?",
            "A planta produz frutos (por exemplo, mangas, maçãs, vagens) com sementes dentro?",
            "As sementes ficam sempre protegidas dentro do fruto?"
        ]

    def descricao(self):
        return (
            "Angiospermas são plantas que produzem flores e frutos com sementes "
            "protegidas dentro do fruto, sendo o grupo mais diverso de plantas."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma angiosperma específica.\n")
        frutos_catinga = classificador.perguntar_sim_nao("Frutos pequenos, secos, típicos da caatinga?")
        flores_rosas = classificador.perguntar_sim_nao("Tem flores roxas/rosas vistosas?")
        palmeira_acai = classificador.perguntar_sim_nao("É uma palmeira com cachos de frutos roxos?")

        if frutos_catinga:
            planta = "Catingueira (árvore da caatinga com frutos pequenos)."
        elif flores_rosas:
            planta = "Quaresmeira (flores roxas/rosas vistosas)."
        elif palmeira_acai:
            planta = "Açaizeiro (palmeira com cachos roxos)."
        else:
            print('Planta não especificamente identificável no sistema')
        return f"Angiosperma mais provável: {planta}"