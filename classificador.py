from briofitas import Briofita
from pteridofitas import Pteridofita
from gimnospermas import Gimnosperma
from angiospermas import Angiosperma


class ClassificadorPlantas:
    def __init__(self):
        self._grupos = [
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

        # ===== PERGUNTAS GERAIS (para identificar o grupo) =====
        tem_flores = self.perguntar_sim_nao(
            "Você consegue ver flores na planta?"
        )
        tem_frutos_visiveis = self.perguntar_sim_nao(
            "Você consegue ver frutos na planta?"
        )
        tem_tronco_lenhoso = self.perguntar_sim_nao(
            "A planta possui um tronco igual a uma árvore?"
        )
        muito_pequena = self.perguntar_sim_nao(
            "A planta é muito pequena (menos de 10 cm) e forma tapete verde?"
        )
        cresce_umido = self.perguntar_sim_nao(
            "Cresce principalmente em local muito úmido e sombreado?"
        )
        if tem_flores and tem_frutos_visiveis and tem_tronco_lenhoso and muito_pequena and cresce_umido:
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 As respostas não podem ser todas verdadeiras. Tente observer atentamente")
            print("Tente observer atentamente")
            return
        if not tem_flores and not tem_frutos_visiveis and not tem_tronco_lenhoso and not muito_pequena and not cresce_umido:
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 As respostas não podem ser todas falsas. Tente observer atentamente")
            return

        if muito_pequena and cresce_umido and tem_flores:
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 Briófitas (plantas muito pequenas e úmidas) não têm flores. Tente observer atentamente")
            return

        if muito_pequena and tem_tronco_lenhoso:
            print("\n❌ Não foi possível identificar o grupo.")
            print("💡 Plantas muito pequenas não possuem tronco. Tente observer atentamente")
            return

        # ===== DECISÃO DO GRUPO =====
        if tem_flores or tem_frutos_visiveis:
            grupo = Angiosperma()
        elif muito_pequena and cresce_umido and not tem_tronco_lenhoso:
            grupo = Briofita()
        elif tem_tronco_lenhoso or self.perguntar_sim_nao(
                "A planta é de médio ou grande porte (acima de 1 metro)?"
        ):
            if self.perguntar_sim_nao(
                    "Folhas em forma de agulha/escamas e produz cones/pinhas?"
            ):
                grupo = Gimnosperma()
            else:
                grupo = Pteridofita()
        else:
            grupo = Pteridofita()

        # ===== DETALHAMENTO ESPECÍFICO (nova parte!) =====
        print(f"\n🟢 Grupo identificado: {grupo.get_nome_grupo()}")
        print(f"   {grupo.descricao()}\n")


        resultado_especifico = grupo.detalhar_especie(self)

        print("\n=== RESULTADO FINAL ===")
        print(resultado_especifico)

    def listar_grupos(self):
        """Lista todos os grupos e seus exemplos."""
        print("\n=== GRUPOS DE PLANTAS DISPONÍVEIS ===\n")
        for grupo in self._grupos:
            print(f"📂 {grupo.get_nome_grupo()}")
            print(f"   {grupo.descricao()}")
            print("   Exemplos Identificáveis pelo Sistema:")
            for exemplo in grupo.get_exemplos():
                print(f"      • {exemplo}")
            print()
