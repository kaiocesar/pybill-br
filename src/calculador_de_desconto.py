# -*- coding: UTF-8 -*-

class Calculador_de_descontos(object):

    def calcular(self, orcamento):

        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        if orcamento.valor > 500:
            return orcamento.valor * 0.07

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))

    print(Calculador_de_descontos().calcular(orcamento))
