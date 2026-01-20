from planta import Planta


class Gimnosperma(Planta):
    def __init__(self):
        exemplos = ["Araucária","Podocarpus", "Cipreste","Juniperus"]
        super().__init__("Gimnosperma", exemplos)

    def descricao(self):
        return (
            "Gimnospermas são plantas geralmente arbóreas, com raízes, caule e folhas, "
            "que produzem sementes nuas em cones, mas não produzem frutos verdadeiros."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma gimnosperma específica da flora carioca.\n")

        if classificador.perguntar_sim_nao(
                "Árvore alta com tronco reto e copa no topo parecendo um guarda-chuva ou candelabro?"):
            return " Araucária"

        if classificador.perguntar_sim_nao(
                "Árvore muito estreita e alta, em forma de coluna, com ramos bem fechados junto ao tronco?"):
            return " Cipreste"

        if classificador.perguntar_sim_nao(
                "Arbusto ou árvore pequena com raminhos finos e folhas em forma de escamas, lembrando um 'mini-cipreste'?"):
            return " Juniperus"

        if classificador.perguntar_sim_nao(
                "Árvore de porte médio, copa arredondada, folhas estreitas, em áreas muito úmidas e altas?"):
            return " Podocarpus"

        return "Gimnosperma carioca não catalogada."
