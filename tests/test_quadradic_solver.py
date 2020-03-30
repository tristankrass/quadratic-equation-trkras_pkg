"""Test possible values for quadratic solver."""
import quadradic_solver.main as quadradic_solver


def test_correct_quadratic_values():
  assert quadradic_solver.solve_equation(1, -1, 0) == (1.0, 0.0)
  assert quadradic_solver.solve_equation(3, -3, -6) == ((18.0, -9.0))

def test_wrong_quadratic_values():
  assert quadradic_solver.solve_equation("a", "b", "c") == (-1, -1) 
  assert quadradic_solver.solve_equation(2, -6, 5) == (-1, -1) 

def test_determinant_equal_zero():
  assert quadradic_solver.solve_equation(1, 0, 0) == (0.0, 0.0) 
  assert quadradic_solver.solve_equation(5, 0, 0) == (0.0, 0.0)

