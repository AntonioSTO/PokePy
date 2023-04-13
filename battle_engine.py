from pokemon_types import tipos_pokemon # Importa a lista de vantagens por tipo
from pokemon import * # Importa a classe Pokemon, os pokemons declarados juntamente com suas sprites e as funcoes img e scale
from battle_selection import *
import pygame
import time
from sys import exit

pygame.init()

# Inicializando os efeitos sonoros de batalha - Deram problema quando inicializados depois provavelmente pq sao usados em funcao#
menu_sound = pygame.mixer.Sound(r'.\Sprites\SonsPokemon\menu_sound.mp3')
pygame.mixer.Sound.set_volume(menu_sound, .1)

def fonte(diretorio, tamanho):
    return pygame.font.Font(diretorio, tamanho)

def add_data(screen, text, coords): # Adiciona texto referente aos dados dos pokemons - Vida e nivel
    texto = fonte_dados_batalha.render(text, False, (62, 62, 62))
    screen.blit(texto, coords)

def add_battle_text(screen, text, line=1):
    # Adiciona texto referente as acoes durante a batalha - Recebe o texto(string) e a linha em que deve ser colocado o texto
    y = 450 + (line * 25) + (15 * line)
    texto = fonte_acoes_batalha.render(text, False, (255, 255, 255))
    screen.blit(texto, (40, y))

def add_skill_text(screen, text, line=1, column=1): # Adiciona texto referente ao nome das habilidades com base na linha e coluna desejados
    x = 40 + 220 * (column - 1)
    y = 450 + (line * 25) + (15 * line)
    texto = fonte_acoes_batalha.render(text, False, (0, 0, 0))
    screen.blit(texto, (x, y))

def clear_battle_text(screen): # Reposiciona a barra de texto e as opcoes de batalha por cima do texto anterior
    screen.blit(text_bar, (0, 450))

def skill_data(screen, habilidade): # Exibe as caracteristicas da habilidade selecionada pelo player
    pp_atual = f'{habilidade.pp}'
    pp_total = f'{habilidade.max_pp}'
    tipo_skill = f'{habilidade.tipo}'

    pp_atual = fonte_acoes_batalha.render(pp_atual, False, (0, 0, 0))
    pp_total = fonte_acoes_batalha.render(pp_total, False, (0, 0, 0))
    tipo_skill = fonte_acoes_batalha.render(tipo_skill, False, (0, 0, 0))

    screen.blit(cover_pp_bar, (533, 450)) # Responsavel por ocultar os dados anteriores
    screen.blit(pp_atual, (670, 485))
    screen.blit(pp_total, (740, 485))
    screen.blit(tipo_skill, (640, 540))
    pygame.display.update()

def width_barra_vida(screen, barra_sem_vida_atacado, width_barra_vida_atacado, dano_causado, pokemon_atacado): # Define a largura da barra sem vida do pokemon, "diminuindo" a vida do pokemon
    # Nao e necessario considerar se o dano ultrapassara a vida do pokemon ja que isso foi considerado na funcao atacar do objeto pokemon

    for i in range(dano_causado):
        width_barra_vida_atacado += (120 / pokemon_atacado.hp_maximo) # Aumenta a largura da barra_sem_vida em x partes para x de dano
        barra_sem_vida_atacado = scale(img(r'.\Sprites\SpritesInterface\barra_sem_vida.png'), (round(width_barra_vida_atacado), 8)) # Escala a barra_sem_vida para a nova largura
        screen.blit(barra_sem_vida_atacado, (151, 92)) 
        pygame.display.update() # Atualiza a tela
        time.sleep(0.05) # Pausa o codigo para que a barra de vida diminua de forma "animada"

    if pokemon_atacado.hp == 0: # Garante que caso a vida do pokemon chegue a zero a barra_sem_vida ocupara todo o espaco da vida
        width_barra_vida_atacado = 120
        barra_sem_vida_atacado = scale(barra_sem_vida_atacado, (round(width_barra_vida_atacado), 8)) # Escala a barra_sem_vida para a nova largura
        screen.blit(barra_sem_vida_atacado, (151, 92)) 
        pygame.display.update() # Atualiza a tela
    
    return barra_sem_vida_atacado, width_barra_vida_atacado # Retorna a barra de vida atual e largura atual da barra_sem_vida

def atacar_pokemon(screen, pokemon_atacante, habilidade_usada, pokemon_atacado): # Exibe a realização do ataque e retorna o dano causado
    dano_causado, mult_tipo, acerto = pokemon_atacante.atacar(habilidade_usada, pokemon_atacado) 
    clear_battle_text(screen) # Limpa a area de texto para batalha
    add_battle_text(screen, f'{pokemon_atacante.nome} usou') # Adiciona texto na linha 1 da area
    add_battle_text(screen, f'{habilidade_usada.nome}', 2) # Adiciona texto na linha 2 da area
    screen.blit(pokemon_atacado.sprite_hit, (490, 40))
    pygame.display.update() # Atualiza a tela
    time.sleep(.2) # Pausa o codigo para que aparente uma animacao de hit
    screen.blit(pokemon_atacado.sprite_frente, (490, 40))
    pygame.display.update()
    time.sleep(.8) # Pausa o codigo para que o texto nao seja sobreposto instantaneamente

    return dano_causado, mult_tipo, acerto # Retorna o dano causado pelo ataque e o multiplicador por tipo

def imprime_efetividade(screen, habilidade, mult_tipo, acerto, pokemon_atacado): # Funcao para desenhar o texto referente a efetividade do ataque realizado - Nao possui retorno
    if acerto: # Caso a habilidade tenha acertado    
        # Condicionais para definir o texto a ser impresso com base na efetivade da habilidade
        if mult_tipo == 0: 
            text1 = f'{habilidade.nome} não'
            text2 = f'afetou {pokemon_atacado.nome}!'
        
        elif mult_tipo == 0.5:
            text1 = f'{habilidade.nome} foi'
            text2 = f'pouco efetiva!'

        # Quando a habilidade causar dano normal nada sera impresso

        elif mult_tipo == 2:
            text1 = f'{habilidade.nome} foi'
            text2 = f'efetiva!'

        elif mult_tipo == 4:
            text1 = f'{habilidade.nome} foi'
            text2 = f'super efetiva!!'
        
    else:
        text1 = f'{habilidade.nome} não'
        text2 = f'acertou {pokemon_atacado.nome}!'

    if mult_tipo != 1: # Condicional para impedir a execucao do comando para o dano normal do ataque
        clear_battle_text(screen) # Limpa a area de impressao de textos durante a batalha
        add_battle_text(screen, text1) # Adiciona o texto 1 na linha 1 
        add_battle_text(screen, text2, 2) # Adiciona o texto 2 na linha 2
        pygame.display.update() # Atualiza a tela
        time.sleep(1) # Pausa o codigo para que o texto nao saia imediatamente da tela

def causar_dano(screen, habilidade, dano_causado, acerto): # Funcao para desenhar o texto referente ao dano do ataque realizado - Nao possui retorno
    if acerto: # O texto so precisa ser impresso caso a habilidade acerte, ja que ja filtramos o acerto na funcao imprime_efetividade
        text1 = f'{habilidade.nome} causou'
        text2 = f'{dano_causado} de dano'
        clear_battle_text(screen) # Limpa a area de impressao de textos durante a batalha
        add_battle_text(screen, text1) # Adiciona o texto 1 na linha 1 
        add_battle_text(screen, text2, 2) # Adiciona o texto 2 na linha 2
        pygame.display.update() # Atualiza a tela
        time.sleep(1) # Pausa o codigo para que o texto nao saia imediatamente da tela

def run(screen, pokemon_atacante): # Funcao responsavel por exibir a tela de confirmacao de Run e confirma-lo ou nao
    clear_battle_text(screen)
    add_battle_text(screen, f'Tem certeza que deseja fugir?')
    add_battle_text(screen, f'Pressione <Enter> para confirmar', 2)
    pygame.display.update()

    while True: # Loop para adquirir inputs
        for e in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                clear_battle_text(screen)
                add_battle_text(screen, f'{pokemon_atacante.nome} fugiu!!')
                add_battle_text(screen, f'SEBO NAS CANELA!!!!', 2)
                pygame.display.update()
                time.sleep(1.5)
                return True # Retorna True caso Run tenha sido confirmado

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return False # Retorna False caso Run tenha sido cancelado

def seletor_de_acao(screen): # Funcao responsavel por selecionar a acao que o pokemon realizara | Fight ou Run
    while True: # Loop responsavel por impedir a passagem infinita de rounds e executar a selecao de acao 
        for e in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_UP]:
                action_selector.moveUP(screen)
                menu_sound.play()
                pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                action_selector.moveDOWN(screen)
                menu_sound.play()
                pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                action_selector.moveLEFT(screen)
                menu_sound.play()
                pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                action_selector.moveRIGHT(screen)
                menu_sound.play()
                pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                menu_sound.play()
                if action_selector.posx == action_selector.x_min and action_selector.posy == action_selector.y_min: # Verifica se Fight foi selecionado
                    battle_stage = 1
                    return battle_stage
                elif action_selector.posx == action_selector.x_max and action_selector.posy == action_selector.y_max: # Verifica se Run foi selecionado
                    battle_stage = 4
                    return battle_stage
       
            if e.type == pygame.QUIT:
                pygame.quit()

def batalha(pokemon1, pokemon2, screen):

    battle_stage = 0 # Define o estado da batalha
    # battle_stage = 0 | Selecao de acao
    # battle_stage = 1 | Selecao de ataque
    # battle_stage = 2 | Apresentacao da efetividade do ataque do dano do ataque e atualizacao da barra de vida
    # battle_stage = 3 | Tela de vitoria
    # battle_stage = 4 | Confirmacao do run

    # Inicializando a musica de batalha - Desativado durante os testes #
    pygame.mixer.music.load(r'.\Sprites\SonsPokemon\batalha.wav')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1) # Mantem a musica em loop ate o final da batalha

    # Definindo o primeiro pokemon a atacar - Ordem invertida ja que existe a troca no loop
    pokemon_atacante = pokemon2
    pokemon_atacado = pokemon1

    # Carregando as barras que representam o dano em cada pokemon
    # Definida dentro da funcao para arrumar problemas de declaracao
    barra_sem_vida_atacado = scale(img(r'.\Sprites\SpritesInterface\barra_sem_vida.png'), (0, 8)) # Max width = 120
    barra_sem_vida_atacante = scale(img(r'.\Sprites\SpritesInterface\barra_sem_vida.png'), (0, 8)) # Max width = 120

    width_barra_vida_atacado = 0
    width_barra_vida_atacante = 0
    

    while pokemon_atacado.hp != 0: # Loop responsavel por realizar o reset a cada round

        pokemon_atacante, pokemon_atacado = pokemon_atacado, pokemon_atacante # Altera a posicao dos pokemons a cada round
        barra_sem_vida_atacado, barra_sem_vida_atacante = barra_sem_vida_atacante, barra_sem_vida_atacado # Altera as barras de vida seguindo a troca de lados
        width_barra_vida_atacado, width_barra_vida_atacante = width_barra_vida_atacante, width_barra_vida_atacado # Alterna as larguras das barras de vida conforme a troca de rounds

        # Carregando a tela de batalha
        screen.blit(bg_batalha, (0, 0))
        screen.blit(pokemon_atacante.sprite_costas, (70, 237))
        screen.blit(pokemon_atacado.sprite_frente, (490, 40))
        screen.blit(barra_atacado, (50, 50))
        screen.blit(barra_atacante, (500, 300))
        screen.blit(text_bar, (0, 450))
        screen.blit(fgt_options, (450, 450))
        screen.blit(barra_sem_vida_atacado, (151, 92))
        screen.blit(barra_sem_vida_atacante, (620, 349))

        # Adiciona os dados dos pokemons na tela - Atualizado a cada troca de lados
        add_data(screen, f'{pokemon_atacado.nome}', (65, 60))
        add_data(screen, f'{pokemon_atacado.level}', (243, 60))
        add_data(screen, f'{pokemon_atacante.nome}', (532, 318))
        add_data(screen, f'{pokemon_atacante.level}', (712, 318))
        add_data(screen, f'{pokemon_atacante.hp}/{pokemon_atacante.hp_maximo}', (650, 360))

        # Adiciona textos usados durante a batalha - Atualizado a cada acao realizada
        add_battle_text(screen, f'What should')
        add_battle_text(screen, f'{pokemon_atacante.nome} do?', 2)

        action_selector.draw_selector(screen)

        pygame.display.update() # Atualiza o display exibindo a tela de batalha

        battle_stage = seletor_de_acao(screen) # Define o estado da batalha (1 ou 5)

        acaba_round = False # Variavel para administrar a mudanca de rodadas

        while not acaba_round:
            
            if battle_stage == 0: # Recarrega a tela de escolha de acoes
                screen.blit(text_bar, (0, 450))
                screen.blit(fgt_options, (450, 450))

                add_battle_text(screen, f'What should')
                add_battle_text(screen, f'{pokemon_atacante.nome} do?', 2)

                action_selector.draw_selector(screen)

                pygame.display.update() # Atualiza o display exibindo a tela de batalha

                battle_stage = seletor_de_acao(screen) # Define o estado da batalha (1 ou 5)

            if battle_stage == 1: # Exibe as escolhas de habilidade
                screen.blit(pp_bar, (0, 450))
                skill_selector.draw_selector(screen)
                add_skill_text(screen, f'{pokemon_atacante.habilidade1.nome}')
                add_skill_text(screen, f'{pokemon_atacante.habilidade2.nome}', 2)
                add_skill_text(screen, f'{pokemon_atacante.habilidade3.nome}', 1, 2)
                add_skill_text(screen, f'{pokemon_atacante.habilidade4.nome}', 2, 2)
                pygame.display.update()

            while battle_stage == 1: # Enquanto o player estiver escolhendo a habilidade    
                for e in pygame.event.get():
                    if not pygame.key.get_pressed()[pygame.K_RETURN] and not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        if skill_selector.posx == skill_selector.x_min and skill_selector.posy == skill_selector.y_min: # Verifica se habilidade1 foi selecionada
                            skill_data(screen, pokemon_atacante.habilidade1)
                        elif skill_selector.posx == skill_selector.x_min and skill_selector.posy == skill_selector.y_max: # Verifica se habilidade2 foi selecionada
                            skill_data(screen, pokemon_atacante.habilidade2)
                        elif skill_selector.posx == skill_selector.x_max and skill_selector.posy == skill_selector.y_min: # Verifica se habilidade3 foi selecionada
                            skill_data(screen, pokemon_atacante.habilidade3)
                        else: # Caso nenhuma outra tenha sido selecionada, seleciona a habilidade 4
                            skill_data(screen, pokemon_atacante.habilidade4)

                        if pygame.key.get_pressed()[pygame.K_UP]: # Quando a seta e apertada, move o seletor na direcao apertada
                            skill_selector.moveUP(screen)
                            menu_sound.play()
                            pygame.display.flip()
                        if pygame.key.get_pressed()[pygame.K_DOWN]: # Quando a seta e apertada, move o seletor na direcao apertada
                            skill_selector.moveDOWN(screen)
                            menu_sound.play()                        
                            pygame.display.flip()
                        if pygame.key.get_pressed()[pygame.K_LEFT]: # Quando a seta e apertada, move o seletor na direcao apertada
                            skill_selector.moveLEFT(screen)
                            menu_sound.play()
                            pygame.display.flip()
                        if pygame.key.get_pressed()[pygame.K_RIGHT]: # Quando a seta e apertada, move o seletor na direcao apertada
                            skill_selector.moveRIGHT(screen)
                            menu_sound.play()                        
                            pygame.display.flip()

                    if pygame.key.get_pressed()[pygame.K_RETURN]: # Quando Enter(RETURN) e apertado, seleciona o ataque e o realiza
                        uso_habilidade = False # Booleano para garantir que a habilidade nao sera usada quando estiver sem pp

                        if skill_selector.posx == skill_selector.x_min and skill_selector.posy == skill_selector.y_min: # Verifica se habilidade1 foi selecionada
                            if pokemon_atacante.habilidade1.pp != 0:
                                habilidade_usada = pokemon_atacante.habilidade1
                                uso_habilidade = True
                        elif skill_selector.posx == skill_selector.x_min and skill_selector.posy == skill_selector.y_max: # Verifica se habilidade2 foi selecionada
                            if pokemon_atacante.habilidade2.pp != 0:
                                habilidade_usada = pokemon_atacante.habilidade2
                                uso_habilidade = True
                        elif skill_selector.posx == skill_selector.x_max and skill_selector.posy == skill_selector.y_min: # Verifica se habilidade3 foi selecionada
                            if pokemon_atacante.habilidade3.pp != 0:
                                habilidade_usada = pokemon_atacante.habilidade3
                                uso_habilidade = True
                        else: # Caso nenhuma outra tenha sido selecionada, seleciona a habilidade 4
                            if pokemon_atacante.habilidade4.pp != 0:
                                habilidade_usada = pokemon_atacante.habilidade4
                                uso_habilidade = True
                            
                        if uso_habilidade: # Se a habilidade pode ser usada
                            menu_sound.play() # Toca o efeito sonoro de selecao

                            dano_causado, multiplicador, acerto = atacar_pokemon(screen, pokemon_atacante, habilidade_usada, pokemon_atacado) # Calcula o dano causado o multiplicador de tipo e o booleano para acerto
                            battle_stage = 2 # Atualiza o valor de battle_stage levando assim para a tela de efetividade do ataque
                    
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        battle_stage = 0 # Reseta a tela de escolha de acoes

                    if e.type == pygame.QUIT:
                        pygame.quit()

                    pygame.event.clear() # Limpa o cache de acoes do pygame, facilitando a execucao dos comandos

            while battle_stage == 2: # Caso o jogo esteja no estado de apresentar a efetividade e dano do ataque e atualizar a barra de vida
                imprime_efetividade(screen, habilidade_usada, multiplicador, acerto, pokemon_atacado)   
                causar_dano(screen, habilidade_usada, dano_causado, acerto)
                barra_sem_vida_atacado, width_barra_vida_atacado = width_barra_vida(screen, barra_sem_vida_atacado, width_barra_vida_atacado, dano_causado, pokemon_atacado)
                time.sleep(.5) # Pausa o codigo, garantindo que a animacao da barra_de_vida sera apresentada completamente
                
                if pokemon_atacado.hp != 0: # Caso o pokemon ainda esteja vivo
                    battle_stage = 0 # Garante que o jogo nao causara dano infinito ao pokemon, saindo do loop do battle_stage = 2
                    acaba_round = True # Acaba o round, saindo do loop do ataque
                else: # Caso o pokemon esteja morto
                    screen.blit(pokemon_atacado.sprite_morto, (490, 40)) # Atualiza a imagem do pokemon para seu estado morto
                    pygame.display.update()
                    battle_stage = 3 # Altera battle_stage para 3 (tela de vitória)
                
                for e in pygame.event.get(): # Garante que o jogo pode ser fechado a qualquer momento
                    if e.type == pygame.QUIT:
                        pygame.quit()

            
            if battle_stage == 3: 
            # Carrega e inicia a musica de vitoria
                pygame.mixer.music.load(r'.\Sprites\SonsPokemon\vitoria.wav')
                pygame.mixer.music.set_volume(0.15)
                pygame.mixer.music.play(-1)
        
            # Exibe o nome do pokemon vencedor no centro da area de texto
                clear_battle_text(screen)
                add_battle_text(screen, f'{pokemon_atacante.nome} ganhou!!', 1.5)
                pygame.display.update()
                time.sleep(3) # Garante que o texto de vitória fique tempo suficiente na tela

                clear_battle_text(screen)
                add_battle_text(screen, 'Pressione <Enter> para jogar novamente.', 1.5)
                pygame.display.update()
            
            while battle_stage == 3:
                for e in pygame.event.get():
                    if pygame.key.get_pressed()[pygame.K_RETURN]: # Inicia outra batalha desde a selecao
                        pokemon_atacante.reset()
                        pokemon_atacado.reset()
                        return 1, 0 # Valor para definir qual a tela que sera exibida e resetar a musica

                    if e.type == pygame.QUIT:
                        pygame.quit()

            if battle_stage == 4:
                correu = run(screen, pokemon_atacante)

                if correu:
                    pokemon_atacante.reset()
                    pokemon_atacado.reset()
                    return 1, 0 # Valor para definir qual a tela que sera exibida e resetar a musica
                else:
                    battle_stage = 0 # Altera battle_state para a selecao de acoes

# Carregando as imagens utilizadas para formar a tela de batalha
bg_batalha = scale(img(r'.\Sprites\SpritesInterface\FundoPokemon.png'), (800, 450))
text_bar = scale(img(r'.\Sprites\SpritesInterface\text_bar.png'), (800, 150))
barra_atacado = scale(img(r'.\Sprites\SpritesInterface\barra_1.png'), (253, 75))
barra_atacante = scale(img(r'.\Sprites\SpritesInterface\barra_2.png'), (260, 100))
fgt_options = scale(img(r'.\Sprites\SpritesInterface\fgt_options.png'), (350, 150))
pp_bar = scale(img(r'.\Sprites\SpritesInterface\pp_bar.png'), (800, 150))
cover_pp_bar = scale(img(r'.\Sprites\SpritesInterface\cover_pp_bar.png'), (267, 150))

fonte_acoes_batalha = fonte(r'.\Fontes\joystix_monospace.ttf', 20)
fonte_dados_batalha = fonte(r'.\Fontes\joystix_monospace.ttf', 18)

if __name__ == '__main__':
    size = (800, 600)
    _colour = (0, 0, 0)
    screen = pygame.display.set_mode(size)
    screen.fill(_colour)
    pygame.display.set_caption('PokePy')
    pygame.display.flip()
    tela = 1
    clock = pygame.time.Clock()

    batalha(squirtle, pidgey2, screen)

barra_sem_vida_atacado = scale(img(r'.\Sprites\SpritesInterface\barra_sem_vida.png'), (0, 8))