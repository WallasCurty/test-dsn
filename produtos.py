class Produtos():
    def __init__(self, id: int,imagem: str, nome: str, descricao: str, preco_ant: float, preco_atual:float) -> None:
        self._id = id
        self._imagem = imagem
        self._nome = nome
        self._descricao = descricao
        self._preco_ant = preco_ant
        self._preco_atual = preco_atual

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    def get_imagem(self):
        return self._imagem
    
    def set_imagem(self, imagem):
        self._imagem = imagem

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_preco_ant(self):
        return self._preco_ant

    def set_preco_ant(self, preco_ant):
        self._preco_ant = preco_ant

    def get_preco_atual(self):
        return self._preco_atual

    def set_preco_atual(self, preco_atual):
        self._preco_atual = preco_atual
