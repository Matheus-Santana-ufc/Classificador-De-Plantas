from planta import Planta


class Pteridofita(Planta):
    def __init__(self):
        exemplos = ["Samambaia", "Avenca", "Licopódio"]
        super().__init__("Pteridófita", exemplos)

    def descricao(self):
        return (
            "Pteridófitas são plantas vasculares, como as samambaias, que têm raízes, "
            "caule e folhas, mas não produzem flores, sementes ou frutos."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma pteridófita específica carioca.\n")

        if classificador.perguntar_sim_nao(
                "Samambaia grande, com 'tronco' grosso no centro e folhas longas saindo do topo?"):
            return "Samambaia-de-metro (Dicksonia sellowiana) - tronco grosso, folhas no topo."

        if classificador.perguntar_sim_nao(
                "Planta pendente com muitos raminhos finos e folhinhas pequenas e delicadas?"):
            return "Avenca (Adiantum raddianum) - raminhos delicados pendentes."

        if classificador.perguntar_sim_nao(
                "Planta com tronco marrom grosso e áspero, com várias folhas apenas na parte de cima?"):
            return "Xaxim (Dicksonia antarctica) - tronco marrom áspero."

        if classificador.perguntar_sim_nao(
                "Samambaia de folhas longas, mais 'rústicas', formando moitas em bordas de mata?"):
            return "Samambaia-rabo-de-gato (Pteridium aquilinum) - folhas rústicas."

        if classificador.perguntar_sim_nao(
                "Samambaia com folhas inteiras (não divididas em muitos folíolos), saindo em roseta do centro?"):
            return "Asplenium"

        print("Planta não especificamente identificável no sistema.")
        return "Pteridófita carioca não catalogada."