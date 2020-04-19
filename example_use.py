import quadradic_solver.main as quadradic_solver

def ask_user_input():
    a = input("Insert square member(x^2): ")
    b = input("Insert member(x): ")
    c = input("Insert free member(c): ")
    if (len(a) == 0 or len(b) == 0 or len(c) == 0):
      print("Please add values for all operands!")
      return
    return quadradic_solver.solve_equation(a, b, c)

if __name__ == "__main__":
    print(ask_user_input()) # Insert your own values from command line