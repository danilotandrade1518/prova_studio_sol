class InputPalavras:
    # Classe responsável por receber e validar as entradas de dados feitas pelo usuário

    def get_palavras(self):
        # Método responsável por solicitar a entrada de dados do usuário, executar a validação desses dados e
        # posteriormente retornar a lista de palavras informadas separadas por ","(vírgula)

        self._palavras = input("\nDigite as palavras à serem buscadas separadas por vírgula e tecle 'Enter': ")
        self._validar_palavras()
        return self._palavras.split(",")

    def _validar_palavras(self):
        # Método responsável por realizar a validação da entrada de dados do usuário.

        if not all(caracter.isalpha() or caracter == "," for caracter in self._palavras):
            print('\nPor favor, informe apenas letras sem acentuação e sem espaços em branco!')
            self.get_palavras()
            self._validar_palavras()
