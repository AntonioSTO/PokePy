#======================================================================#
#                    Definicao da classe Habilidade                    #
#======================================================================#

import random #Importacao da biblioteca para randomizar ataques e chances especiais
import pygame

class Habilidade:
    # sound_effect: diretorio do efeito sonoro da habilidade
    # nome: nome da habilidade(string)
    # categoria: Categoria da habilidade(string) - physical ou special
    # tipo: Tipo da habilidade(string)
    # poder: Valor para calculo do dano da habilidade(int)
    # precisao: Chance de acerto da habilidade(float)
    # chance_critico: Chance de acerto critico(float)
    # efeito: Possivel efeito aplicado pela habilidade(string) - None por padrão
    # chance_efeito: Chance de acerto da habilidade(float)
    # pp: Quantidade de usos da habilidade por batalha(int)
    
    def __init__(self, sound_effect, nome, categoria, tipo, poder, precisao, chance_critico, pp, chance_efeito, efeito=None):
        self.__sound_effect = sound_effect
        self.__nome = nome
        self.__categoria = categoria
        self.__tipo = tipo
        self.__poder = poder
        self.__precisao = precisao
        self.__chance_critico = chance_critico
        self.__efeito = efeito
        self.__chance_efeito = chance_efeito
        self.__max_pp = pp
        self.__pp = pp

    def acerto(self): # Funcao que calcula acerto ou erro da habilidade. Retorna um booleano
        if random.random() <= self.__precisao: # Gera um número aleatório entre 0 e 1 e compara com a chance de acerto da habilidade
            return True
        else:
            return False
    
    def critico(self): # Funcao que calcula critico ou nao da habilidade. Retorna um booleano 
        if random.random() <= self.__chance_critico: # Gera um número aleatório entre 0 e 1 e compara com a chance de critico da habilidade
            return True
        else:
            return False
    
    def aplica_efeito(self): # Funcao que calcula a aplicacao ou nao de efeito da habilidade. Retorna um booleano 
        if random.random() <= self.__chance_efeito: # Gera um número aleatório entre 0 e 1 e compara com a chance de aplicacao de efeito da habilidade
            return True
        else:
            return False
    
    def uso(self): # Funcao responsável por contabilizar o uso da habilidade. Retorna booleanos para acerto, critico e aplica_efeito
        # Executa o efeito sonoro
        sound_effect = pygame.mixer.Sound(self.__sound_effect)
        sound_effect.play()

        return self.acerto(), self.critico(), self.aplica_efeito()

    @property
    def nome(self): #Getter para o nome da habilidade
        return self.__nome

    @property
    def categoria(self): #Getter para a categoria da habilidade
       return self.__categoria
    
    @property
    def tipo(self): #Getter para o tipo da habilidade
        return self.__tipo

    @property
    def poder(self): #Getter para o poder da habilidade
        return self.__poder

    @property
    def efeito(self): #Getter para o efeito da habilidade
        return self.__efeito

    @property   
    def max_pp(self): #Getter para o pp da habilidade
        return self.__max_pp

    @property
    def pp(self): #Getter para o pp da habilidade
        return self.__pp

    @pp.setter
    def pp(self, valor): # Setter para o pp da habilidade
        self.__pp = valor

#======================================================================#
#                     Definicao dos efeitos sonoros                    #
#======================================================================#

normal_se = r'.\Sprites\SonsPokemon\Tackle.wav'
grass_se = r'.\Sprites\SonsPokemon\Razor_Leaf.wav'    
thunder_se = r'.\Sprites\SonsPokemon\Thunder_Shock.wav'
quick_se = r'.\Sprites\SonsPokemon\Quick_Attack.wav'
bubble_se = r'.\Sprites\SonsPokemon\Bubble.wav'
water_se = r'.\Sprites\SonsPokemon\Hydro_Pump.wav'
flame_se = r'.\Sprites\SonsPokemon\Flamethrower.wav'
ember_se = r'.\Sprites\SonsPokemon\Ember.wav'
bite_se = r'.\Sprites\SonsPokemon\Bite.wav'

#======================================================================#
#                       Definicao das habilidades                      #
#======================================================================#

# Estrutura do objeto --> (nome, categoria, tipo, poder, precisao, critico, pp, chance_efeito, efeito)

tackle = Habilidade(normal_se, 'TACKLE', 'physical', 'normal', 40, 1, .04, 35, 0)
vine_whip = Habilidade(grass_se, 'VINE WHIP', 'special', 'grass', 35, .95, .04, 10, 0)
razor_leaf = Habilidade(grass_se, 'RAZOR LEAF', 'special', 'grass', 55, .9, .125, 25, 0)
seed_bomb = Habilidade(grass_se, 'SEED BOMB', 'physical', 'grass', 80, 1, .04, 15, 0)
scratch = Habilidade(normal_se, 'SCRATCH', 'physical', 'normal', 40, 1, .04, 35, 0)
ember = Habilidade(ember_se, 'EMBER', 'special', 'fire', 40, .95, .04, 25, .1, 'burn')
dragon_breath = Habilidade(flame_se, 'DRAGON BREATH', 'special', 'dragon', 60, .95, .04, 20, .3, 'paralyze')
fire_fang = Habilidade(ember_se, 'FIRE FANG', 'physical', 'fire', 65, .9, .04, 15, .1, 'burn')
water_gun = Habilidade(water_se, 'WATER GUN', 'special', 'water', 40, .95, .04, 25, 0)
bite = Habilidade(bite_se, 'BITE', 'physical', 'dark', 60, 1, .04, 25, 0)
water_pulse = Habilidade(water_se, 'WATER PULSE', 'special', 'water', 60, .95, .04, 20, .2, 'confusion')
quick_attack = Habilidade(quick_se, 'QUICK ATTACK', 'physical', 'normal', 40, 1, .08, 30, 0)
gust = Habilidade(quick_se, 'GUST', 'special', 'flying', 40, .95, .04, 35, 0)
wing_attack = Habilidade(quick_se, 'WING ATTACK', 'physical', 'flying', 60, 1, .04, 35, 0)
thunder_shock = Habilidade(thunder_se, 'THUNDER SHOCK', 'special', 'electric', 40, .95, .04, 30, .1, 'paralyze')
feint = Habilidade(normal_se, 'FEINT', 'physical', 'normal', 30, 1, .1, 10, 0)
spark = Habilidade(thunder_se, 'SPARK', 'physical', 'electric', 65, 1, .04, 20, .3, 'paralyze')