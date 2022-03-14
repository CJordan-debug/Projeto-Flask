class Jogo(object):
    #construtor da classe Jogo, __ torna-os privados

    def __init__(self, idjogo=0, nomeJogo="", conquistas=[], HorasJogadas=""):
        self.__idjogo= idjogo
        self.__nomeJogo = nomeJogo
        self.__conquistas= conquistas
        self.__HorasJogadas= HorasJogadas

    @property
    def id(self):
        return self.__idjogo
    
    @id.setter
    def id(self,novoIdjogo):
        self.__idjogo = novoIdjogo

    @property
    def nomeJogo(self):
        return self.__nomeJogo
    @nomeJogo.setter
    
    def nome(self,novoNomeJogo):
        self.__nomejogo = novoNomeJogo
    
    @property
    def conquistas(self):
        return self.__conquistas
    
    @conquistas.setter
    def conquistas(self, novaConquista):
        self.__conquistas = novaConquista

    @property
    def HorasJogadas(self):
        return self.__HorasJogadas
    
    @HorasJogadas.setter
    def HorasJogadas(self, novasHorasJogadas):
        self.__HorasJogadas = novasHorasJogadas


    def toJson(self):
        return {
            "id": self.__idjogo,
            "nome": self.__nomejogo,
            "conquistas": [conquista.toJson() for conquista in self.__conquistas],
            "horasjogadas": self.__HorasJogadas
        }