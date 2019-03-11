import copy

from jogo.util import print_matriz


class Resultado:
    # Classe responsável por imprimir o resultado da busca para o usuário.

    def __init__(self, matriz_inicial, ocorrencias):
        self.matriz_inicial = matriz_inicial
        self.ocorrencias = ocorrencias

    def print_resultado(self):
        # Método responsável por imprimir no terminal as mensagens com os resultados para o usuário.

        palavras_encontradas = self.ocorrencias["palavras_encontradas"]
        palavras_nao_encontradas = self.ocorrencias["palavras_nao_encontradas"]
        quantidade = self.ocorrencias["qtd_encontrada"]

        if quantidade > 0:
            # Imprime as palavras encontradas, palavras não encontradas(caso exista) e a matriz com as palavras encontradas destacadas.

            print("\n{0} ocorrência(s) de '{1}'.".format(quantidade, ", ".join(palavras_encontradas)))

            if len(palavras_nao_encontradas) > 0:
                print("Nenhuma ocorrência encontrada para '{0}'\n".format(", ".join(palavras_nao_encontradas)))

            self._print_matriz_destacada()
        else:
            # Imprime as palavras não encontradas.

            print("\nNenhuma ocorrência encontrada para '{0}'".format(", ".join(palavras_nao_encontradas)))

    def _print_matriz_destacada(self):
        # Método responsável por copiar a matriz inicial do programa, destacar as palavras encontradas e imprimir a matriz destacada.

        matriz_destacada = copy.deepcopy(self.matriz_inicial)
        for index_linha, linha in enumerate(matriz_destacada):
            for index_letra, letra in enumerate(linha):
                if [index_linha, index_letra] not in self.ocorrencias["ocorrencias"]:
                    matriz_destacada[index_linha][index_letra] = "*"

        print_matriz(matriz_destacada)
