
# MLOps — Python Unit Testing with Pytest

A collection of hands-on exercises exploring Python unit testing, Test-Driven Development (TDD), test automation, and code coverage.

## Technologies

- Python 3.11
- pytest
- pytest-cov
- Git and GitHub

## Project Structure

```text
pytest-mlops-lab/
├── unit_testing_simple/
├── unit_testing_best_practice/
├── user_registration/
├── prime_checker/
├── .gitignore
└── README.md
```

## Exercises

### 1. Basic Unit Testing

Introduction to writing test functions using pytest and Python assertions.

### 2. Unit Testing Best Practices

Organizing source code and tests into separate directories, using Python packages and imports.

### 3. User Registration Validation

Implementation and testing of:

- Username validation and banned words
- Email validation
- Handle validation
- Default handle selection
- Interactive user registration
- Automated input simulation using monkeypatch

**Results:** 28 tests passed.

### 4. Prime Number Checker — TDD

Implementation of a prime-number checking algorithm, with tests covering:

- Prime numbers
- Composite numbers
- Zero and one
- Negative numbers
- Larger numbers

**Results:** 25 tests passed.

## Running the Tests

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install pytest pytest-cov
```

Run the registration tests:

```bash
cd user_registration
python -m pytest -v
```

Return to the project root and run the prime checker tests:

```bash
cd ../prime_checker
python -m pytest -v
```

## Code Coverage

From the `prime_checker` directory:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
python -m pytest --cov=src --cov-report=html
```

The prime checker achieved **100% statement coverage** with 25 passing tests.

## Learning Outcomes

- Writing automated unit tests with pytest
- Using parameterized test cases
- Testing valid and invalid inputs
- Applying Test-Driven Development
- Mocking interactive input with monkeypatch
- Measuring code coverage
- Organizing and version-controlling Python projects

## Results

| Exercise | Tests Passed |
|---|---:|
| User Registration | 28 |
| Prime Checker | 25 |
| **Total** | **53** |

The 53 tests represent the registration and prime-checker suites. The introductory exercises are maintained separately.

## Course

MSc Data Science & Artificial Intelligence — MLOps practical exercises.
