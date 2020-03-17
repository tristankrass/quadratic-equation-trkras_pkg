from math import sqrt

def solve_equation() -> list:
  x2 = input("Insert square member(x^2): ")
  x = input("Insert member(x): ")
  c = input("Insert free member(c): ")
  if (len(x2) == 0 or len(x) == 0 or len(c) == 0):
    print("Please add values for all operands!")
    return
  x2 = int(x2)
  x = int(x)
  c = int(c)
  if x == 0:
    print("This values cannot make a quadratic equation.")
    return
  try:
    x_1 = (-x + sqrt(x**2 - 4 * x2 * c)) / 2 * x2
    x_2 = (-x - sqrt(x**2 - 4 * x2 * c)) / 2 * x2
    print("The solution is: " +  str(x_1) + " " + str(x_2))
    return [x_1, x_2]
  except ValueError as e:
    print("This equation does not have any solutions")
