# 🌿 FloraCarioca

---
Sistema interativo de classificação botânica desenvolvido em Python que utiliza uma árvore de decisão para identificar grupos e espécies específicas da flora do Rio de Janeiro.

## 📋 Sobre o Projeto

---
Este é o projeto final da disciplina de Programação Orientada à Objetos, consistindo de um menu interativo onde o usuário deve responder perguntas a respeito das características da planta, podendo descobrir as plantas cariocas em específico, ou ao menos o seu grupo pertencente.
## 📁 Estrutura dos Arquivos

---
- #### main.py: Gerencia o fluxo do menu principal.
- #### classificador.py: O "cérebro" do sistema que contém a árvore de decisão.
- #### planta.py: A superclasse (pai) que define o molde para todas as plantas.
- #### Subclasses: briofitas.py, pteridofitas.py, gimnospermas.py e angiospermas.py.

## 🌱 Grupos e Plantas

---

- ### Angiospermas
    Plantas com Flores ou Frutos. Estão catalogadas no sistema:
    * Ipê-Brasileiro 
    * Quaresmeira
    * Manacá-da-Serra
    * Aroeira Vermelha
    * Paubrasília
    
- ### Gimnospermas
    Grandes plantas com tronco e sementes não protegidas por frutos. Estão catalogadas no sistema:
    * Araucária
    * Podocarpus
    * Cipreste
    * Juniperus

- ### Briófitas
    Pequenas plantas avasculares que crescem em ambientes úmidos, formando um tapete verde.  Estão catalogadas no sistema:
    * Musgo Comum
    * Musgo Pleurocarpo
    * Hepática
    * Antóceros
- ### Pteridófitas
    Plantas vasculares sem sementes que crescem em ambientes úmidos. Estão catalogadas no sistema:
    * Samambaia-de-Metro
    * Avenca
    * Xaxim
    * Samambaia-rabo-de-gato
    * Asplenium

## 🚀 Como Executar

---
Certifique-se de ter o Python 3 instalado.

Mantenha todos os arquivos na mesma pasta.

Execute o arquivo principal:
    
    main.py
## 🏛️ Pilares do POO Aplicados

--- 
### 1. Herança
    class Angiosperma(Planta):
        def __init__(self):
        super().__init__("Angiosperma", exemplos)
### 2. Polimorfismo
    print(f"\nGrupo identificado: {grupo.nome_grupo()}")
    print(f"{grupo.descricao()}\n")
### 3. Encapsulamento
    def nome_grupo(self):
        return self._nome_grupo
    def exemplos(self):
        return self._exemplos 
### 4. Abstração
    class Planta:
    def __init__(self, nome_grupo, exemplos):
        self._nome_grupo = nome_grupo
        self._exemplos = exemplos
## 🔎 Resultados dos Testes

---
    ===== MENU PRINCIPAL =====
    1 - Classificar uma Planta
    2 - Listar Grupos e Plantas Identificáveis pelo Sistema
    0 - Sair
    Escolha uma opção: 1

    === CLASSIFICAÇÃO DE PLANTAS ===

    Responda às perguntas observando a planta.

    Você consegue ver flores na planta? (s/n): s
    Você consegue ver frutos na planta? (s/n): s
    A planta possui um tronco igual a uma árvore? (s/n): n
    A planta é muito pequena (menos de 10 cm)? (s/n): n
    A planta cresce principalmente em local úmido e sombreado? (s/n): n

    Grupo identificado: Angiosperma
    Angiospermas são plantas que produzem flores e frutos com sementes protegidas dentro do fruto, sendo o grupo mais diverso de plantas.
---
    ===== MENU PRINCIPAL =====
    1 - Classificar uma Planta
    2 - Listar Grupos e Plantas Identificáveis pelo Sistema
    0 - Sair
    Escolha uma opção: 2

    === GRUPOS DE PLANTAS DISPONÍVEIS ===

    📂 Briófita  
        Briófitas são plantas pequenas, que vivem em locais úmidos, sem raízes, caule e folhas verdadeiros, e não produzem flores nem frutos.
        Exemplos Identificáveis pelo Sistema:
            • Musgo comum
            • Musgo Pleurocarpo
            • Hepática
            • Antóceros

    📂 Pteridófita
        Pteridófitas são plantas vasculares, como as samambaias, que têm raízes, caule e folhas, mas não produzem flores, sementes ou frutos e crescem em ambientes úmidos.
        Exemplos Identificáveis pelo Sistema:
            • Samambaia-de-Metro
            • Avenca
            • Xaxim
            • Samambaia-rabo-de-gato
            • Asplenium

    📂 Gimnosperma
        Gimnospermas são plantas geralmente arbóreas, com raízes, caule e folhas, que produzem sementes nuas em cones, mas não produzem frutos verdadeiros.
        Exemplos Identificáveis pelo Sistema:
            • Araucária
            • Podocarpus
            • Cipreste
            • Juniperus

    📂 Angiosperma
        Angiospermas são plantas que produzem flores e frutos com sementes protegidas dentro do fruto, sendo o grupo mais diverso de plantas.
        Exemplos Identificáveis pelo Sistema:
            • Ipê-Amarelo
            • Quaresmeira
            • Manacá-da-Serra
            • Aroeira Vermelha
            • Paubrasília

---

    === CLASSIFICAÇÃO DE PLANTAS ===

    Responda às perguntas observando a planta.

    Você consegue ver flores na planta? (s/n): s
    Você consegue ver frutos na planta? (s/n): s
    A planta possui um tronco igual a uma árvore? (s/n): n
    A planta é muito pequena (menos de 10 cm)? (s/n): n
    A planta cresce em local úmido e sombreado? (s/n): s

    Grupo identificado: Angiosperma
    Angiospermas são plantas que produzem flores e frutos com sementes protegidas dentro do fruto, sendo o grupo mais diverso de plantas.

    Vamos identificar uma angiosperma específica da flora carioca.

    Árvore de médio ou grande porte, tronco lenhoso, copa arredondada e cheia de flores amarelas? (s/n): n
    Árvore com flores grandes que mudam de branco para rosa/roxo na mesma copa? (s/n): n
    Árvore com somente flores rosas/roxas (s/n): s

    === RESULTADO FINAL ===
    Planta identificada: Quaresmeira

---

[UML Classificador de Plantas.drawio.pdf](https://github.com/user-attachments/files/24766522/UML.Classificador.de.Plantas.drawio.pdf)
