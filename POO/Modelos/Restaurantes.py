from Modelos.avaliacao import Avaliacao

class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria, cnpj, contato):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._cnpj = cnpj
        self._contato = contato
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f" {self._nome.ljust} | {self._categoria.ljust} | {self._cnpj} | {self._contato}"

    @classmethod
    def listagem_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(26)} | {"Categoria".ljust(25)} | {"CNPJ".ljust(25)} | {"Contato".ljust(25)} | {"Avaliações".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f" {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._cnpj.ljust(25)} | {restaurante._contato.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

            
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐' 
    
    def alterar_status(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return print("O restaurante ainda não possui nenhuma avaliação")
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) 
        quantidade_notas = len(self._avaliacao) 
        media = round(soma_notas / quantidade_notas, 1)
        return media          

