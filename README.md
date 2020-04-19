# quadratic-equation

[Link to Pypi](https://test.pypi.org/project/qequation-trkras-pkg/)

### !UPDATE How to use?
Install the package
```
python3 -m pip install --index-url https://test.pypi.org/simple/ qequation-trkras-pkg --no-deps qequation-trkras-pkg
```

make a new python file and import the package
```python
import quadradic_solver.main as quadradic_solver

quadradic_solver.solve_equation("1", "0", "0") # Main function is solve_equation
# Output -> There is only one solution: 0.0
# (0.0, 0.0)
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

### Sample use
Open the `example_use.py` file. Install the pip package. Run the example file.
```
python3 example_use.py
```

### Running tests

```
cd tests

python -m pytest
```