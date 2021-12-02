from application.model.entity.produtos import Produtos


lista_Produtos = []

class ProdutosDao():
    def __init__(self) -> None:
        self._lista_Produtos = lista_Produtos

    def list(self, produtos_lista):
        lista = []
        for item in produtos_lista:
            produto = Produtos
            produto.set_id(item['id'])
            produto.set_imagem(item['imagem'])
            produto.set_nome(item['nome'])
            produto.set_descricao(item['descricao'])
            produto.set_preco_ant(item['preco_ant'])
            produto.set_preco_atual(item['preco_atual'])
            lista.append(produto)
            return lista
