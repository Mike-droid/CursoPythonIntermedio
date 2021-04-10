def run():
  import math
  """ squares = []
  for i in range(1,101):
    if i % 3 == 0:
      continue
    else:
      squares.append(i**2)

  print(squares) """

  #squares = [i**2 for i in range(1,101) if i % 3 != 0]
  #print(squares)

  lcm = math.lcm(4,6,9)

  my_list = [i for i in range(1,100000) if i % lcm == 0] #!36 es el mínimo común múltiplo de 4, 6 y 9
  print(my_list)


if __name__ == "__main__":
  run()