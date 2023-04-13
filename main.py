#tentativa de tela 
import pygame
from sys import exit 
from telas import * 
from battle_engine import batalha
from pokemon import * # Importa a classe Pokemon, os pokemons declarados juntamente com suas sprites e as funcoes img e scale
pygame.init()

pygame.key.set_repeat() # Usado para evitar repeticao de teclado no KEYDOWN

##############################################

# Funções para as imagens e sprites

def img(nome):
    return pygame.image.load(nome)


def scale(nome, escala):
    return pygame.transform.scale(nome, escala)

##############################################

# Config da janela
size = (800, 600)
_colour = (0, 0, 0)
screen = pygame.display.set_mode(size)
screen.fill(_colour)
pygame.display.set_caption('PokePy')
pygame.display.flip()
tela = 1

##############################################

#Timer
clock = pygame.time.Clock()         

##############################################

#Musicas
music = 0


##############################################

#Efeitos
switch = pygame.mixer.Sound(r'.\Sprites\SonsPokemon\switch_screen.mp3')  # Troca de telas

amogus = pygame.mixer.Sound(r'.\Sprites\SonsPokemon\amogus.mp3')    # Som easter egg

##############################################

# GameLoop
running = True
while running:

    clock.tick(30)  # Limita o fps do jogo

    for event in pygame.event.get():

##############################################
# Elementos da tela inicial   
  
        if tela == 1:
            if music == 0:
                pygame.mixer.music.load(r'.\Sprites\SonsPokemon\main_screen.mp3')    # Música da tela inicial
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play(-1)
                music = 1

            pokemons_selecionados = []
            screen.blit(tela_inicial ,(0,0))  # Display da Tela Inicial
            screen.blit(instruction,instructionRect)
            screen.blit(integrantes,integrantesRect)
            screen.blit(titulo, (230,50))
            pygame.display.update()

            if event.type == pygame.KEYDOWN:                # Mudança de tela 1 -> 2
                if event.key == pygame.K_SPACE:
                    tela += 1
                    switch.play()

##############################################
# Elementos tela sus

                keys = pygame.key.get_pressed()             
                if keys[pygame.K_s] and keys[pygame.K_u]:   # Teclas Easter Egg
                    screen.blit(tela_sus ,(0,0))
                    screen.blit(titulo_sus, (230,50))       # Mudança de tela 1 -> Easter Egg
                    screen.blit(fuga, fugaRect)
                    pygame.display.update()
                    tela -= 1

                    amogus.play()                           # AMOGUS
                    amogus_audio = 0
                    if amogus_audio == 0:
                        pygame.mixer.music.load(r'.\Sprites\SonsPokemon\amogus_music.wav')   
                        pygame.time.delay(1000)
                        pygame.mixer.music.play(-1)         # Musica Tela Easter Egg

        if tela == 0 and event.type == pygame.KEYDOWN:      # VOLTAR PRA TELA INICIAL 
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.music.load(r'.\Sprites\SonsPokemon\main_screen.mp3')    # Música da tela inicial
                pygame.mixer.music.play(-1)
                screen.blit(tela_inicial ,(0,0))
                screen.blit(instruction,instructionRect)
                screen.blit(integrantes,integrantesRect)
                screen.blit(titulo, (230,50))
                pygame.display.update()
                tela += 1

##############################################
# Elementos da tela de Seleção 1

        if tela == 2:
            enter_duplicado = False
            pygame.draw.rect(screen, (0,0,0), ((0,0),(800,600)))                # Display de todos componentes da primeira tela de seleção
            screen.blit(selecao_pokemon1, selecao_pokemon1Rect)
            pygame.draw.rect(screen, (250,250,250), ((225,70),(350,455)),0)
            pygame.draw.rect(screen, (0,0,0), ((230,75),(340,445)),0)
            screen.blit(pikachu_select, pikachu_selectRect)
            screen.blit(charmander_select, charmander_selectRect)
            screen.blit(squirtle_select, squirtle_selectRect)
            screen.blit(bulbasaur_select, bulbasaur_selectRect)
            screen.blit(pidgey_select, pidgey_selectRect)
            screen.blit(selection_arrow, selection_arrowRect)

            pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    if seta_pos == 125:
                        pokemons_selecionados.append(pikachu)
                        tela += 1
                        switch.play()

                    elif seta_pos == 180:
                        pokemons_selecionados.append(charmander)
                        tela += 1
                        switch.play()
                        
                    elif seta_pos == 235:
                        pokemons_selecionados.append(squirtle)
                        tela += 1
                        switch.play()

                    elif seta_pos == 290:
                        pokemons_selecionados.append(bulbassauro)
                        tela += 1
                        switch.play()

                    elif seta_pos == 345:
                        pokemons_selecionados.append(pidgey)
                        tela += 1
                        switch.play()

##############################################

# Seta seleção pokemon - posições e coordenadas

                if seta_pos == 125:
                    if event.key == pygame.K_UP: 
                        seta_pos = 345
                        selection_arrowRect.center = ((270),(345))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 180
                        selection_arrowRect.center = ((270),(180))

                elif seta_pos == 180:
                    if event.key == pygame.K_UP: 
                        seta_pos = 125
                        selection_arrowRect.center = ((270),(125))

                    elif event.key == pygame.K_DOWN: 
                        seta_pos = 235
                        selection_arrowRect.center = ((270),(235))

                elif seta_pos == 235:
                    if event.key == pygame.K_UP:
                        seta_pos = 180
                        selection_arrowRect.center = ((270),(180))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 290
                        selection_arrowRect.center = ((270),(290))
                
                elif seta_pos == 290:
                    if event.key == pygame.K_UP:
                        seta_pos = 235
                        selection_arrowRect.center = ((270),(235))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 345
                        selection_arrowRect.center = ((270),(345))

                elif seta_pos == 345:
                    if event.key == pygame.K_UP:
                        seta_pos = 290
                        selection_arrowRect.center = ((270),(290))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 125
                        selection_arrowRect.center = ((270),(125))
            
##############################################
        
# Retorna para a tela inicial

                if event.key in tecla_retorno:
                    screen.blit(tela_inicial ,(0,0))
                    pygame.display.update()
                    switch.play()
                    tela -= 1

##############################################

# Elementos da tela de Seleção 2

        if tela == 3:
            pygame.draw.rect(screen, (0,0,0), ((0,0),(800,600)))
            screen.blit(selecao_pokemon2, selecao_pokemon2Rect)
            pygame.draw.rect(screen, (250,250,250), ((225,70),(350,455)),0)
            pygame.draw.rect(screen, (0,0,0), ((230,75),(340,445)),0)
            screen.blit(pikachu_select, pikachu_selectRect)
            screen.blit(charmander_select, charmander_selectRect)
            screen.blit(squirtle_select, squirtle_selectRect)
            screen.blit(bulbasaur_select, bulbasaur_selectRect)
            screen.blit(pidgey_select, pidgey_selectRect)
            screen.blit(selection_arrow, selection_arrowRect)
            pygame.display.update()

##############################################

# Solução pra dupla seleção com o comando RETURN

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if enter_duplicado == True:  

##############################################

# Armazenamento do pokemon selecionado pelo player 2

                        if seta_pos == 125:
                            pokemons_selecionados.append(pikachu2)

                        elif seta_pos == 180:
                            pokemons_selecionados.append(charmander2)
                        
                        elif seta_pos == 235:
                            pokemons_selecionados.append(squirtle2)

                        elif seta_pos == 290:
                            pokemons_selecionados.append(bulbassauro2)

                        elif seta_pos == 345:
                            pokemons_selecionados.append(pidgey2)

                        tela, music = batalha(pokemons_selecionados[0],pokemons_selecionados[1], screen)
    
                    enter_duplicado = True
##############################################

# Seta seleção pokemon - posições e coordenadas

                if seta_pos == 125:                                     # Pos Pikachu
                    if event.key == pygame.K_UP: 
                        seta_pos = 345
                        selection_arrowRect.center = ((270),(345))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 180
                        selection_arrowRect.center = ((270),(180))

                elif seta_pos == 180:                                   # Pos Charmander
                    if event.key == pygame.K_UP: 
                        seta_pos = 125
                        selection_arrowRect.center = ((270),(125))

                    elif event.key == pygame.K_DOWN: 
                        seta_pos = 235
                        selection_arrowRect.center = ((270),(235))

                elif seta_pos == 235:                                   # Pos Squirtle
                    if event.key == pygame.K_UP:
                        seta_pos = 180
                        selection_arrowRect.center = ((270),(180))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 290
                        selection_arrowRect.center = ((270),(290))
                
                elif seta_pos == 290:                                   # Pos bulbasaur
                    if event.key == pygame.K_UP:
                        seta_pos = 235
                        selection_arrowRect.center = ((270),(235))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 345
                        selection_arrowRect.center = ((270),(345))

                elif seta_pos == 345:                                   # Pos Pidgey
                    if event.key == pygame.K_UP:
                        seta_pos = 290
                        selection_arrowRect.center = ((270),(290))

                    elif event.key == pygame.K_DOWN:
                        seta_pos = 125
                        selection_arrowRect.center = ((270),(125))
            
##############################################

# Retorna para a seleção 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.update()
                switch.play()
                tela -= 1
                pokemons_selecionados = []

##############################################

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()