class Evento():
    def __init__(self, nome, total_arrecadado, total_gasto, total_gasto_comida, total_gasto_bebida):
        self.__nome = nome
        self.__total_arrecadado = total_arrecadado
        self.__total_gasto = total_gasto
        self.__total_gasto_comida = total_gasto_comida
        self.__total_gasto_bebida = total_gasto_bebida
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def total_arrecadado(self):
        return self.__total_arrecadado
    
    @total_arrecadado.setter
    def total_arrecadado(self, total_arrecadado):
        self.__total_arrecadado = total_arrecadado
    
    @property
    def total_gasto(self):
        return self.__total_gasto
    
    @total_gasto.setter
    def total_gasto(self, total_gasto):
        self.__total_gasto = total_gasto
    
    @property
    def total_gasto_comida(self):
        return self.__total_gasto_comida
    
    @total_gasto_comida.setter
    def total_gasto_comida(self, total_gasto_comida):
        self.__total_gasto_comida = total_gasto_comida
    
    @property
    def total_gasto_bebida(self):
        return self.__total_gasto_bebida
    
    @total_gasto_bebida.setter
    def total_gasto_bebida(self, total_gasto_bebida):
        self.__total_gasto_bebida = total_gasto_bebida
