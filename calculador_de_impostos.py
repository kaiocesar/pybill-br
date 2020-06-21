class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        if imposto == 'ISS':
            return orcamento.valor * 0.1
        elif imposto == 'ICMS':
            return orcamento.valor * 0.06


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    print(calculador.realiza_calculo(orcamento, 'ISS'))
    print(calculador.realiza_calculo(orcamento, 'ICMS'))
