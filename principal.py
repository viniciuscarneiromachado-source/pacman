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
        pygame.display.set_caption(constantes.TITULO_JOGO)
        #criando o relógio do jogo
        self.relogio = pygame.time.Clock()
        self.jogando = True
        self.fonte = pygame.font.SysFont('Arial', 24)
        self carregar_arquivos()
        def novo_jogo(self):
            #instanciar as imagens
            self.todas_as_imagens = pygame.sprite.Group()
            self.rodar()   
        def rodar(self)
            #loop principal do jogo
            self.jogando = True
            while self.jogando:
                self.relogio.tick(constantes.FPS)
                self.eventos()
                self.atualizar_sprites()
                self.desenhar_sprites()

            def eventos(self):
                #loop de eventos de jogo
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        if self.jogando:
                            self.jogando = False
                            self.esta_rodando = False