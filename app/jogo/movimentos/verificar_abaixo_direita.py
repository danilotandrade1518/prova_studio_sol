from jogo.movimentos.VerificarBase import VerificarBase
from jogo.movimentos.movimentos import Movimentos


class VerificarAbaixoDireita(VerificarBase):
    # Classe concreta que extende de VerificarBase.
    # Responsável por executar o movimento abaixo e direita no jogo.

    def __init__(self, matriz_inicial, palavra):
        super().__init__(palavra)
        self.palavra = palavra
        self.movimentos = Movimentos(matriz_inicial)

    def _primeiro_movimento(self, posicao_linha_atual, posicao_letra_atual):
        # Método sobrescrito da classe VerificarBase e executa o primeiro movimento na ordem de execução do zig-zag.
        return self.movimentos.mover_para_baixo(posicao_linha_atual, posicao_letra_atual)

    def _segundo_movimento(self, posicao_linha_atual, posicao_letra_atual):
        # Método sobrescrito da classe VerificarBase e executa o segundo movimento na ordem de execução do zig-zag.
        return self.movimentos.mover_para_direita(posicao_linha_atual, posicao_letra_atual)
