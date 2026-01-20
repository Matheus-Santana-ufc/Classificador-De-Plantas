from planta import Planta


class Briofita(Planta):
    def __init__(self):
        exemplos = ["Musgo comum","Musgo Pleurocarpo", "Hepática", "Antóceros"]
        super().__init__("Briófita", exemplos)

    def descricao(self):
        return (
            "Briófitas são plantas pequenas, que vivem em locais úmidos, sem raízes, "
            "caule e folhas verdadeiros, e não produzem flores nem frutos."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma briófita específica da flora carioca.\n")

        if classificador.perguntar_sim_nao("Forma um tapete verde cobrindo pedras, troncos ou solo?"):
            return " Musgo comum"

        if classificador.perguntar_sim_nao(
                "Parece uma 'folha' achatada grudada no solo úmido, com formato de lâmina larga?"):
            return " Hepática"

        if classificador.perguntar_sim_nao(
                "Massa verde-escura baixa, com pequenas estruturas finas e alongadas saindo para cima?"):
            return " Antóceros"

        if classificador.perguntar_sim_nao(
                "Cresce em troncos sombreados, com raminhos finos que parecem mini galhos pendentes?"):
            return " Musgo pleurocarpo"

        return " Briófita carioca não catalogada."