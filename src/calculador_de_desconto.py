# -*- coding: UTF-8 -*-
from descontos import DescontoPorCincoItens, DescontoPorMaisDe500Reais, SemDesconto


class Calculador_de_descontos(object):

    def calcular(self, orcamento):
        desconto = DescontoPorCincoItens(
            DescontoPorMaisDe500Reais(
                SemDesconto()
            )).calcula(orcamento)
        return desconto


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))

    print(Calculador_de_descontos().calcular(orcamento))
