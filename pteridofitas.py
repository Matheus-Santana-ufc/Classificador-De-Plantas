from planta import Planta


class Pteridofita(Planta):
    def __init__(self):
        exemplos = ["Samambaia-de-Metro","Avenca", "Xaxim","Samambaia-rabo-de-gato","Asplenium"]
        super().__init__("Pteridófita", exemplos)

    def descricao(self):
        return (
            "Pteridófitas são plantas vasculares, como as samambaias, que têm raízes, "
            "caule e folhas, mas não produzem flores, sementes ou frutos e crescem em ambientes úmidos."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma pteridófita específica carioca.\n")

        if classificador.perguntar_sim_nao(
                "A planta tem o crescimento das folhas voltadas para baixo e tem um caule verde?"):
            return " Samambaia-de-metro"

        if classificador.perguntar_sim_nao(
                "A planta tem o crescimento das folhas voltadas para baixo e tem o caule preto?"):
            return " Avenca"

        if classificador.perguntar_sim_nao(
                "A planta com tronco marrom grosso e áspero, com várias folhas apenas na parte de cima?"):
            return " Xaxim"

        if classificador.perguntar_sim_nao(
                "A planta de folhas longas, mais 'rústicas', formando moitas em bordas de mata?"):
            return " Samambaia-rabo-de-gato"

        if classificador.perguntar_sim_nao(
                "As folhas são inteiras e largas (sem divisões) e saindo em um formato circular?"):
            return " Asplenium"

        return " Pteridófita carioca não catalogada."