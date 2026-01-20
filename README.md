🌿 FloraCarioca

Sistema interativo de classificação botânica desenvolvido em Python que utiliza uma árvore de decisão para identificar grupos e espécies específicas da flora do Rio de Janeiro.
📋 Sobre o Projeto

Este projeto aplica os pilares da Programação Orientada a Objetos (POO) para organizar o conhecimento botânico de forma escalável. O sistema guia o usuário através de perguntas sobre características morfológicas, como a presença de flores ou o tamanho da planta, para determinar sua classificação.
🛠️ Pilares de POO na Prática

Abaixo, veja como os conceitos fundamentais foram aplicados diretamente no seu código:
1. Herança

Todas as classes de grupos botânicos herdam características da classe base Planta.
Python

# Arquivo: angiospermas.py
class Angiosperma(Planta): # <--- Aplicação de Herança
    def __init__(self):
        super().__init__("Angiosperma", exemplos) # Reaproveita o construtor do pai

2. Polimorfismo

Cada grupo redefine o método detalhar_especie para executar uma busca específica, embora o nome do método seja o mesmo para todos.
Python

# Cada classe possui sua própria implementação deste método:
def detalhar_especie(self, classificador): 
    # Lógica específica para identificar espécies de seu respectivo grupo

3. Encapsulamento

O uso de atributos com prefixo _ (como self._nome_grupo) indica que esses dados devem ser acessados preferencialmente através de métodos, protegendo a integridade do objeto.
Python

# Arquivo: planta.py
self._nome_grupo = nome_grupo # Atributo protegido

📂 Estrutura de Arquivos

    main.py: Gerencia o fluxo do menu principal.

    classificador.py: O "cérebro" do sistema que contém a árvore de decisão.

    planta.py: A superclasse (pai) que define o molde para todas as plantas.

    Subclasses: briofitas.py, pteridofitas.py, gimnospermas.py e angiospermas.py.

🚀 Como Executar

    Certifique-se de ter o Python 3 instalado.

    Mantenha todos os arquivos na mesma pasta.

    No terminal, execute:
    Bash

    python main.py

📊 Grupos e Exemplos Catalogados
Grupo	Descrição Resumida	Exemplos no Sistema
Briófitas	Pequenas, sem raízes/caule verdadeiros.	Musgo comum, Hepática, Antóceros.
Pteridófitas	Vasculares, sem sementes (locais úmidos).	Samambaia, Avenca, Xaxim, Asplenium.
Gimnospermas	Sementes nuas, sem frutos verdadeiros.	Araucária, Cipreste, Juniperus, Podocarpus.
Angiospermas	Possuem flores e frutos protegendo a semente.	Ipê-Amarelo, Quaresmeira, Manacá, Paubrasília.
💻 Exemplo de Saída
Plaintext

Grupo identificado: Angiosperma
Angiospermas são plantas que produzem flores e frutos...

Vamos identificar uma angiosperma específica da flora carioca.
Árvore com somente flores rosas/roxas? (s/n): s

=== RESULTADO FINAL ===
Planta identificada: Quaresmeira

Sistema desenvolvido para fins educacionais, unindo tecnologia e preservação do conhecimento botânico. 🌿