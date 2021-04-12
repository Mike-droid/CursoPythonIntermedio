import os
import platform
import random

HANGMANPICS = ['''
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


def clearTerminal():
  if platform.system() == 'Linux' or platform.system() == 'Darwin':
    os.system('clear')
  else:
    os.system('cls')


def play_game():
  with open('./archivos/data.txt' , 'r' , encoding='utf-8') as f:
    words = [word for word in f]

    random_number = random.randint(1 , len(words))

    blank_word = []

    for _ in range(len(words[random_number]) -1 ):
      blank_word.append(' _ ')

    listToString = ''.join(map(str , blank_word))

    menu = f"""
    ¡Bienvenido al juego del ahorcado!
    {listToString}
    Adivina la palabra misteriosa
    ANTES DE JUGAR: Toma en cuenta que las letras con tildes serán diferentes a las letras sin tildes.
    """
    print(menu)

    flag_win = False

    try:
      correct_tries = 0
      incorrect_tries = 0
      while not flag_win:
        newLetter = input('Inserta una letra: ')
        if type(newLetter) != str:
          raise ValueError('Solo puedes insertar letras')
        if newLetter in words[random_number]:
          correct_tries += 1
          print('Correcto')
          word_to_list = list(words[random_number])
          for count , letter in enumerate(word_to_list):
            if letter == newLetter:
              blank_word[count] = newLetter
          print(blank_word)
          if ' _ ' not in blank_word:
            print(f'¡Has ganado! Te ha tomado: {correct_tries + incorrect_tries} intentos')
            flag_win = True
        else:
          print('Incorrecto')
          incorrect_tries+=1
          print(HANGMANPICS[incorrect_tries])
          if incorrect_tries == 6:
            print(f'¡Has fallado! :( La palabra era: {words[random_number]} y lo intentaste: {correct_tries + incorrect_tries} veces')
            break
    except ValueError as ve:
      print(ve)


def run():
  clearTerminal()
  play_game()


if __name__ == '__main__':
  run()