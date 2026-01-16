from planta import Planta


class Pteridofita(Planta):
    def __init__(self):
        exemplos = ["Samambaia", "Avenca", "Licopódio"]
        super().__init__("Pteridófita", exemplos)

    def perguntas_especificas(self):
        return [
            "A planta tem folhas bem recortadas, parecidas com as de uma samambaia?",
            "Você vê a planta normalmente em locais sombreados e úmidos?",
            "Na parte de baixo das folhas existem pontinhos ou 'bolinhas' escuros (soros)?"
        ]

    def descricao(self):
        return (
            "Pteridófitas são plantas vasculares, como as samambaias, que têm raízes, "
            "caule e folhas, mas não produzem flores, sementes ou frutos."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma pteridófita específica.\n")
        folhas_grandes = classificador.perguntar_sim_nao("Folhas grandes e muito recortadas?")
        folhas_delicadas = classificador.perguntar_sim_nao("Folhas pequenas, delicadas e pendentes?")
        tronco_xaxim = classificador.perguntar_sim_nao("Tem caule com um tronco marrom?")

        if folhas_grandes:
            planta = "Samambaia (folhas grandes recortadas)."
        elif folhas_delicadas:
            planta = "Avenca (folhas finas, comum em casas)."
        elif tronco_xaxim:
            planta = "Xaxim (tronco marrom, folhas no topo)."
        else:
            print('Planta não especificamente identificável no sistema')
        return f"Pteridófita mais provável: {planta}"