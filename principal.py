import pygame
import sprites
import constantes

class Game:
    def __init__(self):
        #criando o jogo
        #inicializa o pygame
        pygame.init()
        #inicializa o mixer do pygame para tocar sons
        pygame.mixer.init()
        #ciando a tela do jogo
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        #exibindo o título do jogo
        pygamre.display.set_caption(constantes.TITULO_JOGO)
        #criando o relógio do jogo
        self.relogio = pygame.time.Clock()
        self.jogando = True
        self.fonte = pygame.font.SysFont('Arial', 24)
        self carregar_arquivos()