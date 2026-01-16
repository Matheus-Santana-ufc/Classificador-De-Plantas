from planta import Planta


class Briofita(Planta):
    def __init__(self):
        exemplos = ["Musgo", "Hepática", "Antóceros"]
        super().__init__("Briófita", exemplos)

    def perguntas_especificas(self):
        return [
            "A planta é bem pequena (geralmente poucos centímetros)?",
            "A planta parece um tapete verde grudado em superfícies úmidas (rochas, troncos, solo)?",
            "A planta não tem caule duro nem tronco visível?"
        ]

    def descricao(self):
        return (
            "Briófitas são plantas pequenas, que vivem em locais úmidos, sem raízes, "
            "caule e folhas verdadeiros, e não produzem flores nem frutos."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma briófita específica.\n")
        cresce_em_rocha = classificador.perguntar_sim_nao("Cresce em rochas ou muros?")
        folhas_planas = classificador.perguntar_sim_nao("Tem folhas achatadas e verdes brilhantes?")
        escura = classificador.perguntar_sim_nao("É mais escura e cresce em solo úmido?")

        if cresce_em_rocha:
            planta = "Musgo (comum em pedras e muros úmidos)."
        elif folhas_planas:
            planta = "Hepáticas (folhas achatadas, verde brilhante)."
        elif escura:
            planta = "Antóceros (escuro, em solo úmido)."
        else:
            print('Planta não especificamente identificável no sistema')

        return f"Briófita mais provável: {planta}"