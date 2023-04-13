import pygame

class Battle_selection:
    # Classe para os retangulos de selecao utilizados na batalha
    # width: Largura do retangulo (int - pixels)
    # height: Altura do retangulo (int - pixels)
    # start_x: Posicao inicial do retangulo no eixo x (int - pixels)
    # start_y: Posicao inicial do retangulo no eixo y (int - pixels)
    # line_dist: Distancia entre uma linha e outra da selecao (int - pixels)
    # column_dist: Distancia entre uma coluna e outra da selecao (int - pixels)
    # x_max: valor maximo para a posicao de x (int - pixels)
    # x_min: valor minimo para a posicao de x (int - pixels)
    # y_max: valor maximo para a posicao de y (int - pixels)
    # y_min: valor minimo para a posicao de y (int - pixels)
    # new_width: Largura do retangulo em casos que o tamanho dele deva mudar quando mexido

    # As posicoes estao relacionadas com a ponta superior esquerda do retangulo

    def __init__(self, width, height, start_x, start_y, line_dist, column_dist, x_max, x_min, y_max, y_min):
        self.__width = width
        self.__height = height
        self.__pos_x = start_x # Variavel para indicar a posicao atual do retangulo no eixo x
        self.__pos_y = start_y # Variavel para indicar a posicao atual do retangulo no eixo y
        self.__line_dist = line_dist
        self.__column_dist = column_dist
        self.__x_max = x_max
        self.__x_min = x_min
        self.__y_max = y_max
        self.__y_min = y_min

        self.__x = 0 # Variavel para armazenar o offset do retangulo de selecao para utilizar no cover
        self.__y = 0 # Variavel para armazenar o offset do retangulo de selecao para utilizar no cover
        self.__start_pos = (start_x, start_y) # Tupla da posicao inicial do retangulo
        self.__pos = self.__start_pos # Tupla da posicao atual do retangulo
        self.__rect = pygame.Rect(start_x, start_y, width, height) # Representa o retangulo usado para selecao
        self.__cover_rect = pygame.Rect(start_x, start_y, width, height) # Retangulo usado para "apagar" um retangulo quando o mesmo mudar de posicao

    def draw_selector(self, surface): # Desenha o retangulo seletor e o triangulo responsavel por oculta-lo
        pygame.draw.rect(surface, (255, 255, 255), self.__cover_rect, 5) # Desenha um retangulo similar ao usado para selecionar, porem na mesma cor do background
        pygame.draw.rect(surface, (255, 0, 0), self.__rect, 5) # Desenha o retangulo usado para selecao

    def update_rect_pos(self,surface, x, y): # Atualiza a posicao do retangulo - x e y representam o offset da
        pygame.Rect.move_ip(self.__rect, x, y)
        self.draw_selector(surface)

    def update_cover_pos(self,surface, x, y): # Atualiza a posicao do retangulo - x e y representam o offset da
        pygame.Rect.move_ip(self.__cover_rect, x, y)
        self.draw_selector(surface)

    def moveUP(self, surface): # Move o retangulo para cima (Caso ja esteja no topo, move para y_min)
        self.update_cover_pos(surface, self.__x, self.__y)

        if self.__pos_y != self.__y_min: # Condicional para avaliar se o retangulo se encontra no maximo
            self.__pos_y = self.__y_min
            self.__y = -self.__line_dist
        else:
            self.__pos_y += self.__line_dist
            self.__y = self.__line_dist

        self.__pos = (self.__pos_x, self.__pos_y)
        self.__x = 0 # Reset do valor de variacao ja que o retangulo nao se moveu nesse eixo
        self.update_rect_pos(surface, self.__x, self.__y)

    def moveDOWN(self, surface): # Move o retangulo para baixo (Caso ja esteja em baixo, move para y_max)
        self.update_cover_pos(surface, self.__x, self.__y)

        if self.__pos_y != self.__y_max: # Condicional para avaliar se o retangulo se encontra no maximo
            self.__pos_y = self.__y_max
            self.__y = self.__line_dist
        else:
            self.__pos_y -= self.__line_dist
            self.__y = -self.__line_dist
        
        self.__pos = (self.__pos_x, self.__pos_y)
        self.__x = 0 # Reset do valor de variacao ja que o retangulo nao se moveu nesse eixo
        self.update_rect_pos(surface, self.__x, self.__y)
    
    def moveRIGHT(self, surface): # Move o retangulo para direita (Caso ja esteja na direita, move para x_min)
        self.update_cover_pos(surface, self.__x, self.__y)

        if self.__pos_x != self.__x_max: # Condicional para avaliar se o retangulo se encontra no maximo
            self.__pos_x = self.__x_max
            self.__x = self.__column_dist
        else:
            self.__pos_x -= self.__column_dist
            self.__x = -self.__column_dist
        
        self.__pos = (self.__pos_x, self.__pos_y)
        self.__y = 0 # Reset do valor de variacao ja que o retangulo nao se moveu nesse eixo
        self.update_rect_pos(surface, self.__x, self.__y)

    def moveLEFT(self, surface): # Move o retangulo para esquerda (Caso ja esteja na esquerda, move para x_max)
        self.update_cover_pos(surface, self.__x, self.__y)

        if self.__pos_x != self.__x_min: # Condicional para avaliar se o retangulo se encontra no maximo
            self.__pos_x = self.__x_min
            self.__x = -self.__column_dist
        else:
            self.__pos_x += self.__column_dist
            self.__x = self.__column_dist
        
        self.__pos = (self.__pos_x, self.__pos_y)
        self.__y = 0 # Reset do valor de variacao ja que o retangulo nao se moveu nesse eixo
        self.update_rect_pos(surface, self.__x, self.__y)

    @property
    def posx(self): # Getter para a posicao x do retangulo
        return self.__pos_x

    @property
    def posy(self): # Getter para a posicao y do retangulo
        return self.__pos_y

    @property
    def x_min(self): # Getter para a posicao x minimo do retangulo
        return self.__x_min

    @property
    def x_max(self): # Getter para a posicao x maximo do retangulo
        return self.__x_max

    @property
    def y_min(self): # Getter para a posicao y minimo do retangulo
        return self.__y_min

    @property
    def y_max(self): # Getter para a posicao y maximo do retangulo
        return self.__y_max

#width, height, start_x, start_y, line_dist, column_dist, x_max, x_min, y_max, y_min)

action_selector = Battle_selection(135, 40, 490, 483, 52, 150, 640, 490, 535, 483)
skill_selector = Battle_selection(230, 35, 25, 485, 40, 230, 255, 25, 525, 485)