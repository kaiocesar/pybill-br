from impostos import ISS, ICMS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        return imposto.calcula(orcamento)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    print('Valor ISS {}'.format(
        calculador.realiza_calculo(orcamento, ISS())))
    print('Valor ICMSS {}'.format(
        calculador.realiza_calculo(orcamento, ICMS())))
