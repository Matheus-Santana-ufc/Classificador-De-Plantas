from planta import Planta


class Angiosperma(Planta):
    def __init__(self):
        exemplos = ["Catingueira", "Quaresmeira", "Açaízero"]
        super().__init__("Angiosperma", exemplos)

    def descricao(self):
        return (
            "Angiospermas são plantas que produzem flores e frutos com sementes "
            "protegidas dentro do fruto, sendo o grupo mais diverso de plantas."
        )

    def detalhar_especie(self, classificador):
        print("Vamos identificar uma angiosperma específica da flora carioca.\n")

        if classificador.perguntar_sim_nao(
                "Árvore de médio ou grande porte, tronco lenhoso, copa arredondada e cheia de flores amarelas?"):
            return "Ipê-amarelo"

        if classificador.perguntar_sim_nao(
                "Árvore com flores grandes que mudam de branco para rosa/roxo na mesma copa?"):
            return "Manacá-da-serra"

        if classificador.perguntar_sim_nao(
                "Árvore com somente flores rosas/roxas"):
            return "Quaresmeira"

        if classificador.perguntar_sim_nao(
                "Árvore de porte médio, folhas pequenas em muitos raminhos e vários frutinhos vermelhos?"):
            return "Aroeira-vermelha"

        if classificador.perguntar_sim_nao(
                "Planta de porte menor, com poucos ramos, flores amarelas, sem um tronco grosso bem definido?"):
            return "Paubrasília"

        print("Planta não especificamente identificável no sistema.")
        return "Angiosperma carioca não catalogada aqui."