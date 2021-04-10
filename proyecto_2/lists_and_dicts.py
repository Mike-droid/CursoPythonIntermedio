def run():
  my_list = [1, "Hello", True, 4.5] #!Lista
  my_dict = {"firstname": "Miguel" , "lastname": "Reyes"} #!Diccionario

  super_list = [ #!Lista de diccionarios
    {"firstname": "Miguel" , "lastname": "Reyes"},
    {"firstname": "Facundo" , "lastname": "García"},
    {"firstname": "Oscar" , "lastname": "Guerra"},
    {"firstname": "Ximena" , "lastname": "Ruíz"},
  ]

  super_dict = { #! Diccionario de listas
    "natural_nums": [1,2,3,4,5],
    "integer_nums": [-1, -2 ,0 ,1 ,2],
    "floating_nums": [1.1, 4.5, 6.43]
  }

  for key, value in super_dict.items():
    print(key, "-" , value)


  for item in super_list:
    print(item["firstname"] , "-" , item["lastname"])


if __name__ == '__main__':
  run()