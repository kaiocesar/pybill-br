from impostos import calcula_icms, calcula_iss


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        return imposto(orcamento)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    print('Valor ISS {}'.format(
        calculador.realiza_calculo(orcamento, calcula_iss)))
    print('Valor ICMSS {}'.format(
        calculador.realiza_calculo(orcamento, calcula_icms)))
