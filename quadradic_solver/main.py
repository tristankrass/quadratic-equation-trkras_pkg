from math import sqrt

def ask_user_input():
    a = input("Insert square member(x^2): ")
    b = input("Insert member(x): ")
    c = input("Insert free member(c): ")
    if (len(a) == 0 or len(b) == 0 or len(c) == 0):
      print("Please add values for all operands!")
      return
    return solve_equation()

def solve_equation(a, b, c) -> tuple:
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


if __name__ == "__main__":
    print(solve_equation(1, 0, 0))
   # print(solve_equation(3, -3, -6))
    #assert solve_equation("a", "b", "c") == (-1, -1)