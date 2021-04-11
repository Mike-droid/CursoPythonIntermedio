def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 0]
  return divisors


def run():
  try:
    num = int(input("Inserta un número: "))
    if num <= 0:
      raise ValueError("Debes ingresar un número positivo")
    print(divisors(num))
  except ValueError as ve:
    print(ve)
  print("Terminó el programa")


if __name__ == '__main__':
  run()