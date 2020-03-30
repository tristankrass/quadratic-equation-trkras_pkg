# quadratic-equation

[Link to Pypi](https://test.pypi.org/project/qequation-trkras-pkg/0.0.1/)

### How to use?

Install the package
```
pip install -i https://test.pypi.org/simple/ qequation-trkras-pkg==1.0
```

make a new python file and import the package
```python
import quadradic_solver.main as quadradic_solver


quadradic_solver.ask_user_input(1, 0, 0) # This will call  the solve equaiton with user inputs.

quadradic_solver.solve_equation() # Main function is solve_equation
```

This function will ask input from user and decides whether or not the equation has
possible solutions or not. The method return tuple. If there are no solutions then a tuple
of (-1, -1) will be returned and accompanying message will be printed out to the command line. 

DEMO:
```
Insert square member(x^2): 2
Insert member(x): 2
Insert free member(c): 0
The solution is: 0.0 -4.0
```

### Running tests

```
cd tests

python -m pytest
```