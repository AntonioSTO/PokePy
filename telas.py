import pygame
pygame.init()

(width, height) = (800, 600)                         # Configs da tela
screen = pygame.display.set_mode((width, height))

##############################################

# Funções anti repetição

def img(nome):
    return pygame.image.load(nome)
def scale(nome, escala):
    return pygame.transform.scale(nome, escala)
def fonte(nome, tamanho):
    return pygame.font.Font(nome, tamanho)

tecla_passagem = {pygame.K_RETURN}  # Concerta erro de leitura na passagem das telas de seleção de pokemon

tecla_retorno = {pygame.K_ESCAPE}   # Concerta erro de leitura no retorno das telas de seleção de pokemon

selection_keys = {pygame.K_UP, pygame.K_DOWN}

enter_duplicado = False

##############################################

# Elementos TELA INICIAL

tela_inicial = scale(img(r'.\Sprites\SpritesInterface\tela_inicial.jpg'),(800,600))  # Tela de fundo inicial

main_screen_audio = 0
if main_screen_audio == 0:
    pygame.mixer.music.load(r'.\Sprites\SonsPokemon\main_screen.mp3')    # Música da tela inicial
    pygame.mixer.music.play(-1)

texto_tela_inicial = fonte(r'.\Fontes\pokemon_fire_red.ttf',40)  # Texto 'Press SPACE'
instruction = texto_tela_inicial.render('PRESS SPACE TO START', True, (0,0,0))
instructionRect = instruction.get_rect()
instructionRect.center = ((400),(450))

integrantes = fonte(r'.\Fontes\pokemon_fire_red.ttf',1)  # Integrantes
integrantes = texto_tela_inicial.render('By AntonioSt and Traba', True, (0,0,0))
integrantesRect = integrantes.get_rect()
integrantesRect.center = ((400),(200))

titulo = img(r'.\Sprites\SpritesInterface\PokePy.png')  # Sprite Titulo 'PokePy'

##############################################

# Elementos TELA AMOGUS

tela_sus = scale(img(r'.\Sprites\SpritesInterface\tela_sus.jpg'),(800,600))  # Tela de fundo easter egg

titulo_sus = img(r'.\Sprites\SpritesInterface\titulo_sus.png')  # Sprite AMOGUS

texto_tela_sus = fonte(r'.\Fontes\pokemon_fire_red.ttf',40)  # Texto 'Press ESCAPE to escape'
fuga = texto_tela_sus.render('PRESS ESCAPE TO ESCAPE', True, (250,250,250))
fugaRect = fuga.get_rect()
fugaRect.center = ((400),(450))

##############################################

# Elementos Tela Seleção 1

texto_selecao_player1 = fonte(r'.\Fontes\pokemon_fire_red.ttf',35)  # Texto 'Player 1 Select Your Pokemon'
selecao_pokemon1 = texto_selecao_player1.render('PLAYER 1 CHOOSE YOUR POKEMON', True, (250,250,250))
selecao_pokemon1Rect = selecao_pokemon1.get_rect()
selecao_pokemon1Rect.center = ((400),(50))      

##############################################

# Pokemons Selecionaveis
pokemons_selecionados = []

fonte_selecao = fonte(r'.\Fontes\pokemon_fire_red.ttf',40)  # Fonte nomes pokemon selecao

pikachu_select = fonte_selecao.render('PIKACHU', True, (255,215,0))
pikachu_selectRect = pikachu_select.get_rect()
pikachu_selectRect.center = ((400),(125))      

charmander_select = fonte_selecao.render('CHARMANDER', True, (255,140,0))
charmander_selectRect = charmander_select.get_rect()
charmander_selectRect.center = ((400),(180))      

squirtle_select = fonte_selecao.render('SQUIRTLE', True, (135,206,235))
squirtle_selectRect = squirtle_select.get_rect()
squirtle_selectRect.center = ((400),(235))      

bulbasaur_select = fonte_selecao.render('BULBASAUR', True, (0,128,0))
bulbasaur_selectRect = bulbasaur_select.get_rect()
bulbasaur_selectRect.center = ((400),(290))      

pidgey_select = fonte_selecao.render('PIDGEY', True, (255,239,213))
pidgey_selectRect = pidgey_select.get_rect()
pidgey_selectRect.center = ((400),(345))      

seta_pos = 125
selection_arrow = scale(img(r'.\Sprites\SpritesInterface\arrow.png'), (25,20))
selection_arrowRect = selection_arrow.get_rect()
selection_arrowRect.center = ((270),(125))

##############################################

# Elementos Tela Seleção 2

texto_selecao_player2 = fonte(r'.\Fontes\pokemon_fire_red.ttf',35)  # Texto 'Player 2 Select Your Pokemon'
selecao_pokemon2 = texto_selecao_player2.render('PLAYER 2 CHOOSE YOUR POKEMON', True, (250,250,250))
selecao_pokemon2Rect = selecao_pokemon2.get_rect()
selecao_pokemon2Rect.center = ((400),(50))      


