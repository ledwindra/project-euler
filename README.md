![build](https://github.com/ledwindra/project-euler/workflows/build/badge.svg?branch=master)

# About

Hello world :earth_asia:! Are you into mathematics and computer programming? Then [<strong>`Project Euler`</strong>](https://projecteuler.net/about) is a good platform for you. They say the users are allowed to share and discuss the first 100 problems outside of their platform. So here I am. :sunglasses:

# Run

As of now, I rely on [<strong>`Python (3.x)`</strong>](https://www.python.org/downloads/) to solve the problems. The <strong>`project_euler.py`</strong> file can be used as a module, which consists of the problems and answers. Below is the example when you do this on the console:

```python
>>> from project_euler import ProjectEuler
>>> project_euler = ProjectEuler() # assign object
>>> project_euler.problem_one(1000) # solve problem one
233168
>>> project_euler.problem_two() # solve problem two
4613732
```

If instead you want to run the unit test, you can just run the <strong>`test_project_euler.py`</strong> file as follows:

```
python test_project_euler.py
```

If passed, it will show the following result:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Enjoy! :sunglasses: :beers:
