class Jogador(object):
#construtor da classe Jogador, __ torna-os privados

    def __init__(self, id=0, nome="", dataNasc="", apelido="", bibliotecaJogos=[] ):

        self.__id= id
        self.__nome = nome
        self.__dataNasc= dataNasc
        self.__apelido= apelido
        self.__bibliotecaJogos = bibliotecaJogos

 #Property da o Get no valor do ID ja que o mesmo é privado
    @property
    def id(self):
        return self.__id
 # Id.Setter seta um novo valor a variavel id ja que o mesmo é privado
    @id.setter
    def id(self, novoValor):
        self.__id= novoValor

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome
    
    @property
    def dataNasc(self):
        return self.__dataNasc

    @dataNasc.setter
    def dataNasc(self, novaData):
        self.__dataNasc= novaData

    @property
    def apelido(self):
        return self.__apelido

    @apelido.setter
    def apelido(self, novoApelido):
        self.__apelido =novoApelido

    @property
    def bibliotecaJogos(self):
        return self.__bibliotecaJogos
    
    @bibliotecaJogos.setter
    def bibliotecaJogos(self, novaBibliotecaJogos):
        self.__bibliotecaJogos = novaBibliotecaJogos

    def toJson(self):
        return {
            "id"        : self.__id,
            "nome"      : self.__nome,
            "dataNasc"  : self.__dataNasc,
            "apelido"   : self.__apelido,
            "jogos"     : [jogo.toJson() for jogo in self.__bibliotecaJogos]
        }
    
    