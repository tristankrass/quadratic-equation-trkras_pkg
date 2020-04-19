from math import sqrt

def solve_equation(a, b, c) -> tuple:
  try:
    a = int(a)
    b = int(b)
    c = int(c)
    d =  b**2 - ( 4 * a * c)
    d_sqrt = sqrt(d)

    if d < 0:
      raise ValueError 
    
    x_1 = (-b + d_sqrt) / (2 * a)
    x_2 = (-b - d_sqrt) / (2 * a)

    return x_1, x_2

  except ValueError as e:
    return (-1, -1)
