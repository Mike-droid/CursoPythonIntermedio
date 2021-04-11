def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 0]
  return divisors


def run():
  """ num = input("Inserta un número: ")
  assert num.isnumeric() , "Debes ingresar un número"
  print(divisors(int(num)))
  print("Terminó el programa") """
  num = int(input("Ingresa un número: "))
  assert num >= 1 , "Debes ingresar un número positivo"
  print(divisors(int(num)))
  print("Terminó el programa")


if __name__ == '__main__':
  run()