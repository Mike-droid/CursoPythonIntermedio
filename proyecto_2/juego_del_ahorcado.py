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
  if platform.system() == "Linux" or platform.system() == "Darwin":
    os.system('clear')
  else:
    os.system('cls')


def play_game():
  with open('./archivos/data.txt' , 'r' , encoding='utf-8') as f:
    words = [word for word in f]

    random_index = random.randint(1 , len(words))

    blank_word = []

    for _ in range(len(words[random_index]) -1 ):
      blank_word.append(" _ ")

    listToString = ''.join(map(str , blank_word))

    menu = f"""
    ¡Bienvenido al juego del ahorcado!
    {listToString} = {words[random_index]}
    Adivina la palabra misteriosa
    """
    print(menu)

    try:
      while True:
        newLetter = input("Inserta una letra: ")
        if type(newLetter) != str:
          raise ValueError("Solo puedes insertar letras")
        if newLetter in words[random_index]:
          print('Correcto')
          word_to_list = list(words[random_index])
          for i in word_to_list:
            if i == newLetter:
              blank_word.pop(word_to_list.index(i))
              blank_word.insert(word_to_list.index(i) , newLetter)
          print(blank_word)
        else:
          print('Incorrecto')
    except ValueError as ve:
      print(ve)


def run():
  clearTerminal()
  play_game()


if __name__ == '__main__':
  run()