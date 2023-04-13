#=====================================================================#
#                     Definicao da classe Pokemon                     #
#=====================================================================#

import random # Importacao da biblioteca para randomizar o dano dos pokemons
from pokemon_types import tipos_pokemon # Importacao da variavel que define as vantagens por tipo
from moves import * # Importacao da classe Habilidade e das habilidades registradas
import pygame

class Pokemon:
    # nome: Nome do pokemon(string)
    # tipo1: Tipo primário do pokemon(string)
    # tipo2: Tipo secundário do pokemon(string) - None por padrão
    # habilidade1: Primeira habilidade(Objeto habilidade)
    # habilidade2: Segunda habilidade(Objeto habilidade)
    # habilidade3: Terceira habilidade(Objeto habilidade)
    # habilidade4: Quarta habilidade(Objeto habilidade)
    # ataque: Valor de ataque físico do pokemon(int)
    # ataque_especial: Valor de ataque especial do pokemon(int)
    # defesa: Valor de defesa física do pokemon(int)
    # defesa_especial: Valor de defesa especial do pokemon(int)
    # hp_maximo: Vida máxima do pokemon(int)
    # sprite_frente: Imagem do pokemon de frente(local da imagem - string)
    # sprite_costas: imagem do pokemon de costas(local da imagem - string)
    # sprite_hit: Imagem do pokemon de frente quando atacado(local da imagem - string)
    # sprite_morto: imagem do pokemon de frente quando morto(local da imagem - string)
    # level: level do pokemon(string)
    # hp: vida do pokemon durante a batalha(int)
    
    def __init__(self, nome, tipo1, habilidade1, habilidade2, habilidade3, habilidade4, ataque, ataque_especial, defesa, defesa_especial, hp_maximo, sprite_frente, sprite_costas, sprite_hit, sprite_morto, level, tipo2=None):
        self.__nome = nome
        self.__tipo1 = tipo1
        self.__tipo2 = tipo2
        self.__habilidade1 = habilidade1
        self.__habilidade2 = habilidade2
        self.__habilidade3 = habilidade3
        self.__habilidade4 = habilidade4
        self.__ataque = ataque
        self.__ataque_especial = ataque_especial
        self.__defesa = defesa
        self.__defesa_especial = defesa_especial
        self.__hp_maximo = hp_maximo
        self.__sprite_frente = sprite_frente
        self.__sprite_costas = sprite_costas
        self.__sprite_hit = sprite_hit
        self.__sprite_morto = sprite_morto
        self.__level = level
        self.__hp = hp_maximo

    def reset(self):
        self.__hp = self.__hp_maximo
        self.__habilidade1.pp = self.__habilidade1.max_pp
        self.__habilidade2.pp = self.__habilidade2.max_pp
        self.__habilidade3.pp = self.__habilidade3.max_pp
        self.__habilidade4.pp = self.__habilidade4.max_pp

    def atacar(self, habilidade, pokemon_atacado): # Funcao para ataque com qualquer habilidade - altera a vida do pokemon atacado
        habilidade.pp -= 1

        acerto, critico, aplica_efeito = habilidade.uso() # Define valores booleanos para acerto, critico e aplica_efeito

        if acerto: #Condicional para impedir calculos desnecessarios em caso de erro da habilidade

            # Condicional para definir o tipo de ataque e defesa - utilizado no calculo do dano do ataque

            if habilidade.categoria == 'physical': # Caso o tipo de ataque seja fisico
                tipo_ataque = self.ataque # Define o tipo_ataque para o valor do ataque normal do pokemon atacante
                tipo_defesa = pokemon_atacado.defesa # Define o tipo_defesa para o valor da defesa normal do pokemon atacado
            else:
                tipo_ataque = self.ataque_especial # Define o tipo_ataque para o valor do ataque especial do pokemon atacante
                tipo_defesa = pokemon_atacado.defesa_especial # Define o tipo_defesa para o valor da defesa especial do pokemon atacado

            # Adquirindo valores para os modificadores de dano - Critico, random e tipo

            if critico: # Caso o acerto seja critico - Define o multiplicador de dano por critico para 2 (Dobro do dano de um ataque comum)
                mult_critico = 2
            else: # Caso o acerto nao seja critico - Define o multiplicador de dano por critico para 1 (Dano normal do ataque)
                mult_critico = 1
            
            rng = random.uniform(0.1, 1) # Retorna um numero aleatorio entre 0,1 e 1
            
            if pokemon_atacado.tipo2 == None: # Caso o pokemon atacado nao possua um segundo tipo - Calcula o multiplicador de dano por tipo considerando apenas o tipo 1 do pokemon atacado
                mult_tipo = tipos_pokemon[habilidade.tipo][pokemon_atacado.tipo1]
            else: # Caso o pokemon atacado possua um segundo tipo - Calcula o multiplicador de dano por tipo considerando os dois tipos do pokemon atacado
                mult_tipo = tipos_pokemon[habilidade.tipo][pokemon_atacado.tipo1] * tipos_pokemon[habilidade.tipo][pokemon_atacado.tipo2]

            # Calculo do dano causado

            dano = (((2*self.level/5 + 2) * habilidade.poder * (tipo_ataque/tipo_defesa)) / 50) * mult_critico * rng * mult_tipo

            dano = round(dano) # Arredondamento do dano para um numero inteiro

            # Alteracao da vida do pokemon atacado

            if dano < pokemon_atacado.hp: # Processamento para garantir que o pokemon nao atinja menos de 0 de vida
                pokemon_atacado.hp -= dano
            else:
                dano = pokemon_atacado.hp
                pokemon_atacado.hp = 0
            
            return dano, mult_tipo, acerto # Retorna o dano causado, o multiplicador de tipo e o booleano para acerto
        
        else: # Caso a habilidade nao acerte
            dano = 0 # Habilidade nao causa dano
            mult_tipo = None # Multiplicador por tipo pode ser desconsiderado

            return dano, mult_tipo, acerto # Retorna o dano causado, o multiplicador de tipo e o booleano para acerto
            
    
    @property
    def nome(self): #Getter para o nome do pokemon
        return self.__nome

    @property
    def tipo1(self): #Getter para o tipo1 do pokemon
        return self.__tipo1
    
    @property
    def tipo2(self): #Getter para o tipo2 do pokemon
        return self.__tipo2
    
    @property
    def habilidade1(self): #Getter para a skill1 do pokemon
        return self.__habilidade1

    @property
    def habilidade2(self): #Getter para a skill2 do pokemon
        return self.__habilidade2

    @property
    def habilidade3(self): #Getter para a skill3 do pokemon
        return self.__habilidade3

    @property
    def habilidade4(self): #Getter para a skill4 do pokemon
        return self.__habilidade4
    
    @property
    def ataque(self): #Getter para o ataque do pokemon
        return self.__ataque
    
    @property
    def ataque_especial(self): #Getter para o ataque especial do pokemon
        return self.__ataque_especial

    @property
    def defesa(self): #Getter para a defesa do pokemon
        return self.__defesa
    
    @property
    def defesa_especial(self): #Getter para a defesa_especial do pokemon
        return self.__defesa_especial

    @property
    def hp_maximo(self): #Getter para o hp maximo do pokemon
        return self.__hp_maximo
    
    @property
    def sprite_frente(self): #Getter para a sprite de frente do pokemon
        return self.__sprite_frente
    
    @property
    def sprite_costas(self): #Getter para a sprite de costas do pokemon
        return self.__sprite_costas
    
    @property
    def sprite_hit(self): #Getter para a sprite de frente quando atacado do pokemon
        return self.__sprite_hit
    
    @property
    def sprite_morto(self): #Getter para a sprite de frente quando morto do pokemon
        return self.__sprite_morto

    @property
    def level(self): #Getter para o level do pokemon
        return self.__level

    @property
    def hp(self): #Getter para o hp atual pokemon
        return self.__hp

    @hp.setter
    def hp(self, dano): # Setter para o hp atual do pokemon
        self.__hp = dano

#=====================================================================#
#                  Definicao das sprites dos Pokemons                 #
#=====================================================================#

# Funcoes anti repeticao #

def img(diretorio):
    return pygame.image.load(diretorio)

def scale(imagem, resolucao):
    return pygame.transform.scale(imagem, resolucao)

#### Definicao das sprites ####

bulbassauro_back = scale(img(r'.\Sprites\SpritesPokemon\Costas\1.png'), (213, 213))
bulbassauro_front = scale(img(r'.\Sprites\SpritesPokemon\Frente\1.png'), (213, 213))
bulbassauro_hit = scale(img(r'.\Sprites\SpritesPokemon\Hit\1.png'), (213, 213))
bulbassauro_morto = scale(img(r'.\Sprites\SpritesPokemon\Morto\1.png'), (213, 213))

charmander_back = scale(img(r'.\Sprites\SpritesPokemon\Costas\4.png'), (213, 213))
charmander_front = scale(img(r'.\Sprites\SpritesPokemon\Frente\4.png'), (213, 213))
charmander_hit = scale(img(r'.\Sprites\SpritesPokemon\Hit\4.png'), (213, 213))
charmander_morto = scale(img(r'.\Sprites\SpritesPokemon\Morto\4.png'), (213, 213))

squirtle_back = scale(img(r'.\Sprites\SpritesPokemon\Costas\7.png'), (213, 213))
squirtle_front = scale(img(r'.\Sprites\SpritesPokemon\Frente\7.png'), (213, 213))
squirtle_hit = scale(img(r'.\Sprites\SpritesPokemon\Hit\7.png'), (213, 213))
squirtle_morto = scale(img(r'.\Sprites\SpritesPokemon\Morto\7.png'), (213, 213))

pidgey_back = scale(img(r'.\Sprites\SpritesPokemon\Costas\16.png'), (213, 213))
pidgey_front = scale(img(r'.\Sprites\SpritesPokemon\Frente\16.png'), (213, 213))
pidgey_hit = scale(img(r'.\Sprites\SpritesPokemon\Hit\16.png'), (213, 213))
pidgey_morto = scale(img(r'.\Sprites\SpritesPokemon\Morto\16.png'), (213, 213))

pikachu_back = scale(img(r'.\Sprites\SpritesPokemon\Costas\25.png'), (213, 213))
pikachu_front = scale(img(r'.\Sprites\SpritesPokemon\Frente\25.png'), (213, 213))
pikachu_hit = scale(img(r'.\Sprites\SpritesPokemon\Hit\25.png'), (213, 213))
pikachu_morto = scale(img(r'.\Sprites\SpritesPokemon\Morto\25.png'), (213, 213))

#======================================================================#
#                        Definicao dos pokemons                        #
#======================================================================#

# A separação dos pokemons pro player 1 e pro player 2 e necessaria para evitar
# que ambos sejam afetados por uma acao, ja que a mudanca sera feita diretamente nos objetos

# Pokemons do player 1 #

bulbassauro = Pokemon('BULBASAUR', 'grass', tackle, vine_whip, razor_leaf, seed_bomb, 49, 65, 49, 65, 45, bulbassauro_front, bulbassauro_back, bulbassauro_hit, bulbassauro_morto, 20, 'poison')
charmander = Pokemon('CHARMANDER', 'fire', scratch, ember, dragon_breath, fire_fang, 52, 60, 43, 50, 39, charmander_front, charmander_back, charmander_hit, charmander_morto, 20)
squirtle = Pokemon('SQUIRTLE', 'water', tackle, bite, water_gun, water_pulse, 48, 50, 65, 64, 44, squirtle_front, squirtle_back, squirtle_hit, squirtle_morto, 20)
pidgey = Pokemon('PIDGEY', 'normal', tackle, gust, quick_attack, wing_attack, 45, 35, 40, 35, 40, pidgey_front, pidgey_back, pidgey_hit, pidgey_morto, 20, 'flying')
pikachu = Pokemon('PIKACHU', 'electric', feint, spark, quick_attack, thunder_shock, 55, 50, 40, 50, 35, pikachu_front, pikachu_back, pikachu_hit, pikachu_morto, 20)

# Pokemons do player 2 #

bulbassauro2 = Pokemon('BULBASAUR', 'grass', tackle, vine_whip, razor_leaf, seed_bomb, 49, 65, 49, 65, 45, bulbassauro_front, bulbassauro_back, bulbassauro_hit, bulbassauro_morto, 20, 'poison')
charmander2 = Pokemon('CHARMANDER', 'fire', scratch, ember, dragon_breath, fire_fang, 52, 60, 43, 50, 39, charmander_front, charmander_back, charmander_hit, charmander_morto, 20)
squirtle2 = Pokemon('SQUIRTLE', 'water', tackle, bite, water_gun, water_pulse, 48, 50, 65, 64, 44, squirtle_front, squirtle_back, squirtle_hit, squirtle_morto, 20)
pidgey2 = Pokemon('PIDGEY', 'normal', tackle, gust, quick_attack, wing_attack, 45, 35, 40, 35, 40, pidgey_front, pidgey_back, pidgey_hit, pidgey_morto, 20, 'flying')
pikachu2 = Pokemon('PIKACHU', 'electric', feint, spark, quick_attack, thunder_shock, 55, 50, 40, 50, 35, pikachu_front, pikachu_back, pikachu_hit, pikachu_morto, 20)