from math import sqrt

def solve_equation(a : str, b : str, c : str) -> tuple:
  try:
    a = int(a)
    b = int(b)
    c = int(c)
    d = sqrt(b**2 - 4 * a * c)
    if d < 0:
      raise ValueError 
    
    x_1 = (-b + d) / 2 * a
    x_2 = (-b - d) / 2 * a
    if d > 0:
      print("The solution is: " +  str(x_1) + ", " + str(x_2))
    else: 
      print("There is only one solution: " + str(x_1))
      
    return x_1, x_2

  except ValueError as e:
    print("This equation does not have any solutions")
    return (-1, -1)