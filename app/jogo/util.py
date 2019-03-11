def print_matriz(matriz):
    # Método utilitário responsável por imprimir a matriz na formatação padrão do programa

    for linha in matriz:
        row_format = "{:>3}" * (len(linha) + 1)
        print(row_format.format("", *linha))
