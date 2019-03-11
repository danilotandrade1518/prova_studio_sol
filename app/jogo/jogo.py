from jogo.movimentos.verificar_abaixo_direita import VerificarAbaixoDireita
from jogo.movimentos.verificar_abaixo_esquerda import VerificarAbaixoEsquerda
from jogo.movimentos.verificar_acima_direita import VerificarAcimaDireita
from jogo.movimentos.verificar_acima_esquerda import VerificarAcimaEsquerda
from jogo.movimentos.verificar_direita_abaixo import VerificarDireitaAbaixo
from jogo.movimentos.verificar_direita_acima import VerificarDireitaAcima
from jogo.movimentos.verificar_esquerda_abaixo import VerificarEsquerdaAbaixo
from jogo.movimentos.verificar_esquerda_acima import VerificarEsquerdaAcima


class Jogo:
    # Classe responsável por controlar o funcionamento do jogo.

    def __init__(self, matriz_inicial, palavras):
        self.matriz_inicial = matriz_inicial
        self.palavras = palavras

    def jogar(self):
        # Método responsável por executar todos os movimentos possíveis para cada palavra recebida.
        # Após isso é retornado um dicionário contendo as palavras encontradas, palavras não encontradas,
        # quantidade de palavras encontradas e as posições de todas as letras das palavras encontradas.

        ocorrencias = []
        palavras_encontradas = []
        palavras_nao_encontradas = []

        for palavra in self.palavras:
            if len(palavra) == 0:
                continue

            ocorrencias_primeira_letra = self._get_ocorrencias_primeira_letra(palavra)

            ocorrencias_palavra_atual = self._executar_movimentos(ocorrencias_primeira_letra, palavra)
            ocorrencias.extend(ocorrencias_palavra_atual)

            if len([ocorrencia for ocorrencia in ocorrencias_palavra_atual if ocorrencia["qtd_encontrada"] > 0]) > 0:
                palavras_encontradas.append(palavra)
            else:
                palavras_nao_encontradas.append(palavra)

        qtd_total = 0
        ocorrencias_total = []
        for ocorrencia in ocorrencias:
            qtd_total += ocorrencia["qtd_encontrada"]
            ocorrencias_total.extend(ocorrencia["ocorrencias"])

        return {
            "palavras_encontradas": palavras_encontradas,
            "palavras_nao_encontradas": palavras_nao_encontradas,
            "qtd_encontrada": qtd_total,
            "ocorrencias": ocorrencias_total
        }

    def _get_ocorrencias_primeira_letra(self, palavra):
        # Método responsável por encontrar e retornar todas as ocorrências da primeira letra da palavra recebida na matriz inicial do jogo.

        ocorrencias_primeira_letra = []

        for index_linha, linha in enumerate(self.matriz_inicial):
            for index_letra, letra in enumerate(linha):

                if letra.lower() == palavra[0].lower():
                    ocorrencias_primeira_letra.append((index_linha, index_letra))
        return ocorrencias_primeira_letra


    def _executar_movimentos(self, ocorrencias_primeira_letra, palavra):
        # Método responsável por executar os movimentos para a palavra recebida e retornar as ocorrências encontradas.

        ocorrencias_palavra_atual = []

        verificarDireitaAbaixo = VerificarDireitaAbaixo(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarDireitaAbaixo.verificar(ocorrencias_primeira_letra))

        verificarDireitaAcima = VerificarDireitaAcima(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarDireitaAcima.verificar(ocorrencias_primeira_letra))

        verificarEsquerdaAbaixo = VerificarEsquerdaAbaixo(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarEsquerdaAbaixo.verificar(ocorrencias_primeira_letra))

        verificarEsquerdaAcima = VerificarEsquerdaAcima(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarEsquerdaAcima.verificar(ocorrencias_primeira_letra))

        verificarAbaixoDireita = VerificarAbaixoDireita(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarAbaixoDireita.verificar(ocorrencias_primeira_letra))

        verificarAbaixoEsquerda = VerificarAbaixoEsquerda(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarAbaixoEsquerda.verificar(ocorrencias_primeira_letra))

        verificarAcimaDireita = VerificarAcimaDireita(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarAcimaDireita.verificar(ocorrencias_primeira_letra))

        verificarAcimaEsquerda = VerificarAcimaEsquerda(self.matriz_inicial, palavra)
        ocorrencias_palavra_atual.append(verificarAcimaEsquerda.verificar(ocorrencias_primeira_letra))

        return ocorrencias_palavra_atual