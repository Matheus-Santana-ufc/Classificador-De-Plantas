from briofitas import Briofita
from pteridofitas import Pteridofita
from gimnospermas import Gimnosperma
from angiospermas import Angiosperma


class ClassificadorPlantas:
    def __init__(self):
        self.grupos = [
            Briofita(),
            Pteridofita(),
            Gimnosperma(),
            Angiosperma()
        ]

    def perguntar_sim_nao(self, texto):
        while True:
            resp = input(f"{texto} (s/n): ").strip().lower()
            if resp in ("s", "n"):
                return resp == "s"
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    def classificar(self):
        print("\n=== CLASSIFICAÇÃO DE PLANTAS ===\n")
        print("Responda às perguntas observando a planta.\n")

        tem_flores = self.perguntar_sim_nao(
            "Você consegue ver flores na planta?"
        )
        tem_frutos = self.perguntar_sim_nao(
            "Você consegue ver frutos na planta?"
        )
        tem_tronco = self.perguntar_sim_nao(
            "A planta possui um tronco igual a uma árvore?"
        )
        muito_pequena = self.perguntar_sim_nao(
            "A planta é muito pequena (menos de 10 cm)?"
        )
        cresce_umido = self.perguntar_sim_nao(
            "A planta cresce em local úmido e sombreado?"
        )
        if tem_flores and tem_frutos and tem_tronco and muito_pequena and cresce_umido:
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 As respostas não podem ser todas verdadeiras. Tente observer atentamente")
            print("Tente observer atentamente")
            return
        if not tem_flores and not tem_frutos and not tem_tronco and not muito_pequena and not cresce_umido:
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 As respostas não podem ser todas falsas. Tente observer atentamente")
            return

        if muito_pequena and cresce_umido and (tem_flores or tem_frutos):
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 Briófitas (plantas muito pequenas e úmidas) não têm flores. Tente observer atentamente")
            return

        if muito_pequena and tem_tronco:
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 Plantas muito pequenas não possuem tronco. Tente observer atentamente")
            return


        if tem_flores or tem_frutos:
            grupo = Angiosperma()
        elif muito_pequena and cresce_umido and not tem_tronco:
            grupo = Briofita()
        elif tem_tronco and not (tem_flores or tem_frutos):
            folha_agulha = self.perguntar_sim_nao("A folha possui formato semelhante a uma agulha?")
            if folha_agulha:
                grupo = Gimnosperma()
            else:
                grupo = Pteridofita()
        elif cresce_umido:
                grupo = Pteridofita()
        else:
            print("\n❌ Não foi possível identificar o grupo.")
            return


        print(f"\nGrupo identificado: {grupo.nome_grupo()}")
        print(f"{grupo.descricao()}\n")


        resultado_especifico = grupo.detalhar_especie(self)

        print("\n=== RESULTADO FINAL ===")
        print(f'Planta identificada:{ resultado_especifico}')

    def listar_grupos(self):

        print("\n=== GRUPOS DE PLANTAS DISPONÍVEIS ===\n")
        for grupo in self.grupos:
            print(f"📂 {grupo.nome_grupo()}")
            print(f"   {grupo.descricao()}")
            print("   Exemplos Identificáveis pelo Sistema:")
            for exemplo in grupo.exemplos():
                print(f"      • {exemplo}")
            print()
