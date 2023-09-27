import pygame
import random
import string

pygame.init()

# Defina suas listas de palavras aqui
palavras_facil = ["girafa", "banana", "carro", "sorvete", "abacaxi", "macaco", "biciclo", "cadeira", "computador", "elefante", "janela", "morango", "parafuso", "teclado", "pincel", "pessoa", "relogio", "violino", "xicara"]
palavras_medio = ["aventura", "computador", "eletronica", "monitor", "bicicleta", "resistencia", "televisao", "apartamento", "pneumatico", "aprendizado", "frutas", "estudante", "elefantes", "aniversario", "piscina", "cachorro", "documentos", "luminaria", "escritorio", "telescopio"]
palavras_dificil = ["comunicaçcao", "responsavel", "inteligencia", "independente", "planejamento", "empreendedor", "sustentavel", "organizacao", "estrategico", "interessante", "extraordinario"]
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
    
    jogar_novamente = menu_confirmacao()
    if not jogar_novamente:
        return

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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Verifique eventos de toque
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if retangulo_sim.collidepoint(x, y):
                    return True  # Jogar novamente
                elif retangulo_nao.collidepoint(x, y):
                    return False  # Não jogar novamente

        
def main():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    
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
                elif retangulo_sair.collidepoint(x, y):
                    pygame.quit()
                    return

        tela.fill((0, 0, 0))
        retangulo_jogar, retangulo_sair = mostrar_menu_touch(tela)
        pygame.display.flip()

if __name__ == "__main__":
    main()

