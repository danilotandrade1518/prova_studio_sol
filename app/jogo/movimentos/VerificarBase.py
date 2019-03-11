class VerificarBase:
    # Classe responsável por conter o funcionamento base do jogo.
    # Essa classe deve ser extendida por classes concretas que sobrescrevem os métodos
    # _primeiro_movimento(self, posicao_linha_atual, posicao_letra_atual) e
    # _segundo_movimento(self, posicao_linha_atual, posicao_letra_atual).

    def __init__(self, palavra):
        self.palavra = palavra

    def verificar(self, ocorrencias_primeira_letra):
        # Método responsável por encontrar as palavras informadas pelo usuário na matriz incial do jogo.
        # À partir das ocorrências da primeira letra da palavra, o programa percorre as próximas letras respeitando
        # os movimentos contidos nos métodos _primeiro_movimento e _segundo_movimento, até que palavra tenha sido
        # percorrida por completo ou que a letra verificada não coincida.

        # Remoção da primeira letra da palavra, uma vez que o ponto de partida do método são as ocorrências da primeira
        # letra que foram recebidas como parâmetro do método.
        palavra = self.palavra[1:len(self.palavra)]

        qtd_palavra = 0
        ocorrencias_palavra = []

        for ocorrencia in ocorrencias_primeira_letra:
            matching = True
            posicao_linha_atual = ocorrencia[0]
            posicao_letra_atual = ocorrencia[1]
            index = 0

            ocorrencias_atuais = []
            while matching:

                if len(palavra) == index:
                    # Palavra encontrada por completo na matriz
                    qtd_palavra += 1
                    ocorrencias_palavra.append([ocorrencia[0], ocorrencia[1]])
                    ocorrencias_palavra.extend(ocorrencias_atuais)
                    break

                letra_atual = palavra[index]

                if index % 2 == 0:
                    # Primeiro movimento na ordem de execução da classe concreta que extendeu essa classe.
                    posicao_nova_letra = self._primeiro_movimento(posicao_linha_atual, posicao_letra_atual)
                else:
                    # Segundo movimento na ordem de execução da classe concreta que extendeu essa classe.
                    posicao_nova_letra = self._segundo_movimento(posicao_linha_atual, posicao_letra_atual)

                if posicao_nova_letra == None:
                    # Chegou ao fim da matriz.
                    ocorrencias_atuais.clear()
                    break

                if letra_atual.lower() == posicao_nova_letra["nova_letra"]:
                    # Letra atual da matriz coincide com a letra informada pelo usuário.
                    # Execução continua.
                    posicao_linha_atual = posicao_nova_letra["novo_index_linha"]
                    posicao_letra_atual = posicao_nova_letra["novo_index_letra"]
                    ocorrencias_atuais.append([posicao_linha_atual, posicao_letra_atual])
                    index += 1
                else:
                    # Letra atual da matriz não coincide com a letra informada pelo usuário.
                    # Execução pára e vai para próxima ocorrência da primeira letra da palavra recebida.
                    ocorrencias_atuais.clear()
                    matching = False

        return {"qtd_encontrada": qtd_palavra, "ocorrencias": ocorrencias_palavra}

    def _primeiro_movimento(self, posicao_linha_atual, posicao_letra_atual):
        # Método que deve ser sobrescrito pela classe concreta que extender essa classe.
        # O método deve executar o primeiro movimento na ordem de execução do zig-zag.
        pass

    def _segundo_movimento(self, posicao_linha_atual, posicao_letra_atual):
        # Método que deve ser sobrescrito pela classe concreta que extender essa classe.
        # O método deve executar o segundo movimento na ordem de execução do zig-zag.
        pass
