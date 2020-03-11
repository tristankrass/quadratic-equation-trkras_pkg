# quadratic-equation

[Link to Pypi](https://test.pypi.org/project/qequation-trkras-pkg/0.0.1/)

### How to use?

Install the package
```
pip install -i https://test.pypi.org/simple/ qequation-trkras-pkg==0.0.1
```

make a new python file and import the package
```python
import quadradic_solver.main as quadradic_solver

quadradic_solver.solve_equation() ## Main function is solve_equation
```
This function will ask input from user and decides whether or not the equation has
possible solutions or not. The method return the list of two possible solutions.

DEMO:
```
Insert square member(x^2): 2
Insert member(x): 2
Insert free member(c): 0
The solution is: 0.0 -4.0
```