class EventoFuncionario():
    def __init__(self, evento, funcionario, convidado, funcionario_bebe, convidado_bebe):
        self.__evento = evento
        self.__funcionario = funcionario
        self.__convidado = convidado
        self.__funcionario_bebe = funcionario_bebe
        self.__convidado_bebe = convidado_bebe
    
    @property
    def evento(self):
        return self.__evento
    
    @evento.setter
    def evento(self, evento):
        self.__evento = evento

    @property
    def funcionario(self):
        return self.__funcionario
    
    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario
    
    @property
    def convidado(self):
        return self.__convidado
    
    @convidado.setter
    def convidado(self, convidado):
        self.__convidado = convidado
    
    @property
    def funcionario_bebe(self):
        return self.__funcionario_bebe
    
    @funcionario_bebe.setter
    def funcionario_bebe(self, funcionario_bebe):
        self.__funcionario_bebe = funcionario_bebe
    
    @property
    def convidado_bebe(self):
        return self.__convidado_bebe
    
    @convidado_bebe.setter
    def convidado_bebe(self, convidado_bebe):
        self.__convidado_bebe = convidado_bebe