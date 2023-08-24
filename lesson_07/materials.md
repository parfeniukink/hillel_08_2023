1. Python documentation on `contextlib` module: The `contextlib` module in Python provides utilities for working with context managers. It contains the necessary functions and classes for creating and using context managers. You can find the documentation at:
	- [https://docs.python.org/3/library/contextlib.html](https://docs.python.org/3/library/contextlib.html)
2. Real Python - "Python Context Managers and the "`with`" Statement" tutorial: This tutorial from the Real Python website explains the concept of context managers in Python and how to use the `with` statement effectively. It provides code examples and practical use cases.
	- [https://realpython.com/python-with-statement/](https://realpython.com/python-with-statement/)
3. Python documentation on `with` statement: The official Python documentation explains the `with` statement in detail and how it works in conjunction with context managers. You can find the documentation at:
	- [https://docs.python.org/3/reference/compound_stmts.html#the-with-statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
4. Python contextlib - Context Manager Types: This section of the Python documentation covers the various context manager types available in the contextlib module. It includes examples and explanations of each type.
	- [https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager)

A basic example of a context manager in Python using the `with` statement can be found below:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        # Perform any setup or resource allocation here
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        # Perform any cleanup or resource deallocation here
    
    def do_something(self):
        print("Doing something in the context")

# Using the context manager
with MyContextManager() as my_context:
    my_context.do_something()
```


In this example, we define a class `MyContextManager` that acts as a context manager by implementing the `__enter__` and `__exit__` methods. The `__enter__` method is called when the `with` statement is entered, and it returns the context manager object. The `__exit__` method is called when the `with` statement is exited, even in the case of an exception being raised within the `with` block.

Inside the `with` block, we can perform any actions using the context manager object, which in this example is calling the `do_something` method.

When the `with` block is exited, the `__exit__` method is called, allowing us to perform any necessary cleanup or resource deallocation.

This is a basic example, but it demonstrates the essential structure of a context manager. More complex context managers can be created to handle specific scenarios, such as file handling or database connections.
