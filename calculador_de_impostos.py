from impostos import calcula_icms, calcula_iss


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        if imposto == 'ISS':
            return calcula_iss(orcamento)
        elif imposto == 'ICMS':
            return calcula_icms(orcamento)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    print(calculador.realiza_calculo(orcamento, 'ISS'))
    print(calculador.realiza_calculo(orcamento, 'ICMS'))
