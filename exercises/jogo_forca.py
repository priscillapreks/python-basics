# Hangman Game (Jogo da Forca)

# Import
import random

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # Adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Verifica se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters)==6)

    # Verifica se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Verifica o status do game e imprime o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ', )
        for letter in self.missed_letters:
            print(letter, )
        print()
        print('Letras corretas: ', )
        for letter in self.guessed_letters:
            print(letter, )
        print()


# Escolhe uma palavra aleatória do banco de palavras
def rand_word():
    with open("forca_palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Método de execução do programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # Imprime o resultado na tela
    if game.hangman_won():
        print('\nParabéns! Você venceu!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)



# Executa o programa
if __name__=="__main__":
    main()