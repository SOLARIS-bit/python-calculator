# Python Calculator Project
Section 1 – Git Collaboration 

 

Workflow description: 

 The main branch `main` contains stable, functional code. 

 Feature development on dedicated branches: 

   `feature/calculator` for developing `calculator.py`. 

   `feature/tests` for unit and integration testing. 

 Simulation and resolution of conflicts during merges. 

 Clear and frequent commits to track the history of changes.  

```bash 

Git log –graph –oneline –all 

``` 

## Section 2 – Testing and Quality 

 

Tools used: 

 
 `pytest` for unit and integration testing. 

 `flake8` for code quality (linting). 

 `coverage` for test coverage. 

 

1. `pytest` results showing all tests passed. 

2. `flake8` results showing 0 errors. 

3. `coverage report -m` report with 100% coverage. 

 

## Section 3 – Integration 

 

Running the script: 

 

```bash 

python3 src/calculator.py 

``` 

 

Example session: 

 

``` 

=== Python Calculator === 

1. Add 

2. Subtract 

3. Multiply 

4. Divide 

5. Exit 

Choose operation: 1 

Enter first number: 3 

Enter second number: 4 

Result: 7.0 

 

Choose operation: 2 

Enter first number: 10 

Enter second number: 5 

Result: 5.0 

 

Choose operation: 3 

Enter first number: 3 

Enter second number: 5 

Result: 15.0 

 

Choose operation: 4 

Enter first number: 12 

Enter second number: 3 

Result: 4.0 

 

Choose operation: 5 

``` 
 

## Section 4 – Conclusion 

 

What I learned: 

 Managing Git branches, merges, and conflict resolution. 

 Quality assurance with linting (`flake8`) and automated testing (`pytest`). 

 Measuring and tracking test coverage with `coverage`. 

 Separating code between logic and user interface for testability. 

 Importance of a collaborative Git workflow and reliable testing to ensure a stable project. 

 
