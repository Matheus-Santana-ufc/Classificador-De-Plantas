from planta import Planta


class Gimnosperma(Planta):
    def __init__(self):
        exemplos = ["Pinheiro", "Sequoia", "Cipreste"]
        super().__init__("Gimnosperma", exemplos)

    def perguntas_especificas(self):
        return [
            "A planta é uma árvore alta, com tronco grosso?",
            "As folhas são em forma de agulha ou escamas (como em pinheiros)?",
            "A planta produz 'pinhas' ou cones, em vez de frutos carnosos?"
        ]

    def descricao(self):
        return (
            "Gimnospermas são plantas geralmente arbóreas, com raízes, caule e folhas, "
            "que produzem sementes nuas em cones, mas não produzem frutos verdadeiros."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma gimnosperma específica.\n")
        copa_chuva = classificador.perguntar_sim_nao("Copa em forma de guarda-chuva ou prato?")
        agulhas_longas = classificador.perguntar_sim_nao("Folhas são agulhas longas agrupadas?")
        forma_estreita = classificador.perguntar_sim_nao("Árvore alta e bem estreita?")

        if copa_chuva:
            planta = "Araucária (pinheiro-do-paraná, copa como guarda-chuva)."
        elif agulhas_longas:
            planta = "Pinheiro (agulhas longas em feixes)."
        elif forma_estreita:
            planta = "Cipreste (árvore estreita e alta)."
        else:
            print('Planta não especificamente identificável no sistema')
        return f"Gimnosperma mais provável: {planta}"