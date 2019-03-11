from jogo.input_palavras import InputPalavras
from jogo.jogo import Jogo
from jogo.matriz import Matriz
from jogo.resultado import Resultado
from jogo.util import print_matriz

# Arquivo de inicialização do programa, responsável por iniciar a interação com o usuário e inicializar as classes
# responsáveis pelo jogo

print('''
    Seja bem vindo(a) ao Caça-palavras Zig-Zag!
    Diferente do Caça-palavras original as palavras serão buscadas em Zig-Zag nos seguintes sentidos:
    - direita → e abaixo ↓;
    - direita → e acima ↑;
    - esquerda ← e abaixo ↓;
    - esquerda ← e acima ↑;
    - abaixo ↓ e à direita →;
    - abaixo ↓ e à esquerda ←;
    - acima ↑ e à direita →;
    - acima ↑ e à esquerda ←.    
    Boa sorte e encontre o máximo de palavras que puder!
''')

matriz = Matriz()
print_matriz(matriz._matriz_inicial)

while True:
    input_palavras = InputPalavras()
    palavras = input_palavras.get_palavras()

    jogo = Jogo(matriz._matriz_inicial, palavras)
    ocorrencias = jogo.jogar()

    resultado = Resultado(matriz._matriz_inicial, ocorrencias)
    resultado.print_resultado()
