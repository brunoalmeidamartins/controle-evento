class Convidado():
    def __init__(self, nome, funcionario):
        self.__nome = nome
        self.__funcionario = funcionario
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def funcionario(self):
        return self.__funcionario
    
    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario