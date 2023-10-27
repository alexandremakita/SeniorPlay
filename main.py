import pygame
import random
import string
import json  # Adicionado para salvar e carregar dados

pygame.init()
fonte_grande = pygame.font.Font(None, 48)

retangulo_voltar = pygame.Rect(10, 10, 110, 40)
retangulo_adicionar = pygame.Rect(600, 100, 200, 50)
retangulo_confirmar = pygame.Rect(600, 160, 200, 50)

# Defina suas listas de palavras aqui
palavras_facil = ["girafa", "banana", "carro", "sorvete", "abacaxi", "macaco", "biciclo", "cadeira", "computador", "elefante", "janela", "morango", "parafuso", "teclado", "pincel", "pessoa", "relogio", "violino", "xicara"]
palavras_medio = ["aventura", "computador", "eletronica", "monitor", "bicicleta", "resistencia", "televisao", "apartamento", "pneumatico", "aprendizado", "frutas", "estudante", "elefantes", "aniversario", "piscina", "cachorro", "documentos", "luminaria", "escritorio", "telescopio"]
palavras_dificil = ["comunicaçcao", "responsavel", "inteligencia", "independente", "planejamento", "empreendedor", "sustentavel", "organizacao", "estrategico", "interessante", "extraordinario"]

usuarios = []
def mostrar_menu_touch(tela):
    fonte = pygame.font.Font(None, 48)
    cor_texto = (255, 255, 255)
    
    # Desenhe os retângulos clicáveis para as opções "Jogar" e "Sair"
    retangulo_jogar = pygame.Rect(300, 200, 200, 50)
    pygame.draw.rect(tela, (0, 255, 0), retangulo_jogar)
    texto_jogar = fonte.render("Jogar", True, cor_texto)
    tela.blit(texto_jogar, (325, 210))

    retangulo_sair = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(tela, (255, 0, 0), retangulo_sair)
    texto_sair = fonte.render("Sair", True, cor_texto)
    tela.blit(texto_sair, (335, 310))

    return retangulo_jogar, retangulo_sair


def escolher_palavra(nivel):
    if nivel == 1:
        return random.choice(palavras_facil)
    elif nivel == 2:
        return random.choice(palavras_medio)
    elif nivel == 3:
        return random.choice(palavras_dificil)

def organizar_teclado():
    letras = list(string.ascii_lowercase)
    teclado = []

    linha_atual = []
    for letra in letras:
        linha_atual.append(letra)
        if len(linha_atual) == 7:
            teclado.append(linha_atual)
            linha_atual = []

    if linha_atual:
        teclado.append(linha_atual)

    return teclado

def mostrar_menu(tela):
    fonte = pygame.font.Font(None, 48)
    cor_texto = (255, 255, 255)
    texto_titulo = fonte.render("Jogo da Forca", True, cor_texto)
    tela.blit(texto_titulo, (300, 100))

    fonte = pygame.font.Font(None, 36)
    texto_instrucoes = fonte.render("Pressione 1 para Jogar", True, cor_texto)
    tela.blit(texto_instrucoes, (300, 200))

    texto_sair = fonte.render("Pressione 0 para Sair", True, cor_texto)
    tela.blit(texto_sair, (300, 250))

def desenhar_vidas(tela, vidas):
    fonte = pygame.font.Font(None, 36)
    cor_texto = (255, 0, 0)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, cor_texto)
    tela.blit(texto_vidas, (20, 20))

def desenhar_teclado(tela, teclado, letras_incorretas, letras_corretas):
    fonte = pygame.font.Font(None, 36)
    cor_texto = (255, 255, 255)
    tecla_largura = 40
    tecla_altura = 40

    for linha in range(len(teclado)):
        for coluna in range(len(teclado[linha])):
            letra = teclado[linha][coluna]
            cor = (255, 0, 0) if letra in letras_incorretas else (0, 255, 0) if letra in letras_corretas else (0, 0, 0)
            
            pygame.draw.rect(tela, cor, (coluna * tecla_largura + 150, linha * tecla_altura + 300, tecla_largura, tecla_altura))
            
            letra_texto = fonte.render(letra, True, cor_texto)
            tela.blit(letra_texto, (coluna * tecla_largura + 10 + 150, linha * tecla_altura + 300 + 10))


def selecao_dificuldade():
    tela = pygame.display.set_mode((800, 600))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Verifique eventos de toque
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if retangulo_facil.collidepoint(x, y):
                    return 1  # Fácil
                elif retangulo_medio.collidepoint(x, y):
                    return 2  # Médio
                elif retangulo_dificil.collidepoint(x, y):
                    return 3  # Difícil

        tela.fill((0, 0, 0))
        retangulo_facil, retangulo_medio, retangulo_dificil = mostrar_menu_dificuldade(tela)
        pygame.display.flip()

def mostrar_menu_dificuldade(tela):
    fonte = pygame.font.Font(None, 48)
    cor_texto = (255, 255, 255)
    
    pergunta = fonte.render("Dificuldade:", True, cor_texto)
    tela.blit(pergunta, (330, 110))
    # Desenhe os retângulos clicáveis para as opções de dificuldade
    retangulo_facil = pygame.Rect(300, 200, 200, 50)
    pygame.draw.rect(tela, (0, 255, 0), retangulo_facil)
    texto_facil = fonte.render("Fácil", True, cor_texto)
    tela.blit(texto_facil, (330, 210))

    retangulo_medio = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(tela, (255, 255, 0), retangulo_medio)
    texto_medio = fonte.render("Médio", True, cor_texto)
    tela.blit(texto_medio, (330, 310))

    retangulo_dificil = pygame.Rect(300, 400, 200, 50)
    pygame.draw.rect(tela, (255, 0, 0), retangulo_dificil)
    texto_dificil = fonte.render("Difícil", True, cor_texto)
    tela.blit(texto_dificil, (330, 410))

    return retangulo_facil, retangulo_medio, retangulo_dificil
def jogar():
    nivel = selecao_dificuldade()
    

    palavra = escolher_palavra(nivel)
    letras_corretas = set()
    letras_incorretas = set()
    vidas = 5

    # Configuração da janela do Pygame
    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Jogo da Forca")

    # Outras configurações de aparência
    fonte = pygame.font.Font(None, 36)
    cor_texto = (255, 255, 255)
    
    teclado = organizar_teclado()

    print("Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")

    while vidas > 0:
        palavra_oculta = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_oculta += letra
            else:
                palavra_oculta += "_"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 470 and 300 <= y <= 540:  # Verifica se o toque ocorreu na área do teclado
                    coluna = (x - 150) // 40
                    linha = (y - 300) // 40
                    letra_tentativa = teclado[linha][coluna].lower()

                    if letra_tentativa in letras_incorretas or letra_tentativa in letras_corretas:
                        print("Você já tentou esta letra antes.")
                    else:
                        if letra_tentativa in palavra:
                            letras_corretas.add(letra_tentativa)
                        else:
                            letras_incorretas.add(letra_tentativa)
                            vidas -= 1
                            print("Letra errada. Tente novamente.")

        tela.fill((0, 0, 0))
        
        if palavra_oculta == palavra:
            fonte_vitoria = pygame.font.Font(None, 48)
            texto_vitoria = fonte_vitoria.render("Parabéns! Você acertou a palavra.", True, (0, 255, 0))
            tela.blit(texto_vitoria, (200, 250))
        else:
            desenhar_vidas(tela, vidas)
            
            texto_palavra = fonte.render(f"Palavra: {palavra_oculta}", True, cor_texto)
            tela.blit(texto_palavra, (300, 100))
            desenhar_teclado(tela, teclado,letras_incorretas,letras_corretas)

        pygame.display.flip()

        if palavra_oculta == palavra:
            break

    if vidas == 0:
      print(f"Fim de jogo. A palavra era: {palavra}")
      

      tela_nome_usuario = pygame.display.set_mode((800, 600))
      fonte = pygame.font.Font(None, 36)
      cor_texto = (255, 255, 255)
      input_rect = pygame.Rect(300, 250, 200, 32)
      nome_usuario = ""

      while True:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  return

              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RETURN:
                      usuario_partida = nome_usuario
                      salvar_estatisticas(False, nivel, usuario_partida)
                      jogar_novamente = menu_confirmacao()
                      if not jogar_novamente:
                        main()
                  elif event.key == pygame.K_BACKSPACE:
                      nome_usuario = nome_usuario[:-1]
                  elif event.unicode and event.unicode.isprintable():        
                    nome_usuario += event.unicode

          tela_nome_usuario.fill((0, 0, 0))
          inserir_nome_usuario(tela_nome_usuario, fonte, cor_texto, input_rect, nome_usuario)
          pygame.display.flip()

      
    else:
      # Comentando a linha abaixo, já que agora vamos inserir o nome do usuário na tela
      # usuario_partida = input("Digite o nome do usuário para atualizar o histórico: ")

      tela_nome_usuario = pygame.display.set_mode((800, 600))
      fonte = pygame.font.Font(None, 36)
      cor_texto = (255, 255, 255)
      input_rect = pygame.Rect(300, 250, 200, 32)
      nome_usuario = ""

      while True:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  return

              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RETURN:
                    usuario_partida = nome_usuario
                    salvar_estatisticas(True, nivel, usuario_partida)
                    jogar_novamente = menu_confirmacao()
                    if not jogar_novamente:
                      main()
                  elif event.key == pygame.K_BACKSPACE:
                      nome_usuario = nome_usuario[:-1]
                  elif event.unicode and event.unicode.isprintable():
                      nome_usuario += event.unicode

          tela_nome_usuario.fill((0, 0, 0))
          inserir_nome_usuario(tela_nome_usuario, fonte, cor_texto, input_rect, nome_usuario)
          pygame.display.flip()


    
def inserir_nome_usuario(tela, fonte, cor_texto, input_rect, nome_usuario):
  pygame.draw.rect(tela, (255, 255, 255), input_rect, 2)
  texto_input = fonte.render(nome_usuario, True, cor_texto)
  tela.blit(texto_input, (input_rect.x + 5, input_rect.y + 5))


def salvar_estatisticas(vitoria, nivel, usuario_partida):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["nome"] == usuario_partida:
            usuario["vitorias"] += 1 if vitoria else 0

    salvar_usuarios(usuarios)

def carregar_estatisticas(usuario):
    try:
        with open(f"usuarios.json", "r") as file:
            estatisticas = json.load(file)
    except FileNotFoundError:
        estatisticas = {}
    return estatisticas


def salvar_estatisticas_usuario(usuario, estatisticas):
    with open(f"estatisticas_{usuario}.json", "w") as file:
        json.dump(estatisticas, file)


def mostrar_estatisticas(usuario):
    estatisticas = carregar_estatisticas(usuario)
    print("Estatísticas:")
    for nivel, dados in estatisticas.items():
        jogos_jogados = dados["jogos_jogados"]
        vitorias = dados["vitorias"]
        porcentagem_vitoria = (vitorias / jogos_jogados) * 100 if jogos_jogados > 0 else 0
        print(f"Nível {nivel}: Jogos Jogados: {jogos_jogados}, Vitórias: {vitorias}, Porcentagem de Vitória: {porcentagem_vitoria:.2f}%")





def mostrar_menu_confirmacao(tela):
    fonte = pygame.font.Font(None, 48)
    cor_texto = (255, 255, 255)

    pergunta = fonte.render("Jogar novamente?", True, cor_texto)
    tela.blit(pergunta, (330, 110))
    # Desenhe os retângulos clicáveis para as opções "Sim" e "Não"
    retangulo_sim = pygame.Rect(250, 300, 150, 50)
    pygame.draw.rect(tela, (0, 255, 0), retangulo_sim)
    texto_sim = fonte.render("Sim", True, cor_texto)
    tela.blit(texto_sim, (290, 310))

    retangulo_nao = pygame.Rect(450, 300, 150, 50)
    pygame.draw.rect(tela, (255, 0, 0), retangulo_nao)
    texto_nao = fonte.render("Não", True, cor_texto)
    tela.blit(texto_nao, (485, 310))

    return retangulo_sim, retangulo_nao


def menu_confirmacao():
        tela = pygame.display.set_mode((800, 600))

        retangulo_sim = None
        retangulo_nao = None

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

                # Verifique eventos de toque
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if retangulo_sim and retangulo_sim.collidepoint(x, y):
                        return True  # Jogar novamente
                    elif retangulo_nao and retangulo_nao.collidepoint(x, y):
                        return False  # Não jogar novamente

            tela.fill((0, 0, 0))
            retangulo_sim, retangulo_nao = mostrar_menu_confirmacao(tela)
            pygame.display.flip()


def mostrar_menu_touch(tela):
    fonte = pygame.font.Font(None, 48)
    cor_texto = (255, 255, 255)
    
    # Desenhe os retângulos clicáveis para as opções "Jogar", "Usuários" e "Sair"
    retangulo_jogar = pygame.Rect(300, 200, 200, 50)
    pygame.draw.rect(tela, (0, 255, 0), retangulo_jogar)
    texto_jogar = fonte.render("Jogar", True, cor_texto)
    tela.blit(texto_jogar, (325, 210))

    retangulo_usuarios = pygame.Rect(300, 250, 200, 50)
    pygame.draw.rect(tela, (0, 0, 255), retangulo_usuarios)
    texto_usuarios = fonte.render("Usuários", True, cor_texto)
    tela.blit(texto_usuarios, (310, 260))

    retangulo_sair = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(tela, (255, 0, 0), retangulo_sair)
    texto_sair = fonte.render("Sair", True, cor_texto)
    tela.blit(texto_sair, (335, 310))

    return retangulo_jogar, retangulo_usuarios, retangulo_sair

# Nova função para mostrar a lista de botões de usuários
def mostrar_menu_usuarios(tela, adicionando_usuario, nome_usuario, input_rect, usuarios, fonte, cor_texto):
    fonte = pygame.font.Font(None, 48)
    cor_texto = (255, 255, 255)

    # Adicione a linha abaixo para criar os botões de usuários
    botoes_usuarios = criar_botoes_usuarios(usuarios, fonte, cor_texto)

    # Sempre desenhe o botão "Voltar"
    retangulo_voltar = pygame.Rect(50, 10, 110, 40)
    pygame.draw.rect(tela, (255, 0, 0), retangulo_voltar)
    texto_voltar = fonte.render("Voltar", True, cor_texto)
    tela.blit(texto_voltar, (60, 20))

    retangulo_adicionar = pygame.Rect(600, 100, 200, 50)
    pygame.draw.rect(tela, (0, 255, 0), retangulo_adicionar)
    texto_adicionar = fonte.render("Adicionar", True, cor_texto)
    tela.blit(texto_adicionar, (600, 110))

    if adicionando_usuario:
        # Desenhe a barra de inserção e o botão de confirmar apenas quando estiver adicionando um usuário
        pygame.draw.rect(tela, (255, 255, 255), input_rect, 2)
        texto_input = fonte.render(nome_usuario, True, cor_texto)
        tela.blit(texto_input, (input_rect.x + 5, input_rect.y + 5))

        

        # Adicione um retângulo e texto para o botão "Confirmar"
        retangulo_confirmar = pygame.Rect(600, 160, 200, 50)
        pygame.draw.rect(tela, (255, 0, 0), retangulo_confirmar)
        texto_confirmar = fonte.render("Confirmar", True, cor_texto)
        tela.blit(texto_confirmar, (600, 170))

    mostrar_usuarios(tela, botoes_usuarios, fonte, cor_texto)
    return botoes_usuarios



def tela_usuarios(usuarios):
    tela = pygame.display.set_mode((800, 600))
    fonte = pygame.font.Font(None, 36)
    cor_texto = (255, 255, 255)

    # Variáveis para o campo de texto e botão "Adicionar"
    input_rect = pygame.Rect(50, 50, 200, 32)
    nome_usuario = ""
    adicionando_usuario = False

    # Adicione a linha abaixo para criar os botões de usuários
    botoes_usuarios = criar_botoes_usuarios(usuarios, fonte, cor_texto)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Verifique eventos de toque
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if retangulo_voltar.collidepoint(x, y):
                    return  # Volta para o menu anterior
                elif not adicionando_usuario and retangulo_adicionar.collidepoint(x, y):
                    adicionando_usuario = True
                elif adicionando_usuario and retangulo_confirmar.collidepoint(x, y):
                    # Adiciona o novo usuário
                    novo_usuario = {"nome": nome_usuario, "vitorias": 0}
                    usuarios.append(novo_usuario)
                    nome_usuario = ""
                    adicionando_usuario = False
                    salvar_usuarios(usuarios)  # Salva a lista atualizada no arquivo JSON
                    pygame.display.flip()  # Atualiza a tela imediatamente
                else:
                    # Verifica se algum botão de usuário foi clicado
                    for retangulo, usuario_info in botoes_usuarios:
                      if retangulo.collidepoint(x, y):
                        print(f"Usuário {usuario_info['nome']} clicado!")
                        retangulo_detalhes = mostrar_detalhes_usuario(tela, usuario_info, fonte_grande, cor_texto)  # Nova função para mostrar detalhes

            if adicionando_usuario and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Adiciona o novo usuário
                    novo_usuario = {"nome": nome_usuario, "vitorias": 0}
                    usuarios.append(novo_usuario)
                    nome_usuario = ""
                    adicionando_usuario = False
                    salvar_usuarios(usuarios)  # Salva a lista atualizada no arquivo JSON
                    pygame.display.flip()  # Atualiza a tela imediatamente
                elif event.key == pygame.K_BACKSPACE:
                    nome_usuario = nome_usuario[:-1]
                else:
                    nome_usuario += event.unicode

        tela.fill((0, 0, 0))
        botoes_usuarios = mostrar_menu_usuarios(tela, adicionando_usuario, nome_usuario, input_rect, usuarios, fonte, cor_texto)
        mostrar_usuarios(tela, botoes_usuarios, fonte, cor_texto)

        pygame.display.flip()

        




# Adicione a linha abaixo para criar os botões de usuários

def retangulo_voltar_menu_inicial(tela, fonte, cor_texto):
    retangulo_voltar = pygame.Rect(50, 10, 110, 40)
    pygame.draw.rect(tela, (255, 0, 0), retangulo_voltar)
    texto_voltar = fonte.render("Voltar", True, cor_texto)
    tela.blit(texto_voltar, (60, 20))
    return retangulo_voltar

def mostrar_detalhes_usuario(tela, usuario_info, fonte_grande, cor_texto):
    tela.fill((0, 0, 0))
    texto_detalhes = fonte_grande.render(f"Detalhes do Usuário {usuario_info['nome']}", True, cor_texto)
    tela.blit(texto_detalhes, (150, 50))

    # Exibe todas as informações do usuário
    texto_nome = fonte_grande.render(f"Nome: {usuario_info['nome']}", True, cor_texto)
    tela.blit(texto_nome, (150, 150))

    texto_vitorias = fonte_grande.render(f"Vitórias: {usuario_info['vitorias']}", True, cor_texto)
    tela.blit(texto_vitorias, (150, 200))

    pygame.display.flip()

    return retangulo_voltar_menu_inicial(tela, fonte_grande, cor_texto)  # Nova função para botão "Voltar"

#

def criar_botoes_usuarios(lista_usuarios, fonte, cor_texto):
    botoes_usuarios = []
    for i, usuario in enumerate(lista_usuarios):
        retangulo_usuario = pygame.Rect(50, 200 + i * 40, 200, 30)
        botoes_usuarios.append((retangulo_usuario, usuario))
    return botoes_usuarios

# Atualize a função mostrar_usuarios
def mostrar_usuarios(tela, botoes_usuarios, fonte, cor_texto):

    for retangulo, usuario_info in botoes_usuarios:
        pygame.draw.rect(tela, (0, 255, 0), retangulo)
        texto_usuario = fonte.render(usuario_info['nome'], True, cor_texto)
        tela.blit(texto_usuario, (retangulo.x + 10, retangulo.y + 5))

    # Adicione o botão "Detalhes"
    retangulo_detalhes = pygame.Rect(600, 400, 150, 50)
    pygame.draw.rect(tela, (0, 0, 255), retangulo_detalhes)
    texto_detalhes = fonte.render("Detalhes", True, cor_texto)
    tela.blit(texto_detalhes, (620, 410))

    return retangulo_detalhes


def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)
        return usuarios
    except FileNotFoundError:
        return []

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=2)


def main():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    
    # Declare as variáveis de retângulo
    retangulo_jogar = None
    retangulo_usuarios = None
    retangulo_sair = None

    # Carrega automaticamente os usuários do arquivo JSON
    usuarios = carregar_usuarios()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Verifique eventos de toque
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if retangulo_jogar.collidepoint(x, y):
                    if not jogar():
                        pygame.quit()
                        return  # O jogador escolheu sair após a partida
                elif retangulo_usuarios.collidepoint(x, y):
                    tela_usuarios(usuarios)  # Mostra a tela de listagem de usuários
                elif retangulo_sair.collidepoint(x, y):
                    pygame.quit()
                    return

        tela.fill((0, 0, 0))
        retangulo_jogar, retangulo_usuarios, retangulo_sair = mostrar_menu_touch(tela)
        pygame.display.flip()

if __name__ == "__main__":
    main()

