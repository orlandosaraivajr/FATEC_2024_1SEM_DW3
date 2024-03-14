class PrimeiraClasse:
    pass

objeto1 = PrimeiraClasse()
objeto2 = PrimeiraClasse()

objeto1.teste = "teste"
objeto1.__dict__

class SegundaClasse:
    def metodo1(self):
        print("Método 1")
    
    def metodo2(self, nome):
        print("Método 2" + nome)

objeto3 = SegundaClasse()

class CarrinhoCompra:
    def __init__(self):
        print('Vamos iniciar as compras. Gaste muito !')
        self.__lista = []
    
    def adicionar(self, item):
        print('Você adicionou ao carrinho')
        self.__lista.append(item)

    def listar(self):
        print('Lista de produtos')
        return self.lista
    
    def adicionar_varios_produtos(self, *args):
        for item in args:
            self.__lista.append(item)


cliente1 = CarrinhoCompra()
cliente2 = CarrinhoCompra()
cliente3 = CarrinhoCompra()

class CarrinhoCompraInternacional(CarrinhoCompra):
    pass

clienteInternacional1 = CarrinhoCompraInternacional()