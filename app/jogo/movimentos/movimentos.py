class Movimentos:
    # Classe responsável por conter os movimentos únicos possíveis no jogo.

    def __init__(self, matriz_inicial):
        self.matriz_inicial = matriz_inicial

    def mover_para_direita(self, index_linha_atual, index_letra_atual):
        # Método responsável por executar o movimento à direita.

        try:
            index_letra_a_direita = index_letra_atual + 1
            letra_a_direita = self.matriz_inicial[index_linha_atual][index_letra_a_direita]

            return {'nova_letra': letra_a_direita.lower(), 'novo_index_letra': index_letra_a_direita, 'novo_index_linha': index_linha_atual}
        except IndexError:
            # Chegou ao fim da matriz.
            return None

    def mover_para_baixo(self, index_linha_atual, index_letra_atual):
        # Método responsável por executar o movimento abaixo.

        try:
            index_linha_abaixo = index_linha_atual + 1
            letra_abaixo = self.matriz_inicial[index_linha_abaixo][index_letra_atual]

            return {'nova_letra': letra_abaixo.lower(), 'novo_index_letra': index_letra_atual, 'novo_index_linha': index_linha_abaixo}
        except IndexError:
            # Chegou ao fim da matriz.
            return None

    def mover_para_esquerda(self, index_linha_atual, index_letra_atual):
        # Método responsável por executar o movimento à esquerda.

        try:
            index_letra_a_esquerda = index_letra_atual - 1
            letra_a_esquerda = self.matriz_inicial[index_linha_atual][index_letra_a_esquerda]

            return {'nova_letra': letra_a_esquerda.lower(), 'novo_index_letra': index_letra_a_esquerda, 'novo_index_linha': index_linha_atual}
        except IndexError:
            # Chegou ao fim da matriz.
            return None

    def mover_para_cima(self, index_linha_atual, index_letra_atual):
        # Método responsável por executar o movimento acima.

        try:
            index_linha_acima = index_linha_atual - 1
            letra_acima = self.matriz_inicial[index_linha_acima][index_letra_atual]

            return {'nova_letra': letra_acima.lower(), 'novo_index_letra': index_letra_atual, 'novo_index_linha': index_linha_acima}
        except IndexError:
            # Chegou ao fim da matriz.
            return None
