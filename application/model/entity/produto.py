class Produto:

    def __init__(self, name, preco) -> None:
        self.name = name
        self.preco = preco

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_preco(self):
        return self.preco 

    def set_preco(self, preco):
        self.preco = preco